# Veri Özeti

Kaggle’dan Online Shoppers Purchasing Intention veri seti. Tek bir e-ticaret oturumunun satın alma ile sonuçlanıp sonuçlanmayacağını (Revenue) tahmin etmek için kullanılır.

**Veri seti:** https://www.kaggle.com/datasets/imakash3011/online-shoppers-purchasing-intention-dataset

## Dosya

### online_shoppers_intention.csv
Oturum seviyesinde 18 sütun (17 özellik + 1 hedef).

**Hedef:**
- `Revenue`: Boolean etiket (True = satın alma, False = satın alma yok)

**Oturum Yapısı:**
- `Administrative`: Ziyaret edilen idari sayfa sayısı
- `Administrative_Duration`: İdari sayfalarda geçirilen toplam süre (saniye)
- `Informational`: Ziyaret edilen bilgi sayfası sayısı
- `Informational_Duration`: Bilgi sayfalarında geçirilen toplam süre (saniye)
- `ProductRelated`: Ziyaret edilen ürün ilişkili sayfa sayısı
- `ProductRelated_Duration`: Ürün ilişkili sayfalarda geçirilen toplam süre (saniye)

**Etkileşim ve Değer:**
- `BounceRates`: Tek sayfa oturum oranı
- `ExitRates`: Sayfa çıkış oranı
- `PageValues`: Sayfa görüntülemesinin beklenen parasal değeri
- `SpecialDay`: Özel güne yakınlık (0–1 arası)

**Zamansal:**
- `Month`: Ziyaretin gerçekleştiği ay (örn. Feb, Mar, May, June, Jul, Aug, Sep, Oct, Nov, Dec)
- `Weekend`: Ziyaret hafta sonu mu? (True/False)

**Ziyaretçi ve Trafik:**
- `VisitorType`: Returning_Visitor, New_Visitor veya Other
- `TrafficType`: Trafik kaynak kimliği (tam sayı)
- `Region`: Bölge kimliği (tam sayı)
- `OperatingSystems`: İşletim sistemi kimliği (tam sayı)
- `Browser`: Tarayıcı kimliği (tam sayı)

## Notlar
- Her satır tek bir kullanıcı oturumunu temsil eder; kullanıcı kimliği yoktur.
- Revenue etiketi dengeli değildir (satın almayan oturum sayısı daha fazladır).
- Süreler saniye cinsinden, oranlar 0–1 aralığındadır.
- Month ve VisitorType kategoriktir; Weekend ve Revenue ham CSV’de True/False olarak tutulur.
