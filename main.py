import whisper
import datetime
import os
import torch
import sys


# İşlenecek video dosyasının adı
INPUT_VIDEO = "video.mp4"

# Çıktı dosya isimleri
OUTPUT_SRT = "subtitle.srt"
OUTPUT_VIDEO = "video_with_subs.mp4"

# Whisper Model Boyutu: tiny, base, small, medium, large
# 'medium' veya 'large' daha iyi sonuç verir ancak daha fazla VRAM gerektirir.
MODEL_SIZE = "medium" 


# Videonun içeriği hakkında kısa bir bilgi verirseniz doğruluk artar.
INITIAL_PROMPT = "Bu video genel konuşmalar, diyaloglar ve teknik terimler içermektedir."

def format_timestamp(seconds):
    """Saniye cinsinden süreyi SRT formatına (HH:MM:SS,ms) dönüştürür."""
    td = datetime.timedelta(seconds=seconds)
    return f"{td.seconds // 3600:02}:{(td.seconds % 3600) // 60:02}:{td.seconds % 60:02},{int((seconds % 1) * 1000):03}"

def check_ffmpeg():
    """Sistemde FFmpeg'in yüklü olup olmadığını kontrol eder."""
    if os.system("ffmpeg -version") != 0:
        print("HATA: FFmpeg sisteminizde yüklü değil veya yol (path) ayarları yapılmamış.")
        print("Lütfen https://ffmpeg.org/ adresinden yükleyin.")
        sys.exit(1)

def main():
    print("=" * 60)
    print("OTOMATİK ALTYAZI OLUŞTURUCU VE GÖMÜCÜ")
    print("=" * 60)

    # 1. Dosya Kontrolü
    if not os.path.exists(INPUT_VIDEO):
        print(f"HATA: Giriş dosyası '{INPUT_VIDEO}' bulunamadı.")
        return

    check_ffmpeg()

    # 2. Donanım Kontrolü (GPU/CPU)
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"Bilgi: İşlem '{device.upper()}' üzerinde gerçekleştirilecek.")


    if os.path.exists(OUTPUT_SRT):
        os.remove(OUTPUT_SRT)

    
    print(f"\n1. Whisper modeli yükleniyor ({MODEL_SIZE})...")
    try:
        model = whisper.load_model(MODEL_SIZE, device=device)
    except Exception as e:
        print(f"Model yüklenirken hata oluştu: {e}")
        return

    print(f"2. Video işleniyor: {INPUT_VIDEO}")
    print("   (Bu işlem videonun uzunluğuna ve donanım hızına göre zaman alabilir...)")

    try:
        result = model.transcribe(
            INPUT_VIDEO, 
            fp16=False, 
            language="tr",       
            beam_size=5,        
            best_of=5, 
            temperature=0, 
            initial_prompt=INITIAL_PROMPT,
            condition_on_previous_text=False
        )
    except Exception as e:
        print(f"Transkripsiyon hatası: {e}")
        return
    
    
    print("\n3. SRT altyazı dosyası oluşturuluyor...")
    with open(OUTPUT_SRT, "w", encoding="utf-8") as srt_file:
        for index, segment in enumerate(result['segments']):
            start = format_timestamp(segment['start'])
            end = format_timestamp(segment['end'])
            text = segment['text'].strip()
            
            if len(text) < 2: continue
            
            srt_file.write(f"{index + 1}\n{start} --> {end}\n{text}\n\n")
            
    print(f"   Altyazı kaydedildi: {OUTPUT_SRT}")

    # 5. FFmpeg ile Altyazıyı Videoya Göm
    print("-" * 60)
    print("4. FFmpeg ile altyazı videoya gömülüyor...")
    
    # FFmpeg komutu: Font boyutu, rengi ve kenarlık ayarları burada yapılabilir
    ffmpeg_cmd = (
        f'ffmpeg -y -v warning -i "{INPUT_VIDEO}" -vf "subtitles={OUTPUT_SRT}:force_style=\'Fontsize=22,PrimaryColour=&H00FFFFFF,BorderStyle=1,Outline=1,Shadow=0\'" '
        f'-c:v libx264 -preset fast -crf 23 -c:a copy "{OUTPUT_VIDEO}"'
    )
    
    ret_code = os.system(ffmpeg_cmd)

    print("=" * 60)
    if ret_code == 0:
        print(f"BAŞARILI! Videonuz hazır: {OUTPUT_VIDEO}")
    else:
        print("HATA: Video oluşturulurken bir sorun çıktı.")

if __name__ == "__main__":
    main()
