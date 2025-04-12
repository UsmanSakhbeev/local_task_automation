import subprocess

def run():
    try:
        # Попробуем открыть VS Code, если установлен
        subprocess.Popen(["code"])
    except FileNotFoundError:
        try:
            # Если нет VS Code — откроем стандартный редактор gedit
            subprocess.Popen(["gedit"])
        except FileNotFoundError:
            print("❌ Ни VS Code, ни Gedit не найдены. Установи один из них.")
