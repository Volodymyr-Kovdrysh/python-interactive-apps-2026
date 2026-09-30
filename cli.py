import os
import functions


def repl():
    todos = functions.get_todos()
    while True:
        parts = input("add, show, edit, exit: ").strip().split(maxsplit=1)
        if not parts:
            print("Введіть команду")
            continue
        command = parts[0]
        argument = parts[1] if len(parts) > 1 else ""

        if command == "add":
            if not argument:
                print("\tВведіть тудушку")
                continue
            todos.append(argument)
            functions.write_todos(todos)
        elif command == "show":
            if not todos:
                print("\tСписок поржній")
            for number, todo in enumerate(todos, start=1):
                print(f"{number} -- {todo}")

        elif command == "edit":
            try:
                number = int(argument)
                if number < 1 or number > len(todos):
                    raise IndexError
                new_todo = input("Введіть новий текст: ").strip()
                if not new_todo:
                    print("\tВведіть тудушку")
                    continue

                todos[number - 1] = new_todo
                functions.write_todos(todos)
            except ValueError:
                print("Введіть цілий номер тудушки")
            except IndexError:
                print("Невірний номер тудушки")
        elif command == "exit":
            break
        else:
            print("Невідома команда")


def main():
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(functions.FILEPATH):
        with open(functions.FILEPATH, "w", encoding="utf-8"):
            pass

    repl()


if __name__ == "__main__":
    main()
    print("Babay!")
