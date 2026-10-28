import shutil
from datetime import datetime
from pathlib import Path

import functions


def add_todo(todos, text):
    """Додає тексті і зберігає список; повертає None"""
    if not text:
        raise ValueError("Порожній текст")
    todos.append(text)
    functions.write_todos(todos)


def edit_todo(todos, number, new_text):
    """Замінює справу за номером від 1; повертає None."""
    if number < 1 or number > len(todos):
        raise IndexError
    if not new_text:
        raise ValueError("Порожній текст")
    todos[number - 1] = new_text
    functions.write_todos(todos)


def complete_todo(todos, number):
    """Видаляє справу, зберігає список і повертає видалений текст."""
    if number < 1 or number > len(todos):
        raise IndexError
    completed_todo = todos.pop(number - 1)
    functions.write_todos(todos)
    return completed_todo


def count_todos(todos):
    """Повертає кількість справ, не змінюючи список."""
    return len(todos)


def clear_todos(todos):
    """Очищує переданий список і файл; повертає None."""
    todos.clear()
    functions.write_todos(todos)


def backup_todos(filepath=functions.FILEPATH):
    """Копіює файл справ і повертає шлях резервної копії.
    :param filepath: необов'язковий шлях до вихідного файла
    :return: об'єкт Path створеної копії
    """
    source = Path(filepath)
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S-%f")
    backup = source.with_name(f"{source.stem}-backup-{timestamp}{source.suffix}")
    shutil.copy2(source, backup)
    return backup
