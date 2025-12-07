# 05 - Evaluation

## Doğrulama Şeması
- Stratified train/test split (test_size=0.2, random_state=42).
- Metrikler: Accuracy, sınıf bazlı precision/recall/f1; dengesiz veri nedeniyle F1 ve ROC/PR önemlidir.

## Sonuçlar (örnek koşu)
- Accuracy: 0.899
- F1 (Revenue=True): 0.63
- F1 (Revenue=False): 0.94
- Sınıf oranı: ~%15.5 pozitif, ~%84.5 negatif.
- Confusion matrix görseli: `confusion_matrix.png` (örnek çıktı).

## Yorum
- Pozitif sınıf geri çağırma (recall) artırılmalı; class_weight veya eşik ayarıyla iyileştirilebilir.
- ROC-AUC/PR-AUC ölçülmedi; bir sonraki iterasyonda eklenmeli.
- Özellik katkıları (SHAP/importance) raporu henüz yok; model açıklanabilirliği için eklenmeli.
