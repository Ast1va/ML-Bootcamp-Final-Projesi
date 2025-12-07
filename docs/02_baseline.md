# 02 - Baseline

## Yaklaşım
- Ön işleme: Kategorik alanlar için one-hot encoding (`pd.get_dummies`, drop_first=True).
- Model: RandomForestClassifier (n_estimators=200, max_depth=None, random_state=42, n_jobs=-1).
- Ayrım: Stratified train/test split (test_size=0.2).

## Sonuçlar (örnek koşu)
- Accuracy: 0.899
- Pozitif sınıf (Revenue=True) f1: 0.63
- Negatif sınıf f1: 0.94
- Sınıf dengesizliği: pozitif ~%15.5 → eşik optimizasyonu gerekli.

## Notlar
- Şu anda baseline ve “final” aynı modeldir.
- Ağaç tabanlı basit model; LightGBM/LogReg ile karşılaştırma yapılmadı (yapılmalı).
