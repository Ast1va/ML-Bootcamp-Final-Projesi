# Baseline Models

## Overview
- Basit başlangıç modelleriyle `Revenue` (satın alma) tahmini yapıldı: (1) Lojistik Regresyon + temel ölçekleme/one-hot, (2) class_weight ile iyileştirilmiş Lojistik Regresyon. Notebookta ağaç tabanlı ek bir baseline yok.
- Veri dengesiz: pozitif sınıf (`Revenue = True`) daha az.

## Data
- Satır/sütun: 12.330 satır, 18 sütun.
- Hedef dağılımı (`Revenue`): False = 10.422 (~%84,5), True = 1.908 (~%15,5) — kaynak: `01_Baseline.ipynb` (EDA hücresi).
- Train/Test: Stratified split 80/20 → Train 9.864, Test 2.466.

## Preprocessing & Feature Selection
- Hedef `Revenue` integer’a çevrildi.
- Kategorik sütunlar: `Month`, `VisitorType`, `Weekend` (3 adet).  
- Sayısal sütunlar: 14 adet (`Administrative`, `Administrative_Duration`, `Informational`, `Informational_Duration`, `ProductRelated`, `ProductRelated_Duration`, `BounceRates`, `ExitRates`, `PageValues`, `SpecialDay`, `OperatingSystems`, `Browser`, `Region`, `TrafficType`).
- One-hot sonrası 26 sütunluk özellik matrisi.
- StandardScaler ile sayısal (ve one-hot sonrası tüm) özellikler ölçeklendi. (Notebook'ta doğrudan get_dummies + scaler; ColumnTransformer ve OneHotEncoder(handle_unknown="ignore") mimarisi final pipeline'da uygulandı.)

## Baseline Model 1 – Logistic Regression
- Parametreler: `max_iter=2000`, `C=1.0`, `n_jobs=-1`, `random_state=42`, `class_weight=None` (varsayılan).
- Değerlendirme (test/validation, 20% split):

| Metric | Value |
|--------|-------|
| Accuracy | 0.8812 |
| Precision (Revenue=1) | 0.74 |
| Recall (Revenue=1) | 0.36 |
| F1 (Revenue=1) | 0.48 |
| ROC-AUC | (raporlanmadı) |

**Confusion matrix:**  
`[[2037, 47], [246, 136]]`

## Baseline Model 2 – Logistic Regression (class_weight='balanced')
- Parametreler: `max_iter=2000`, `C=1.0`, `class_weight="balanced"`, `n_jobs=-1`, `random_state=42`.
- Değerlendirme (aynı 20% split):

| Metric | Value |
|--------|-------|
| Accuracy | 0.8500 |
| ROC-AUC | 0.8963 |
| Precision (Revenue=1) | 0.51 |
| Recall (Revenue=1) | 0.75 |
| F1 (Revenue=1) | 0.61 |

**Confusion matrix:**  
`[[1810, 274], [96, 286]]`

## Key Observations
- Dengesiz veri nedeniyle pozitif sınıf (Revenue=1) için temel lojistik regresyonda recall düşük (0.36); class_weight uygulaması recall ve F1’i belirgin artırıyor.
- ROC-AUC (balanced) ~0.90 seviyesinde; metrikler iyileşse de hassasiyet/geri çağırma dengesi hâlâ ayar gerektirebilir.
- Bu sonuçlar, daha iyi performans için özellik mühendisliği (özellikle oranlar/süreler) ve model optimizasyonu (ör. LightGBM, eşik ayarı) ihtiyacını gösteriyor.
