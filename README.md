# Online Shoppers ML Projesi

Online Shoppers Intention veri seti ile ziyaret�i davran��lar�ndan gelir �retme olas�l���n� tahmin etmeye y�nelik bir u�tan uca makine ��renmesi projesi. Depoda veri ke�fi, modelleme, �zellik m�hendisli�i, model optimizasyonu ve basit bir FastAPI tabanl� servis iskeleti bulunur.

## Klas�r Yap�s�
- `data/`: Ham ve i�lenmi� veri dosyalar�.
- `docs/`: Ad�m ad�m proje dok�mantasyonu i�in �ablon dosyalar�.
- `models/`: E�itilmi� model ve se�ili �zellik dosyalar�.
- `notebooks/`: Ke�if ve modelleme s�recine ait notebook iskeletleri.
- `src/`: Python mod�lleri, FastAPI uygulamas� ve testler.

## H�zl� Ba�lang��
1. Ba��ml�l�klar� kur: `pip install -r requirements.txt`
2. Veri dosyas�n� `data/raw/online_shoppers_intention.csv` yoluna yerle�tir.
3. E�itim iskeletini �al��t�r (�rn. `python -m src.pipeline`).
4. FastAPI servisini �al��t�r: `uvicorn src.app:app --reload`.

## Not
Bu depo temel iskeleti i�erir; veri temizleme, �zellik se�imi ve model konfig�rasyonunu proje gereksinimlerine g�re doldurulacak.
