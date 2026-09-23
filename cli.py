def repl():
    todos = []
    while True:
        parts = input("add, show, exit: ").strip().split(maxsplit=1)
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
        elif command == "show":
            if not todos:
                print("\tСписок поржній")
            for number, todo in enumerate(todos, start=1):
                print(f"{number} -- {todo}")
        elif command == "exit":
            break
        else:
            print("Невідома команда")


def main():
    repl()


if __name__ == "__main__":
    main()
    print("Babay!")
