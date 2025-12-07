# 01 - Data Overview

## Problem ve Veri Tanımı
- Amaç: Ziyaretçinin Revenue (satın alma) yapıp yapmayacağını tahmin etmek.
- Veri seti: Online Shoppers Intention; 12.330 satır, 17 özellik + hedef.
- Hedef dağılımı: `Revenue=True` ~%15.5, `Revenue=False` ~%84.5 (dengesiz).

## Alanlar (özet)
- Sayısal: Administrative, Administrative_Duration, Informational, Informational_Duration, ProductRelated, ProductRelated_Duration, BounceRates, ExitRates, PageValues, SpecialDay, OperatingSystems, Browser, Region, TrafficType.
- Kategorik: Month (örn. Feb, Mar, Nov), VisitorType, Weekend (bool).

## Temel Bulgular (hızlı EDA)
- Dengesiz sınıf → değerlendirme için F1/ROC-AUC ve eşik optimizasyonu önemli.
- ProductRelated ve PageValues metrikleri satın alma ile en çok ilişki beklenen alanlar.
- Month ve SpecialDay sezonluk etkileri incelemek için aday.

## Önerilen İyileştirmeler
- Kategorik alanların hedefe göre dağılımını inceleyip nadir kategorileri birleştirmek.
- Ziyaret süresi/yoğunluğu türevleri: oturum toplam süreleri, oranlar.
- Class imbalance için ağırlıklandırma veya SMOTE/undersampling denemeleri.
