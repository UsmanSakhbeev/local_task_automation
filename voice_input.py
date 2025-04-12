import sounddevice as sd
from scipy.io.wavfile import write
import whisper

SAMPLE_RATE = 16000

def record_audio(filename="recording.wav", duration=5):
    print("🎙️ Говорите...")
    recording = sd.rec(int(duration * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype='int16')
    sd.wait()
    write(filename, SAMPLE_RATE, recording)
    print("✅ Запись завершена.")

def recognize_speech(filename="recording.wav") -> str:
    print("🧠 Распознавание...")
    model = whisper.load_model("base")  # Можно попробовать 'small', 'medium' или 'large'
    result = model.transcribe(filename, language="ru")
    return result["text"]
