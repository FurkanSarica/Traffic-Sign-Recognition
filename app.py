import os
import tensorflow as tf
from tensorflow.keras.models import load_model
import gradio as gr
import numpy as np
from PIL import Image



MODEL_DOSYA_ADI = os.path.join("models", "traffic_classifier_v2.h5") 

# Örnek Resimlerin Listesi

ornek_resimler_listesi = [
    [os.path.join("Test", "00074.png")],
    [os.path.join("Test", "00915.png")],
    [os.path.join("Test", "01570.png")],
    [os.path.join("Test", "00179.png")],
    [os.path.join("Test", "02010.png")],
    [os.path.join("Test", "12460.png")],
    [os.path.join("Test", "08154.png")],
    [os.path.join("Test", "04554.png")],
    [os.path.join("Test", "03480.png")],
    [os.path.join("Test", "07618.png")]
]

# Sınıf İsimleri 
classes = { 
    0:'Hız Limiti (20km/s)',
    1:'Hız Limiti (30km/s)',
    2:'Hız Limiti (50km/s)', 
    3:'Hız Limiti (60km/s)',
    4:'Hız Limiti (70km/s)',
    5:'Hız Limiti (80km/s)',
    6:'Hız Limiti Bitişi (80km/s)',
    7:'Hız Limiti (100km/s)',
    8:'Hız Limiti (120km/s)',
    9:'Sollama Yasak',
    10:'Kamyonlar için Sollama Yasak',
    11:'Ana Yol Tali Yol Kavşağı',
    12:'Ana Yol',
    13:'Yol Ver',
    14:'DUR (Stop)',
    15:'Taşıt Giremez',
    16:'Kamyon Giremez',
    17:'Girişi Olmayan Yol',
    18:'Dikkat', 
    19:'Sola Tehlikeli Viraj',
    20:'Sağa Tehlikeli Viraj',
    21:'Virajlı Yol',
    22:'Engebeli Yol',
    23:'Kaygan Yol',
    24:'Yol Daralması (Sağdan)',
    25:'Yol Çalışması',
    26:'Trafik Işıkları',
    27:'Yaya Geçidi',
    28:'Okul Geçidi',
    29:'Bisiklet Geçidi',
    30:'Buzlanma Tehlikesi',
    31:'Vahşi Hayvan Çıkabilir', 
    32:'Hız Sınırı ve Yasakların Sonu',
    33:'Sağa Mecburi Yön',
    34:'Sola Mecburi Yön', 
    35:'İleri Mecburi Yön',
    36:'İleri ve Sağa Mecburi Yön',
    37:'İleri ve Sola Mecburi Yön',   
    38:'Sağdan Gidiniz',
    39:'Soldan Gidiniz',
    40:'Dönel Kavşak', 
    41:'Sollama Yasağı Sonu',
    42:'Kamyonlar İçin Sollama Yasağı Sonu'
}


# MODEL YÜKLEME

print("Model yükleniyor...")
model = None
input_shape = (30, 30) 

try:
    if not os.path.exists(MODEL_DOSYA_ADI):
        print(f"HATA: '{MODEL_DOSYA_ADI}' bulunamadı! Lütfen dosya yolunu kontrol edin.")
    else:
        model = load_model(MODEL_DOSYA_ADI)
        input_shape = model.input_shape[1:3]
        print(f"✅ Model başarıyla yüklendi. Beklenen input boyutu: {input_shape}")
except Exception as e:
    print(f"BİR HATA OLUŞTU: {e}")


# TAHMİN FONKSİYONU

def trafik_tahmin(image):
    
    if model is None:
        return {"HATA": "Model yüklenemedi"}
    if image is None:
        return None
    
    # Resmi modele hazırlama
    image = image.resize(input_shape)
    img_array = np.array(image) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    
    # Tahmin etme
    prediction = model.predict(img_array)[0]
    
    # Sonuçları düzenleme
    results = {}
    top_indices = prediction.argsort()[-3:][::-1]
    
    for i in top_indices:
        label = classes.get(i, f"Sınıf {i}")
        score = float(prediction[i])
        results[label] = score
        
    return results


# ARAYÜZ (GRADIO)

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("# 🚦 Trafik Levhası Tanıma Sistemi")
    gr.Markdown("Aşağıdaki **örnek resimlere tıklayarak** hızlıca test edebilir veya kendi resminizi yükleyebilirsiniz.")
    
    with gr.Row():
        with gr.Column():
            img_input = gr.Image(type="pil", label="Resim Yükle")
            btn_predict = gr.Button("Analiz Et", variant="primary")
        
        with gr.Column():
            lbl_output = gr.Label(num_top_classes=3, label="Tahmin Sonuçları")
    
    # Örnek Resimler Bölümü
    examples = gr.Examples(
        examples=ornek_resimler_listesi, 
        inputs=img_input,               
        outputs=lbl_output,             
        fn=trafik_tahmin,               
        cache_examples=False, 
        label="Test Etmek İçin Örnek Levhalara Tıklayın"
    )
    
    btn_predict.click(trafik_tahmin, inputs=img_input, outputs=lbl_output)


    # UYGULAMAYI BAŞLAT
if __name__ == "__main__":
    demo.launch()