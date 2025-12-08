# Evaluation & Final Model Summary

## Amaç
Modelleme sürecinin çıktısını, kullanılan doğrulama şemasını ve final model seçim gerekçesini özetler; üretim izlemesi için odak metrikleri belirtir.

## Veri ve Validasyon
- Veri: 12.330 satır, 17 özellik + hedef (`Revenue`), pozitif oranı ~%15,5.
- Split: Stratified 80/20 (train 9.864, test 2.466) – tüm metrikler bu test seti üzerindedir.
- Tuning sırasında 3-fold stratified CV kullanıldı.

## Metrik Özeti (20% Test)
| Model | Accuracy | ROC-AUC | Precision (Rev=1) | Recall (Rev=1) | F1 (Rev=1) |
|-------|----------|---------|-------------------|----------------|------------|
| LogReg (class_weight=balanced, FE yok) | 0.8500 | 0.8963 | 0.51 | 0.75 | 0.61 |
| RF (FE, untuned) | 0.8966 | 0.9247 | 0.73 | 0.53 | 0.62 |
| RF (FE, tuned) | 0.8694 | 0.9296 | 0.5566 | 0.7723 | 0.6469 |
| LightGBM (FE, tuned) | 0.8812 | 0.9275 | 0.5903 | 0.7618 | 0.6651 |

## Değerlendirme
- **Sınıf dengesizliği** nedeniyle pozitif sınıfta Recall/F1 kritik; ROC-AUC tek başına yeterli değil.
- FE + tuning, pozitif Recall/F1’yi anlamlı artırdı (LightGBM F1≈0.67, Recall≈0.76).
- RF tuned AUC biraz daha yüksek olsa da LightGBM metrikleri daha dengeli (precision/recall trade-off).

## Final Model Kararı
- Seçim: **RandomForest (tuned)**  
  - Özellik seti: FE sonrası 21 temel sütun + one-hot (Total_Duration, PageValue_per_Product, Is_HighSeason, Is_ReturningVisitor dahil).  
  - Ön işleme: Sayısal için StandardScaler, kategorik için OneHotEncoder(handle_unknown="ignore") via ColumnTransformer.  
  - Hiperparametreler: n_estimators=400, max_depth=10, max_features="sqrt", min_samples_split=5, min_samples_leaf=8, random_state=42.
- Gerekçe: Yüksek ROC-AUC (0.9296) ve pozitif sınıf Recall/F1 (0.77 / 0.65) ile dengeli performans; inference süresi sade ve anlaşılır pipeline.

**Alternatif:** LightGBM (tuned) benzer AUC ile biraz daha dengeli precision/recall sunar.

## İş Uyumu
- Pozitif sınıfı kaçırmamak (Recall) kritik; Precision makul seviyede tutuluyor.  
- Web UI ve JSON API ile tahminler açıklanabilir formatta (probability + karar).  
- Özellikler iş tarafından anlaşılır (süreler, sayfa değerleri, sezon/ziyaretçi bayrakları).

## İzleme ve Sonraki Adımlar
- Üretimde izlenecekler: pozitif Recall/Precision/F1, PR-AUC, sınıf dağılımı kayması, giriş feature drift (özellikle `PageValues`, `ExitRates`, `Month_*`).  
- Eşik ayarı: İş ihtiyacına göre olasılık eşiği yeniden kalibre edilebilir.  
- Genişletme: XGBoost denemesi, kalibrasyon (Platt/Isotonic), ve basit A/B eşiği testleri.
