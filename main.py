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
