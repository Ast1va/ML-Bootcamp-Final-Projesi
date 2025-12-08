# Final Pipeline & Deployment Readiness

Bu belge, final model/pipeline seçimini, kullanılan özellik ve ön işleme adımlarını, üretimsel hazırlığı ve izleme metriklerini tek yerde özetler. Aşağıdaki maddeler, ödevde sorulan 8 başlığın son durumunu da bağlar.

## 1) Problem Tanımı
- Tek oturum verisinden `Revenue` (satın alma) olasılığını tahmin etmek (Online Shoppers Purchasing Intention).
- Pozitif sınıf (~%15,5) az; hedef, satın alma eğilimini yakalamak.

## 2) Baseline Süreci ve Skor
- Lojistik Regresyon (class_weight=balanced): Accuracy 0.8500, ROC-AUC 0.8963, Precision 0.51, Recall 0.75, F1 0.61 (20% test).
- Referans olarak kullanıldı; Recall/F1 iyileştirme ihtiyacı görüldü.

## 3) Feature Engineering Denemeleri
- Türetilenler: `Total_Duration`, `PageValue_per_Product`, `Is_HighSeason`, `Is_ReturningVisitor`.
- Amaç: Oturum süresi ve değer yoğunluğunu, sezonsallığı ve geri dönen ziyaretçi sinyalini eklemek.
- Sonuç: AUC ve pozitif sınıf Recall/F1 artışı; RF/LightGBM ile anlamlı kazanç (AUC ~0.93, Recall ~0.76).

## 4) Validasyon Şeması
- Stratified 80/20 train/test (2466 test örneği), sınıf dağılımı korunur.
- Hiperparametre aramalarında 3-fold stratified CV.

## 5) Final Pipeline (Özellik ve Ön İşleme)
- Özellik seti: 17 özgün + 4 FE türevi = 21 sütun (one-hot sonrası ~30+).
- Ön işleme: ColumnTransformer; sayısal → StandardScaler, kategorik (`Month`, `VisitorType`, `Weekend`) → OneHotEncoder(handle_unknown="ignore").
- Model: **RandomForest (tuned)** seçildi.
- Hiperparametreler: n_estimators=400, max_depth=10, max_features="sqrt", min_samples_split=5, min_samples_leaf=8, random_state=42.
- Artefakt: `models/final_rf_pipeline.pkl` (aktif). İsterseniz LightGBM alternatifi `models/final_lgbm_pipeline.pkl` olarak saklanabilir.

## 6) Final Model ↔ Baseline Farkı
- Baseline (LogReg bal.): ROC-AUC 0.8963, Recall 0.75, F1 0.61.
- Final (RF tuned): ROC-AUC 0.9296, Recall 0.7723, F1 0.6469.
- Kazanç: AUC +0.03, F1 (pozitif) +0.04; Recall korunup iyileşti.

## 7) İş Uyumu
- Pozitif sınıfı kaçırmamak kritik (Recall öncelikli); precision dengesi korunuyor.
- Özellikler iş açısından anlamlı: sayfa değerleri, çıkış oranı, süreler, sezon, geri dönüş.
- Web UI ve JSON API ile sonuçlar olasılık + karar formatında sunuluyor.

## 8) Canlıya Alma ve İzleme
- Deployment: FastAPI (bkz. `docs/api_deployment.md`), Render start komutu: `uvicorn src.app:app --host 0.0.0.0 --port $PORT`.
- İzleme metrikleri: pozitif Recall/Precision/F1, PR-AUC; sınıf dağılımı; feature drift (özellikle `PageValues`, `ExitRates`, `Month_*`); latency.
- Eşik ayarı: İş gereksinimine göre `Revenue=True` eşiği yeniden kalibre edilebilir; izleme sırasında gerekirse threshold tuning yapılmalı.

## Inference Akışı (Kısa)
1) Giriş JSON/form → doğrulama (`src.app` / `src.inference`).  
2) Ön işleme pipeline (scaler + one-hot + FE’li özellik sırası).  
3) Model tahmini → olasılık + karar döner.  
4) Loglama: giriş/çıkış (kişisel veri yok), hata/latency metrikleri.
