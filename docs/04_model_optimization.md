# 04 - Model Optimization

## Mevcut Durum
- Hyperparametre araması yapılmadı.
- Tek model: RandomForestClassifier (varsayılan ayarlar, n_estimators=200).

## Planlanan Adımlar
- Grid/Random/Optuna ile RF ve LightGBM için arama.
- Değerlendirme metrikleri: ROC-AUC, PR-AUC, F1 (pozitif sınıf öncelikli).
- Sınıf ağırlıkları: class_weight kullanarak dengesizliği adreslemek.
- Eşik optimizasyonu: İş kuralına göre karar eşiğini ROC/PR eğrisi üstünden seçmek.
- Çapraz doğrulama: Stratified K-Fold (k=5) ile daha kararlı metrik takibi.

## İzleme / Kayıt
- MLflow veya benzeri takip sistemi henüz eklenmedi; ileride deneyleri kaydetmek için önerilir.
