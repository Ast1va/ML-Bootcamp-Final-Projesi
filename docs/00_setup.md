# Kurulum

## Önkoşullar
- Python 3.12.x
- pip veya uv, ve git kurulu olmalı

## Kurulum

### Depoyu klonla
```bash
git clone https://github.com/Ast1va/ML-Bootcamp-Final-Projesi.git
cd online-shoppers-ml-project
```

### Sanal ortam oluştur ve etkinleştir
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

### Bağımlılıkları yükle
```bash
pip install -r requirements.txt
```
(Tercihen uv kullanıyorsanız: `uv sync`)

### FastAPI uygulamasını çalıştır
```bash
uvicorn src.app:app --reload
```
- Web arayüzü: http://127.0.0.1:8000/
- Swagger dokümanı: http://127.0.0.1:8000/docs

### Notebookları çalıştır
```bash
jupyter lab
```
Sırayla:
- `notebooks/modeling/00_EDA.ipynb`
- `notebooks/modeling/01_Baseline.ipynb`
- `notebooks/modeling/02_Feature_Engineering.ipynb`
- `notebooks/modeling/03_Model_Optimization.ipynb`
- `notebooks/modeling/04_Evaluation.ipynb`
- `notebooks/modeling/05_Final_Pipeline.ipynb`

### Bağımlılıklar
**Çekirdek:** pandas, numpy, scikit-learn, lightgbm, fastapi, uvicorn, pydantic, python-multipart, jinja2  
**Geliştirme:** jupyter, matplotlib, seaborn

## Proje Yapısı
```
online-shoppers-ml-project/
|-- data/                 # (gerekirse veri dosyaları)
|-- models/               # Kaydedilmiş model(ler)
|   `-- final_rf_pipeline.pkl
|-- notebooks/
|   `-- modeling/
|       |-- 00_EDA.ipynb
|       |-- 01_Baseline.ipynb
|       |-- 02_Feature_Engineering.ipynb
|       |-- 03_Model_Optimization.ipynb
|       |-- 04_Evaluation.ipynb
|       `-- 05_Final_Pipeline.ipynb
|-- src/
|   |-- app.py
|   |-- config.py
|   |-- inference.py
|   `-- templates/
|       `-- index.html
|-- docs/
|   `-- 00_setup.md
`-- requirements.txt
```

## Dağıtım
- Uygulama Render üzerinde yayında:  
  https://ml-bootcamp-final-projesi.onrender.com
