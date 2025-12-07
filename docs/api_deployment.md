# API Deployment (FastAPI)

## Yerel Çalıştırma
```bash
uvicorn src.app:app --reload
# http://127.0.0.1:8000
```

## Endpointler
- `GET /` : HTML formu (Jinja2 template, tek kayıt tahmini).
- `POST /predict` : Form post, tahmin sonucu aynı sayfada gösterilir.
- `POST /predict.json` : JSON giriş/çıkış.

### JSON Örnek İstek
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

## Yayına Alma Önerileri
- Render / HuggingFace Space / Heroku / VM: `uvicorn src.app:app --host 0.0.0.0 --port 8000`
- Artefaktları (model ve feature listesi) depoya dahil ettik; istenirse Git LFS’e taşınabilir.
- İzleme: istek sayısı, hata oranı, gecikme; model için sınıf dağılımı, accuracy/F1 ve drift (PSI) takibi.
