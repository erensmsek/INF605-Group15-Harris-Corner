# INF605 – Grup 15: Harris Köşe Dedektörü — İlerleme Durumu

_Son güncelleme: 23 Kasım 2026_

## Proje

INF605 Görüntü İşleme Temelleri dersinin final projesi. Konu, Harris & Stephens (1988) *"A combined corner and edge detector"* makalesindeki köşe dedektörünü sıfırdan yazmak ve deneylerle incelemek.

Adımlar:
1. Görüntü türevleri $I_x$, $I_y$ (Sobel)
2. Gauss penceresiyle yapı tensörü $M$
3. Köşe cevabı $R = \det(M) - k \cdot \text{trace}(M)^2$
4. Eşikleme ve non-maximum suppression

`cv2.cornerHarris` yalnızca karşılaştırma için kullanılacak.

- Ana dosya: `harris_corner_detector.ipynb`

**Genel durum:** yaklaşık %20–25 tamamlandı (notebook'un 0–2. bölümleri).

---

## ✅ Yapılanlar

### Repo ve altyapı
- [x] Proje klasör yapısı: `data/`, `results/`, `slides/`, `report/`
- [x] `README.md`: makale referansı, takım tablosu (GitHub kullanıcı adlarıyla), kurulum ve çalıştırma talimatı
- [x] `requirements.txt` ve `.gitignore`
- [x] Sanal ortam (`.venv`)

### 0. Kurulum
- [x] Kütüphane importları, `DATA_DIR` ve `RESULTS_DIR` tanımları

### 1. Test görüntülerinin yüklenmesi
- [x] `load_gray()`: görüntüyü gri tonlu, `float64` ve [0, 1] aralığında okuyor
- [x] `show_images()`: görüntüleri yan yana gösteren yardımcı fonksiyon
- [x] Test görüntüleri:
  - `shapes.png`: grubun kendi çizdiği sentetik sahne (düz bölge, kenar, köşe ve daire)
  - `checkerboard.png`: skimage'den
  - `camera.png`: skimage'den

### 2. Görüntü gradyanları (Sobel)
- [x] Sobel çekirdekleri elle tanımlandı (`SOBEL_X`, `SOBEL_Y`)
- [x] `image_gradients()`: `cv2.filter2D` ve yansıtmalı sınır kullanıyor
- [x] Doğrulama testleri:
  - [x] Rampa görüntüsünde $I_x = 8s$ ve $I_y = 0$
  - [x] Sabit görüntüde iki türev de 0
  - [x] `filter2D` sonucu NumPy slicing ile elle yazılan Sobel'le aynı
- [x] `plot_gradients()`: $I_x$, $I_y$ ve gradyan büyüklüğü
- [x] $I_x^2$, $I_y^2$, $I_xI_y$ görselleştirmesi
- [x] 10. hafta ilerleme raporu figürü: `results/week10_gradients_shapes.png`

---

## ⏳ Yapılacaklar

### Notebook bölümleri (başlıkları var, içleri boş)
- [ ] **3. Yapı tensörü:** $I_x^2$, $I_y^2$ ve $I_xI_y$'yi Gauss penceresiyle (σ) toplamak
- [ ] **4. Köşe cevabı R:** $\det(M) - k\cdot\text{trace}(M)^2$; R>0 köşe, R<0 kenar, R≈0 düz bölge olarak yorumlamak
- [ ] **5. Eşikleme ve non-maximum suppression:** köşe noktalarını seçip görüntü üzerinde çizmek
- [ ] **6. Makaleden bir sonucu tekrar üretmek**
- [ ] **7. Kendi görüntülerimizle deneyler:** k, σ ve eşik değerinin etkisi
- [ ] **8. İki görüntü arasında köşe eşleştirme**
- [ ] **9. Tekrarlanabilirlik:** döndürme ve parlaklık değişimi altında
- [ ] **10. `cv2.cornerHarris` ile karşılaştırma**
- [ ] **11. Sonuç**

### Veri
- [ ] Kendi fotoğraf çiftlerimiz: aynı sahnenin iki farklı açıdan çekimi (7. ve 8. bölüm için)

### Teslim edilecekler
- [ ] Sunum (PDF): `slides/`
- [ ] Final raporu (PDF): `report/`, yapay zekâ kullanım beyanı dahil
- [ ] Sonuç figürlerinin `results/` klasörüne kaydedilmesi
- [ ] Notebook'un baştan sona sorunsuz çalıştığının kontrolü

---

## Sıradaki adım

3., 4. ve 5. bölümler, yani Harris dedektörünün çekirdeği. Ardından kendi fotoğraflarımızın çekilmesi.
