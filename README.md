# 🎬 Auto Subtitle Generator & Burner

Bu proje, OpenAI'ın **Whisper** modelini kullanarak videolarınız için otomatik olarak yüksek doğrulukta Türkçe altyazı (.srt) oluşturur ve **FFmpeg** kullanarak bu altyazıyı videoya gömer (Hardsub).

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Whisper](https://img.shields.io/badge/OpenAI-Whisper-green)
![FFmpeg](https://img.shields.io/badge/Tool-FFmpeg-red)

## 🚀 Özellikler

* **Yüksek Doğruluk:** OpenAI Whisper 'medium' modeli ile gelişmiş Türkçe transkripsiyon.
* **Otomatik Senkronizasyon:** Konuşma zamanlamalarını milisaniye hassasiyetinde algılar.
* **Hardsub Desteği:** Altyazıyı videonun üzerine kalıcı olarak yazar, böylece her oynatıcıda görünür.
* **GPU Hızlandırma:** NVIDIA ekran kartınız varsa (CUDA) işlemleri CPU'ya göre 10 kat daha hızlı yapar.
* **Akıllı Bağlam:** Videonun içeriğine dair (prompt) desteği ile teknik terim hatalarını azaltır.

## 🛠️ Gereksinimler

Bu aracı kullanabilmek için bilgisayarınızda şunlar yüklü olmalıdır:

1.  **Python 3.8+**
2.  **FFmpeg** (Sistem yoluna/PATH'e eklenmiş olmalıdır).
3.  **(Önerilen)** NVIDIA GPU + CUDA Toolkit (İşlem hızı için kritiktir).

## 📦 Kurulum

1.  Repoyu klonlayın:
    ```bash
    git clone [https://github.com/Gunduzy12/auto-subtitle-generator.git](https://github.com/Gunduzy12/auto-subtitle-generator.git)
    cd auto-subtitle-generator
    ```

2.  Gerekli kütüphaneleri yükleyin:
    ```bash
    pip install -r requirements.txt
    ```

    *Not: PyTorch'u GPU (CUDA) desteğiyle kurmak için [resmi sitesindeki](https://pytorch.org/get-started/locally/) komutu kullanmanız gerekebilir.*

## ⚙️ Kullanım

1.  Altyazı eklemek istediğiniz videoyu proje klasörüne atın.
2.  `main.py` dosyasını açın ve video adını güncelleyin:

    ```python
    # main.py dosyasının içi:
    INPUT_VIDEO = "videonuz.mp4" 
    MODEL_SIZE = "medium"
    ```

3.  Aracı çalıştırın:
    ```bash
    python main.py
    ```

4.  İşlem bittiğinde `video_with_subs.mp4` dosyası hazır olacaktır.

## 🤝 Katkıda Bulunma

Hataları bildirmek veya geliştirme önerileri için "Issue" açabilir veya "Pull Request" gönderebilirsiniz.

## 📄 Lisans

Bu proje MIT lisansı altındadır.