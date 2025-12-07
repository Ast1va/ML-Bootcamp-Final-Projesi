# Online Shoppers ML Servisi

Online Shoppers Intention verisinden ziyaretçilerin satın alma (Revenue) olasılığını tahmin eden uçtan uca makine öğrenmesi projesi. Veri hazırlama, model eğitimi, model artefaktları ve FastAPI tabanlı basit bir arayüz içerir.

## Hızlı Özet (gereksinim yanıtları)
1) Problem: E-ticaret ziyaretçisinin satın alma yapma olasılığını öngörmek.  
2) Baseline: One-hot encoded basit RandomForest; doğruluk 0.899 (stratified 80/20).  
3) Feature eng: Kategorik alanlarda one-hot; henüz ek türetme yok (iyileştirme listede).  
4) Validasyon: Stratified train/test (0.2); k-fold veya zaman serisi şeması henüz yok.  
5) Final pipeline: One-hot + RandomForest; artefaktlar `models/final/*` altında.  
6) Baseline vs final: Şu an aynı model; iyileştirme için LightGBM, eşik optimizasyonu planlandı.  
7) İş uyumu: Pozitif sınıf olasılığı raporlanıyor; iş kuralına göre karar eşiği ayarlanmalı ve izlenmeli.  
8) Canlıya alma: FastAPI servisi hazır; Render/HF Space/VM’de uvicorn ile yayımlanabilir; izleme için accuracy/F1, sınıf dağılımı ve drift (PSI) takip edilmeli.

## Demo / İnference
- Yerel UI: `uvicorn src.app:app --reload` → `http://127.0.0.1:8000`
- JSON endpoint: `POST http://127.0.0.1:8000/predict.json`
- Canlı deploy linki: Henüz yok (Render / HuggingFace Space gibi ortamlara taşınabilir).

## Veri, Pipeline ve Metrikler
- Veri: 12.330 satır, 17 özellik + hedef (`Revenue`); pozitif sınıf oranı ~%15,5.  
- Ön işleme: Kategorik alanlar için one-hot encoding; sayısal alanlar doğrudan kullanılır.  
- Model: RandomForestClassifier (n_estimators=200, max_depth=None, random_state=42).  
- Doğrulama: Stratified train/test (test_size=0.2).  
- Sonuçlar (örnek koşu): accuracy 0.899, pozitif sınıf f1 0.63 (dengesiz veri).  
- Artefaktlar: `models/final/final_model.pkl`, `models/final/selected_features.json`.

## Teknolojiler
Python 3.10+, pandas, numpy, scikit-learn, fastapi, uvicorn, joblib, shap, matplotlib, seaborn, jinja2.

## Kurulum
1. (Opsiyonel) Sanal ortam oluşturun: `python -m venv venv && venv\Scripts\activate`
2. Bağımlılıkları kurun: `pip install -r requirements.txt`
3. Veriyi yerleştirin: `data/raw/online_shoppers_intention.csv`

## Model Eğitimi
Eğitim ve artefakt kaydetme:
```bash
python -m src.pipeline
```
Çıktılar: `models/final/final_model.pkl` ve `models/final/selected_features.json`.

## Servisi Çalıştırma (FastAPI)
```bash
uvicorn src.app:app --reload
```
- Form tabanlı: `http://127.0.0.1:8000`
- JSON isteği örneği:
```json
{
  "Administrative": 2,
  "Administrative_Duration": 60,
  "Informational": 0,
  "Informational_Duration": 0,
  "ProductRelated": 20,
  "ProductRelated_Duration": 1200,
  "BounceRates": 0.02,
  "ExitRates": 0.04,
  "PageValues": 35.7,
  "SpecialDay": 0.0,
  "Month": "Nov",
  "OperatingSystems": 2,
  "Browser": 3,
  "Region": 1,
  "TrafficType": 2,
  "VisitorType": "Returning_Visitor",
  "Weekend": false
}
```

## Repo Yapısı
- `data/` ham ve işlenmiş veri
- `docs/` deney ve rehber dokümanları
- `models/` model ve özellik listesi artefaktları
- `notebooks/` EDA ve modelleme notebook’ları
- `src/` kod (pipeline, inference, API, template, test iskeleti)

## Ekran / Görseller
- `confusion_matrix.png`: örnek model çıktısı (lokal).

## İletişim
Sorun/öneri için GitHub Issues üzerinden bildirebilirsiniz.
