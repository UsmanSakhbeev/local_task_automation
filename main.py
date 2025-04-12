from command_processor import process_command
from voice_input import record_audio, recognize_speech

def main():
    print("Автоматизатор локальных задач.")
    print("Скажи что-нибудь или напиши вручную (введи 'голос' или 'текст'). Для выхода введи 'выход'.")

    while True:
        mode = input("Режим (голос/текст/выход): ").strip().lower()

        if mode == "выход":
            print("До свидания!")
            break

        if mode == "текст":
            command = input("Введите команду: ")
        elif mode == "голос":
            record_audio()
            command = recognize_speech()
            print(f"📝 Распознано: {command}")
        else:
            print("Непонятный режим.")
            continue

        result = process_command(command)
        print(result)

if __name__ == "__main__":
    main()
