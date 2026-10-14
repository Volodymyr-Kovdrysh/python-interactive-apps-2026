import functions


def do_add(todos, argument):
    """Додає справу та зберігає список.

    :param todos: поточний список справ без переносів рядків
    :param argument: текст нової справи
    :return: True — продовжувати діалог, навіть якщо текст порожній
    """
    if not argument:
        print("\tВведіть тудушку")
        return True
    todos.append(argument)
    functions.write_todos(todos)
    return True


def do_show(todos, argument):
    """Показує список справ.

    :param todos: поточний список справ
    :param argument: приймаємо для спільного способу виклику; не використовуємо
    :return: True — продовжувати діалог
    """
    if not todos:
        print("\tСписок поржній")
    for number, todo in enumerate(todos, start=1):
        print(f"{number} -- {todo}")
    return True


def do_edit(todos, argument):
    """
    edit <number>

    Змінює текст справи за номером і зберігає список.
    :param todos: поточний список справ
    :param argument: номер справи у вигляді рядка
    :return: True — продовжувати діалог
    """
    number = int(argument)
    if number < 1 or number > len(todos):
        raise IndexError
    new_todo = input("Введіть новий текст: ").strip()
    if not new_todo:
        print("\tВведіть тудушку")
        return True
    todos[number - 1] = new_todo
    functions.write_todos(todos)
    return True


def do_complete(todos, argument):
    """Видаляє виконану справу й зберігає список.

    :param todos: поточний список справ
    :param argument: номер справи у вигляді рядка
    :return: True — продовжувати діалог
    """
    number = int(argument)
    if number < 1 or number > len(todos):
        raise IndexError
    completed_todo = todos.pop(number - 1)
    functions.write_todos(todos)
    print(f'Виконано: "{completed_todo}"')
    return True


def do_exit(todos, argument):
    """Просить завершити діалог.

    :param todos: приймаємо для спільного способу виклику; не використовуємо
    :param argument: приймаємо для спільного способу виклику; не використовуємо
    :return: False — завершити діалог
    """
    return False


# Таблиця команд
COMMANDS = {
    "add": do_add,
    "exit": do_exit,
    "show": do_show,
    "edit": do_edit,
    "complete": do_complete,
}


def dispatch(todos, user_action):
    """
    Виконує одну команду.

    Повертає:
        True  — продовжувати REPL
        False — вийти (exit)

    :param todos: поточний список справ
    :param user_action: повний рядок введення користувача
    """

    parts = user_action.strip().split(maxsplit=1)
    if not parts:
        print("Введіть команду")
        return True
    command = parts[0]
    argument = parts[1] if len(parts) > 1 else ""

    handler = COMMANDS.get(command)

    if handler is None:
        print("Невідома команда")
        return True

    try:
        return handler(todos, argument)
    except ValueError:
        print("Введіть цілий номер тудушки")
        return True
    except IndexError:
        print("Невірний номер тудушки")
        return True
