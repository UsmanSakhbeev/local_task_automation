import json
import os

from actions import launch_editor, open_browser

# Загружаем intents.json по относительному пути от текущего файла
intents_path = os.path.join(os.path.dirname(__file__), "intents.json")
with open(intents_path, encoding="utf-8") as f:
    intents = json.load(f)

print("Загруженные intents:", intents)

def process_command(command: str) -> str:
    command = command.lower()
    print("Пользовательская команда:", command)
    for key_phrase, action in intents.items():
        if key_phrase in command:
            if action == "open_browser":
                open_browser.run()
            elif action == "launch_editor":
                launch_editor.run()
            return f"Выполняю: {action}"
    return "Команда не распознана"
