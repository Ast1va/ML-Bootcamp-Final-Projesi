# 00 - Setup ve Proje Yapısı

Bu doküman, ortam kurulumunu ve klasör yapısını özetler.

## Gereksinimler
- Python 3.10+
- pip veya conda
- Git (opsiyonel)

Temel paketler: pandas, numpy, scikit-learn, matplotlib, seaborn, shap, joblib, fastapi, uvicorn, jupyter.

## Kurulum Adımları
```bash
# (Opsiyonel) Sanal ortam
python -m venv venv
venv\Scripts\activate   # macOS/Linux: source venv/bin/activate

# Bağımlılıklar
pip install -r requirements.txt
```

## Veri
- Ham veri: `data/raw/online_shoppers_intention.csv`
- İşlenmiş veri: `data/processed/`

## Model ve Artefaktlar
- Model: `models/final/final_model.pkl`
- Özellik listesi: `models/final/selected_features.json`

## Çalıştırma
- Model eğitimi: `python -m src.pipeline`
- API (FastAPI): `uvicorn src.app:app --reload` → `http://127.0.0.1:8000`

## Klasör Yapısı
- `data/` ham ve işlenmiş veri
- `docs/` dokümantasyon
- `models/` eğitim çıktıları
- `notebooks/` EDA ve modelleme notebook’ları
- `src/` kod (pipeline, inference, API, template, test iskeleti)
