# API Deployment Guide

FastAPI uygulaması, Online Shoppers Intention modelini kullanarak satın alma olasılığı tahmini yapar.

## Proje Yapısı
```
src/
├── config.py          # Yol ve ayarlar
├── inference.py       # Model yükleme ve tahmin
├── app.py             # FastAPI uygulaması
└── templates/
    └── index.html     # Web arayüzü
models/
└── final_rf_pipeline.pkl  # Eğitilmiş pipeline (FE + OneHot + RandomForest)
```

## Lokal Geliştirme
```bash
# Bağımlılıkları kur
pip install -r requirements.txt

# Sunucuyu çalıştır
uvicorn src.app:app --reload --port 8000
```
Ziyaret: http://localhost:8000

## API Uç Noktaları
- `GET /`        - Web arayüzü (form)
- `GET /health`  - Sağlık kontrolü
- `GET /features`- Beklenen özellik listesi
- `POST /predict.json` - JSON tahmin uç noktası
- `POST /predict` - Form tabanlı tahmin

## Örnek JSON İsteği
```bash
curl -X POST http://localhost:8000/predict.json \
  -H "Content-Type: application/json" \
  -d '{
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
  }'
```

## Örnek Yanıt
```json
{
  "prediction": false,
  "probability": 0.17,
  "message": "Satın alma beklenmiyor",
  "features_used": 17
}
```

## Render’a Deploy
1. Kodu GitHub’a pushla.
2. Render’da yeni Web Service oluştur.
3. Depoyu bağla.
4. Build: `pip install -r requirements.txt`
5. Start: `uvicorn src.app:app --host 0.0.0.0 --port $PORT`
6. Deploy et.

## Test
```bash
# (Varsa) testleri çalıştırmak için pytest
pytest
```
