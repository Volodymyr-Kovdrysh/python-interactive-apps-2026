import os
import argparse
import sys
import functions
import commands


def repl():
    """Читає введення та передає кожну команду диспетчеру"""
    todos = functions.get_todos()
    while True:
        user_action = input("add, show, edit, complete, count, clear, backup, exit: ")
        if not commands.dispatch(todos, user_action):
            break


def build_parser():
    parser = argparse.ArgumentParser(
        prog="python cli.py", description="Todo: діалог або команда під час запуску."
    )
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("show", help="Показати список")
    p_add = sub.add_parser("add", help="Додати тудушку")
    p_add.add_argument("text", nargs="+", help="Текст тудушки (одне або більше слів)")
    p_edit = sub.add_parser("edit", help="Редагувати тудушку")
    p_edit.add_argument("number", type=int, help="Номер тудушки (1..n)")
    p_complete = sub.add_parser("complete", help="Завершити тудушку")
    p_complete.add_argument("number", type=int, help="Номер тудушки (1..n)")
    sub.add_parser("repl", help="Запустити діалог")
    return parser


def run_from_args(args):
    """Передає розібрану команду до наявної логіки.

    :param args: результат parse_args(); обов'язковий параметр
    :return: None; результат дії показують наявні обробники
    """
    if args.command == "repl":
        repl()
        return
    todos = functions.get_todos()

    if args.command == "add":
        text = " ".join(args.text)
        commands.dispatch(todos, f"add {text}")
    elif args.command == "show":
        commands.dispatch(todos, "show")
    elif args.command == "edit":
        commands.dispatch(todos, f"edit {args.number}")
    elif args.command == "complete":
        commands.dispatch(todos, f"complete {args.number}")


def main():
    """Готує сховище та запускає діалог"""
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(functions.FILEPATH):
        with open(functions.FILEPATH, "w", encoding="utf-8"):
            pass

    if len(sys.argv) == 1:
        repl()

    parser = build_parser()
    args = parser.parse_args()
    run_from_args(args)


if __name__ == "__main__":
    main()
    print("Babay!")
