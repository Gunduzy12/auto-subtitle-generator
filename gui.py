import customtkinter
from tkinter import filedialog
import threading
import whisper
import os
import datetime
import torch


customtkinter.set_appearance_mode("Dark")  
customtkinter.set_default_color_theme("blue")  

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        
        self.title("Auto Subtitle Generator Pro")
        self.geometry("600x500")
        self.resizable(False, False)

        
        self.label_title = customtkinter.CTkLabel(self, text="Kolay Altyazı Oluşturucu", font=("Roboto", 24, "bold"))
        self.label_title.pack(pady=20)

        
        self.frame_file = customtkinter.CTkFrame(self)
        self.frame_file.pack(pady=10, padx=20, fill="x")

        self.btn_select = customtkinter.CTkButton(self.frame_file, text="Video Seç", command=self.select_file)
        self.btn_select.pack(side="left", padx=10, pady=10)

        self.label_file = customtkinter.CTkLabel(self.frame_file, text="Dosya seçilmedi...", text_color="gray")
        self.label_file.pack(side="left", padx=10)

        
        self.label_model = customtkinter.CTkLabel(self, text="Model Boyutu Seçin:")
        self.label_model.pack(pady=(10, 0))

        self.option_model = customtkinter.CTkOptionMenu(self, values=["base", "small", "medium", "large"])
        self.option_model.set("medium")  
        self.option_model.pack(pady=5)

      
        self.btn_start = customtkinter.CTkButton(self, text="İŞLEMİ BAŞLAT", command=self.start_thread, height=40, font=("Roboto", 16, "bold"), fg_color="green", hover_color="darkgreen")
        self.btn_start.pack(pady=20)

        
        self.textbox_log = customtkinter.CTkTextbox(self, height=150)
        self.textbox_log.pack(pady=10, padx=20, fill="x")
        self.textbox_log.insert("0.0", "Sistem hazır. Lütfen bir video seçin...\n")

       
        self.selected_file = None

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video Files", "*.mp4 *.mkv *.avi *.mov")])
        if file_path:
            self.selected_file = file_path
            self.label_file.configure(text=os.path.basename(file_path), text_color="white")
            self.log(f"Dosya seçildi: {file_path}")

    def log(self, message):
        """Arayüzdeki kutuya yazı yazar"""
        self.textbox_log.insert("end", f"> {message}\n")
        self.textbox_log.see("end")

    def start_thread(self):
        """Arayüz donmasın diye işlemi ayrı kanalda (thread) başlatır"""
        if not self.selected_file:
            self.log("HATA: Önce bir video seçmelisiniz!")
            return
        
        
        self.btn_start.configure(state="disabled", text="İşleniyor...")
        
       
        threading.Thread(target=self.process_video).start()

    def process_video(self):
        try:
            input_video = self.selected_file
            model_size = self.option_model.get()
            output_srt = "subtitle.srt"
            output_video = "video_with_subs.mp4"

           
            device = "cuda" if torch.cuda.is_available() else "cpu"
            self.log(f"İşlem birimi: {device.upper()} (Model: {model_size})")

            self.log("Model yükleniyor, lütfen bekleyin...")
            model = whisper.load_model(model_size, device=device)
            
            self.log("Transkripsiyon başladı (Bu işlem videonun uzunluğuna göre sürer)...")
            result = model.transcribe(input_video, language="tr", fp16=False)

          
            self.log("SRT dosyası oluşturuluyor...")
            with open(output_srt, "w", encoding="utf-8") as srt_file:
                for i, segment in enumerate(result['segments']):
                    start = self.format_time(segment['start'])
                    end = self.format_time(segment['end'])
                    text = segment['text'].strip()
                    srt_file.write(f"{i+1}\n{start} --> {end}\n{text}\n\n")

            
            self.log("FFmpeg ile altyazı videoya gömülüyor...")
            command = (
                f'ffmpeg -y -v warning -i "{input_video}" '
                f'-vf "subtitles={output_srt}:force_style=\'Fontsize=22,PrimaryColour=&H00FFFFFF,BorderStyle=1\'" '
                f'-c:v libx264 -preset fast -crf 23 -c:a copy "{output_video}"'
            )
            os.system(command)

            self.log("✅ İŞLEM BAŞARIYLA TAMAMLANDI!")
            self.log(f"Video hazır: {output_video}")

        except Exception as e:
            self.log(f"❌ HATA OLUŞTU: {str(e)}")
        finally:
            
            self.btn_start.configure(state="normal", text="İŞLEMİ BAŞLAT")

    def format_time(self, seconds):
        td = datetime.timedelta(seconds=seconds)
        return f"{td.seconds // 3600:02}:{(td.seconds % 3600) // 60:02}:{td.seconds % 60:02},{int((seconds % 1) * 1000):03}"

if __name__ == "__main__":
    app = App()
    app.mainloop()