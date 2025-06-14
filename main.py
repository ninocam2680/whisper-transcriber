import whisper

model = whisper.load_model("base")

def transcribe(file_path):
    result = model.transcribe(file_path)
    print("📝 Trascrizione:")
    print(result["text"])

# ESEMPIO: cambiare con il tuo file locale
if __name__ == "__main__":
    transcribe("demo.mp3")
