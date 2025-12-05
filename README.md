# Online Shoppers ML Projesi

Online Shoppers Intention veri setiyle ziyaretçi davranışlarından gelir üretme olasılığını tahmin eden uçtan uca bir makine öğrenmesi projesi. Repoda veri hazırlama, model eğitimi, model saklama ve FastAPI ile gerçek zamanlı tahmin servisi yer alır.

## Proje İçeriği
- `data/`: Ham veri (`data/raw/online_shoppers_intention.csv`) ve işlenmiş veri klasörleri.
- `docs/`: Analiz ve deney adımlarına dair şablon dökümanlar.
- `models/`: Eğitilmiş model (`models/final/final_model.pkl`) ve özellik listesi (`models/final/selected_features.json`).
- `notebooks/`: EDA ve modelleme notebook’ları.
- `src/`: Eğitim pipeline’ı (`pipeline.py`), tahmin yardımcıları (`inference.py`), FastAPI servisi (`app.py`) ve Jinja2 template’i (`templates/index.html`).

## Kurulum
1. Python 3.10+ ortamı oluşturun (isteğe bağlı sanal ortam).
2. Bağımlılıkları kurun:
   ```bash
   pip install -r requirements.txt
   ```
3. Ham veri dosyasını `data/raw/online_shoppers_intention.csv` konumuna yerleştirin.

## Model Eğitimi
Eğitim pipeline’ı veriyi okur, temel one-hot encoding uygular, RandomForest modeli ile eğitir ve çıktıları kaydeder.
```bash
python -m src.pipeline
```
- Model: `models/final/final_model.pkl`
- Özellik sırası: `models/final/selected_features.json`

## Servisi Çalıştırma (FastAPI)
Uygulama, HTML formu ve JSON endpoint’i üzerinden tekil kayıt tahmini yapar.
```bash
uvicorn src.app:app --reload
```
- Tarayıcı: `http://127.0.0.1:8000` (form tabanlı tahmin)
- JSON isteği: `POST http://127.0.0.1:8000/predict.json`
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
    "Month": 6,
    "OperatingSystems": 2,
    "Browser": 3,
    "Region": 1,
    "TrafficType": 2,
    "VisitorType": "Returning_Visitor",
    "Weekend": false
  }
  ```

## Notlar
- Model dosyaları ve veri depoda yer alır; istenirse Git LFS’e taşınabilir.
- Template içinde yer alan form, beklenen alanlarla (`EXPECTED_FIELDS`) hizalıdır; yeni özellik eklerken aynı listeyi güncelleyin.***
