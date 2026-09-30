FILEPATH = "data/todos.txt"


def get_todos(filepath=FILEPATH):
    """Зчитує файл і повертає список тудушок

    :param filepath:
    :return: список
    """
    with open(filepath, "r", encoding="utf-8") as file:
        return [line.rstrip("\n") for line in file]


def write_todos(todos_arg, filepath=FILEPATH):
    """
    Записує дані у файл
    :param todos_arg:
    :param filepath:
    """
    with open(filepath, "w", encoding="utf-8") as file:
        file.writelines(todo + "\n" for todo in todos_arg)


if __name__ == "__main__":
    print("hello")
    print(get_todos("todos.txt"))
