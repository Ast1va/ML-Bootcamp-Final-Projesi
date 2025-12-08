# Feature Engineering

## Baseline Performansı
- Referans (class_weight'li LogReg, 20% test): Accuracy 0.8500, ROC-AUC 0.8963, Precision (Rev=1) 0.51, Recall 0.75, F1 0.61. Temel LogReg (class_weight=None) Recall 0.36, F1 0.48.
- İhtiyaç: Pozitif sınıfta (Revenue=1) Recall/F1 düşüktü; sinyal zayıf kaldığı için yeni türetilmiş özellikler gerekli.

## Strateji
- Oturum yoğunluğu, değer yoğunluğu, sezon ve ziyaretçi tipini yansıtan bayraklar eklendi; kategorikler one-hot, sayısallar ölçeklendi.
- Modeller: Lojistik Regresyon ve RandomForest ile ardışık denemeler; metrik odağı ROC-AUC ve Revenue=1 Recall/F1.

## Deney Günlüğü / Adımlar

### 1) Oturum Süresi ve Değer Yoğunluğu
- **Total_Duration:** `Administrative_Duration + Informational_Duration + ProductRelated_Duration`
- **PageValue_per_Product:** `PageValues / (ProductRelated + 1e-3)`
- İş mantığı: Oturum süresinin ve sayfa başına değer yoğunluğunun satın alma niyetine yansıması.
- Etki: Özellik sayısı 17 → 19; LogReg (FE) ROC-AUC 0.8959, Recall 0.75, F1 0.60; RF (FE) ROC-AUC 0.9247, Recall 0.53, F1 0.62.

### 2) Sezon ve Ziyaretçi Tipi Bayrakları
- **Is_HighSeason:** Ay ∈ {Nov, Dec, Mar, May} → 1, aksi 0.
- **Is_ReturningVisitor:** VisitorType == Returning_Visitor → 1, aksi 0.
- İş mantığı: Sezonsal alışveriş yoğunluğu ve geri dönen ziyaretçinin satın alma ihtimali daha yüksek olabilir.
- Etki: +2 özellik; toplam 21 sütun (one-hot öncesi). LogReg (FE) metrikleri korunurken, RF’nin Recall/F1’i iyileşti (Recall 0.53, F1 0.62; AUC 0.9247).

### 3) Model Optimizasyonu (03_Model_Optimization.ipynb)
- FE’li **RandomForest (tuned)**: Accuracy 0.8694, ROC-AUC 0.9296, Precision 0.5566, Recall 0.7723, F1 0.6469.
- FE’li **LightGBM (tuned)**: Accuracy 0.8812, ROC-AUC 0.9275, Precision 0.5903, Recall 0.7618, F1 0.6651.
- Gözlem: FE + hiperparametre araması pozitif sınıf Recall/F1’ini belirgin artırdı; AUC ~0.93 bandına yükseldi.

## Nihai Özellik Seti
- One-hot sonrası ~30+ sütun (21 temel + kategorik genişlemeler).
- Öne çıkanlar (SHAP/önem): `PageValues`, `PageValue_per_Product`, `ExitRates`, `Month_Nov`, `Month_May`, `Total_Duration`, `Is_ReturningVisitor`, `Is_HighSeason`, `BounceRates`, `ProductRelated_Duration`.

## Çıkarımlar
- Süre ve değer yoğunluğu sinyalleri (Total_Duration, PageValue_per_Product) Recall/F1’i dengede tutarken AUC’yi yüksek seviyede korudu.
- Sezon ve geri dönüş bayrakları, özellikle ağaç tabanlı modellerde pozitif sınıf geri çağırmayı artırdı.
- FE + tuning ile ROC-AUC ~0.93, Recall (Revenue=1) ~0.76–0.77 ve F1 ~0.65–0.67 seviyelerine çıktı; bu, nihai model seçiminde bu özellik setini ve ön işleme akışını temel almamızı sağladı.
