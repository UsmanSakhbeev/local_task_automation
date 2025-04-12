import subprocess

def run():
    try:
        # xdg-open откроет браузер по умолчанию
        subprocess.Popen(["xdg-open", "https://www.google.com"])
    except FileNotFoundError:
        print("❌ Не удалось открыть браузер. Убедись, что xdg-open установлен.")
