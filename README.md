# Online Shoppers ML Projesi

Online Shoppers Intention veri seti ile ziyaretçi davranýþlarýndan gelir üretme olasýlýðýný tahmin etmeye yönelik bir uçtan uca makine öðrenmesi projesi. Depoda veri keþfi, modelleme, özellik mühendisliði, model optimizasyonu ve basit bir FastAPI tabanlý servis iskeleti bulunur.

## Klasör Yapýsý
- `data/`: Ham ve iþlenmiþ veri dosyalarý.
- `docs/`: Adým adým proje dokümantasyonu için þablon dosyalarý.
- `models/`: Eðitilmiþ model ve seçili özellik dosyalarý.
- `notebooks/`: Keþif ve modelleme sürecine ait notebook iskeletleri.
- `src/`: Python modülleri, FastAPI uygulamasý ve testler.

## Hýzlý Baþlangýç
1. Baðýmlýlýklarý kur: `pip install -r requirements.txt`
2. Veri dosyasýný `data/raw/online_shoppers_intention.csv` yoluna yerleþtir.
3. Eðitim iskeletini çalýþtýr (örn. `python -m src.pipeline`).
4. FastAPI servisini çalýþtýr: `uvicorn src.app:app --reload`.

## Not
Bu depo temel iskeleti içerir; veri temizleme, özellik seçimi ve model konfigürasyonunu proje gereksinimlerine göre doldurun.
