# 🚦 Trafik Levhası Tanıma Sistemi (Traffic Sign Recognition)

Bu proje, otonom sürüş sistemlerinde kullanılmak üzere geliştirilmiş, **Derin Öğrenme (CNN)** tabanlı bir trafik levhası sınıflandırma uygulamasıdır. **GTSRB (German Traffic Sign Recognition Benchmark)** veri seti kullanılarak eğitilen model, 43 farklı trafik levhası sınıfını yüksek doğrulukla tespit edebilmektedir.

## 🚀 Proje Özellikleri

* **Yüksek Başarım:** Test verilerinde **%97.8** genel doğruluk oranı.
* **Kritik Tespit:** Özellikle "DUR (Stop)" ve "Yol Ver" gibi güvenlik açısından kritik levhalarda **%100** başarı.
* **Teknik Altyapı:** Görüntü işleme için OpenCV, model eğitimi için TensorFlow/Keras kullanılmıştır.
* **Renk Düzeltmesi:** Eğitim (RGB) ve test (BGR) aşamaları arasındaki renk uzayı farkları optimize edilmiştir.

## 📂 Proje Yapısı

Proje dosyalarının ve klasörlerin görevleri aşağıdadır:

* **`main.py`**: Modelin test edildiği ana çalışma dosyasıdır.
* **`Model_Test.ipynb`**: Adım adım analiz, görselleştirme ve detaylı testlerin yapıldığı Jupyter Notebook dosyası.
* **`training/`**: Modelin eğitilmesi için kullanılan kodları ve eğitim süreç loglarını içerir.
* **`models/`**: Eğitilmiş ve kaydedilmiş `.h5` model dosyalarını barındırır.
* **`data/`**: GTSRB veri seti (Eğitim ve Test resimleri) burada bulunur. *(Not: Dosya boyutu nedeniyle GitHub'a yüklenmemiştir)*.
* **`requirements.txt`**: Projenin çalışması için gerekli kütüphane listesi.

## 🛠 Kurulum ve Kullanım

Projeyi bilgisayarınıza indirip çalıştırmak için:

1.  **Projeyi Klonlayın:**
    ```bash
    git clone [https://github.com/FurkanSarica/Traffic-Sign-Recognition.git](https://github.com/FurkanSarica/Traffic-Sign-Recognition.git)
    cd Traffic-Sign-Recognition
    ```

2.  **Gerekli Kütüphaneleri Yükleyin:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Projeyi Çalıştırın:**
    ```bash
    python main.py
    ```

## 👨‍💻 Geliştirici

**Furkan Sarıca**
* GitHub: [github.com/FurkanSarica](https://github.com/FurkanSarica)