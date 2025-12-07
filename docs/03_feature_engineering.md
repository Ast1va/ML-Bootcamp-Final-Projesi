# 03 - Feature Engineering

## Mevcut Durum
- Kategorik alanlar: One-hot encoding (drop_first=True).
- Sayısal alanlar: Ham değerler kullanıldı, ölçekleme yapılmadı.
- Eksik veri: Set ham geldiği için ek temizleme uygulanmadı.

## Planlanan / Eksik Çalışmalar
- Ziyaret yoğunluğu: Toplam süre / toplam sayfa sayısı, oran türevleri.
- Sezonluk sinyaller: Ay ve SpecialDay için ikili/bucket özellikler.
- Class imbalance: class_weight, SMOTE/undersampling denemeleri.
- Nadiren görülen kategorileri “Other” altında toplama.
- Öznitelik etki analizi için SHAP/feature importance raporları.

## Not
- Yeni özellik eklerken `expected_fields` ve template formu ile hizalanması gerekir (`src/app.py`, `src/templates/index.html`).
