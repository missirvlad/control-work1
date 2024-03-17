import json
import os
import datetime


# Функция для чтения заметок из файла
def load_notes():
    if os.path.exists("notes.json"):
        with open("notes.json", "r") as file:
            return json.load(file)
    else:
        return []


# Функция для сохранения заметок в файл
def save_notes(notes):
    with open("notes.json", "w") as file:
        json.dump(notes, file, indent=4)


# Функция для фильтрации заметок по дате
def filter_notes_by_date(notes, date):
    return [note for note in notes if note["date"] == date]


# Консольное приложение заметок
def main():
    notes = load_notes()
    print("Добро пожаловать в приложение заметки.")

    while True:
        command = input("Введите команду (Создать/Прочитать/Редактировать/Удалить/Фильтровать(по дате)/Выход): ")

        if command == "Создать":
            title = input("Введите заголовок заметки: ")
            body = input("Введите тело заметки: ")
            note = {"id": len(notes) + 1, "title": title, "body": body, "date": str(datetime.datetime.now())}
            notes.append(note)
            save_notes(notes)
            print("Заметка успешно сохранена.")

        elif command == "Прочитать":
            print("ID | Заголовок | Тело | Дата и время создания")
            for note in notes:
                print(f'{note["id"]} | {note["title"]} | {note["body"]} | {note["date"]}')

        elif command == "Редактировать":
            note_id = int(input("Введите ID заметки для редактирования: "))
            for note in notes:
                if note["id"] == note_id:
                    note["title"] = input("Введите новый заголовок заметки: ")
                    note["body"] = input("Введите новое тело заметки: ")
                    note["date"] = str(datetime.datetime.now())
                    save_notes(notes)
                    print("Заметка успешно отредактирована.")
                    break

        elif command == "Удалить":
            note_id = int(input("Введите ID заметки для удаления: "))
            notes = [note for note in notes if note["id"] != note_id]
            save_notes(notes)
            print("Заметка успешно удалена.")

        elif command == "Фильтровать":
            date = input("Введите дату для фильтрации (гггг-мм-дд): ")
            filtered_notes = filter_notes_by_date(notes, date)
            print("ID | Заголовок | Тело | Дата и время создания")
            for note in filtered_notes:
                print(f'{note["id"]} | {note["title"]} | {note["body"]} | {note["date"]}')

        elif command == "Выход":
            break

        else:
            print("Некорректная команда. Попробуйте снова.")


if __name__ == "__main__":
    main()


