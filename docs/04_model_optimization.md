# Model Optimizasyonu

## Genel Bakış
- Temel özellik seti: FE adımlarından sonra oluşan 21 sütun (4 türetilmiş + özgün 17); one-hot sonrası ~30+ sütun.
- Optimizasyon: RandomizedSearchCV ile RandomForest ve LightGBM için sınırlı arama; odak metrik ROC-AUC ve Revenue=1 Recall/F1.
- Validasyon: Stratified 80/20 train/test, arama sırasında 3-fold CV.

## Pipeline
1. FE özelliklerini yükle (`Total_Duration`, `PageValue_per_Product`, `Is_HighSeason`, `Is_ReturningVisitor` dahil).
2. Ön işleme: ColumnTransformer ile sayısallara StandardScaler, kategoriklere OneHotEncoder(handle_unknown="ignore").
3. Model ve arama:  
   - RandomForest: 20 aday, CV=3 (03_Model_Optimization.ipynb)  
   - LightGBM: 12 aday, CV=3

## Sonuçlar

### Karşılaştırma (20% test split)
| Model | Accuracy | ROC-AUC | Precision (Rev=1) | Recall (Rev=1) | F1 (Rev=1) |
|-------|----------|---------|-------------------|----------------|------------|
| LogReg (baseline, class_weight=balanced) | 0.8500 | 0.8963 | 0.51 | 0.75 | 0.61 |
| RF (FE, untuned) | 0.8966 | 0.9247 | 0.73 | 0.53 | 0.62 |
| **RF (tuned)** | 0.8694 | 0.9296 | 0.5566 | 0.7723 | 0.6469 |
| **LightGBM (tuned)** | 0.8812 | 0.9275 | 0.5903 | 0.7618 | 0.6651 |

### En İyi Hiperparametreler

**RandomForest (tuned)**  
```
n_estimators: 400
max_depth: 10
max_features: sqrt
min_samples_split: 5
min_samples_leaf: 8
random_state: 42
```

**LightGBM (tuned)**  
```
n_estimators: 250
learning_rate: 0.03
num_leaves: 63
max_depth: -1
subsample: 1.0
colsample_bytree: 0.7
random_state: 42
```

## Gözlemler
- FE + tuning ile ROC-AUC ~0.93 bandına çıktı; pozitif sınıf Recall/F1 (0.76–0.77 / 0.65–0.67) baseline’a göre belirgin arttı.
- Tuned RF, F1/Recall’da iyileşirken Accuracy biraz düştü; LightGBM dengeli bir noktada kaldı ve genel olarak en tutarlı sonuçları verdi.
- Final model seçimi için LightGBM (tuned) veya RF (tuned) tercih edilebilir; her ikisi de FE setine dayanıyor ve class imbalance’i makul yönetiyor.
