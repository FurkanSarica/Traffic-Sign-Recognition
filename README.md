# 🚦 Trafik Levhası Tanıma Sistemi (Traffic Sign Recognition)

Bu proje, otonom sürüş sistemlerinde kullanılmak üzere geliştirilmiş, **Derin Öğrenme (CNN)** tabanlı bir trafik levhası sınıflandırma uygulamasıdır. **GTSRB (German Traffic Sign Recognition Benchmark)** veri seti kullanılarak eğitilen model, 43 farklı trafik levhası sınıfını yüksek doğrulukla tespit edebilmektedir.

Proje, hem teknik analiz notebook'unu hem de kullanıcı dostu **Gradio Web Arayüzünü** içermektedir.

## 🚀 Proje Özellikleri ve Başarımlar

* **Yüksek Başarım:** Test verilerinde **%97.8** genel doğruluk (Accuracy) oranı.
* **Kritik Tespit:** Trafik güvenliği için hayati olan **"DUR (Stop)"** ve **"Yol Ver"** levhalarında **%100** başarı sağlanmıştır.
* **Teknik Altyapı:** TensorFlow/Keras, OpenCV, Pandas ve Gradio.
* **Renk Düzeltmesi:** OpenCV (BGR) ve model eğitimi (RGB) arasındaki renk uzayı farkları tespit edilip optimize edilmiştir.

## 📂 Proje Dosya Yapısı

Proje içerisindeki klasör ve dosyaların görevleri şöyledir:

* **`app.py`**: Projenin web tabanlı arayüzünü (Gradio) başlatan ana uygulama dosyasıdır.
* **`Model_Test.ipynb`**: Modelin performans analizinin, grafiklerin ve detaylı testlerin yapıldığı Jupyter Notebook dosyası.
* **`models/`**: Eğitilmiş ve kullanıma hazır `.h5` model dosyasını barındırır.
* **`Proje_Raporu/`**: Projenin teknik detaylarını, literatür taramasını ve sonuçlarını içeren rapor dosyaları.
* **`training/`**: Modelin eğitimi sırasında kullanılan kodlar ve loglar.
* **`Test/`**: Modelin denenmesi için ayrılmış örnek trafik levhası görselleri.
* **`data/`**: Veri seti klasörü. *(GitHub boyut sınırı nedeniyle boştur, aşağıdan indirmelisiniz)*.
* **`requirements.txt`**: Projenin çalışması için gerekli Python kütüphanelerinin listesi.

## 📥 Veri Seti (Kurulum İçin Önemli)

GitHub dosya boyutu sınırları nedeniyle (100MB+), veri seti bu depoya doğrudan yüklenmemiştir. Projeyi tam kapsamlı çalıştırmak için:

1.  **GTSRB Veri Setini İndirin:** Veri setine [Kaggle GTSRB Sayfasından](https://www.kaggle.com/datasets/meowmeowmeowmeowmeow/gtsrb-german-traffic-sign) ulaşabilirsiniz.
2.  **Zip Dosyasını Çıkarın:** İndirdiğiniz arşivdeki dosyaları projenin ana dizinindeki **`data/`** klasörünün içine çıkartın.
3.  Dosya yapısının şu şekilde olduğundan emin olun:
    * `data/Train/`
    * `data/Test/`
    * `data/Meta/`

## 🛠 Kurulum ve Kullanım

Projeyi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin:

### 1. Projeyi Klonlayın
```bash
git clone https://github.com/FurkanSarica/Traffic-Sign-Recognition.git
cd Traffic-Sign-Recognition
```

### 2. Gerekli Kütüphaneleri Yükleyin:
```bash
pip install -r requirements.txt
```

### 3. Uygulamayı Başlatın (Arayüz):
```bash
python app.py
```
*Bu komut size tarayıcıda çalışan bir arayüz linki verecektir.*