# 🎬 Auto Subtitle Generator & Burner Pro

Bu proje, OpenAI'ın **Whisper** modelini kullanarak videolarınız için otomatik olarak yüksek doğrulukta Türkçe altyazı (.srt) oluşturur ve **FFmpeg** kullanarak bu altyazıyı videoya gömer (Hardsub).

Hem **Komut Satırı (CLI)** hem de **Modern Grafik Arayüz (GUI)** ile kullanılabilir.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Whisper](https://img.shields.io/badge/OpenAI-Whisper-green)
![FFmpeg](https://img.shields.io/badge/Tool-FFmpeg-red)
![GUI](https://img.shields.io/badge/Interface-CustomTkinter-purple)

## 🚀 Özellikler

* **Modern Arayüz (GUI):** Kullanıcı dostu, Dark Mode destekli grafik arayüz ile kolay dosya seçimi.
* **Yüksek Doğruluk:** OpenAI Whisper 'medium' modeli ile gelişmiş Türkçe transkripsiyon.
* **Otomatik Senkronizasyon:** Konuşma zamanlamalarını milisaniye hassasiyetinde algılar.
* **Hardsub Desteği:** Altyazıyı videonun üzerine kalıcı olarak yazar (Gömülü Altyazı).
* **GPU Hızlandırma:** NVIDIA ekran kartınız varsa (CUDA) işlemleri CPU'ya göre çok daha hızlı yapar.
* **Akıllı Threading:** İşlem yapılırken arayüz donmaz, logları anlık takip edebilirsiniz.

## 🛠️ Gereksinimler

Bu projeyi çalıştırmak için sisteminizde aşağıdakilerin yüklü olması gerekir:

1.  **Python 3.10 veya üzeri**
2.  **FFmpeg** (Sistem yoluna/PATH'e eklenmiş olmalıdır).
3.  **(Önerilen)** NVIDIA Ekran Kartı + CUDA Toolkit (Performans için).

## 📦 Kurulum

1.  Repoyu klonlayın:
    ```bash
    git clone https://github.com/Gunduzy12/auto-subtitle-generator.git
    cd auto-subtitle-generator
    ```

2.  Gerekli kütüphaneleri yükleyin:
    ```bash
    pip install -r requirements.txt
    ```

    *Not: Eğer `customtkinter` hatası alırsanız manuel olarak `pip install customtkinter` komutunu çalıştırın.*

## ⚙️ Kullanım

Projenin iki farklı kullanım modu vardır:

### 1. Grafik Arayüz ile Kullanım (Önerilen)
Modern arayüzü açmak için terminale şu komutu yazın:

```bash
python gui.py
```
Açılan pencereden "Video Seç" butonuna tıklayın.

Model boyutunu seçin (Varsayılan: medium en dengeli olanıdır).

"İŞLEMİ BAŞLAT" butonuna basın ve arkanıza yaslanın.

İşlem bitince video_with_subs.mp4 dosyası klasörde hazır olacaktır.

### 2. Komut Satırı ile Kullanım (CLI)
Arayüz kullanmadan, kod üzerinden ayar yaparak kullanmak isterseniz:

main.py dosyasını açıp INPUT_VIDEO kısmına video adını yazın.

Scripti çalıştırın:

Bash
```bash
python main.py
```
## 🤝 Katkıda Bulunma
Hataları bildirmek veya özellik eklemek için "Issue" açabilir veya "Pull Request" gönderebilirsiniz.

## 📄 Lisans
Bu proje MIT License altında lisanslanmıştır.
---
