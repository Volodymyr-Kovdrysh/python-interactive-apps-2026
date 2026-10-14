import os
import argparse
import sys
import functions
import commands


def repl():
    """Читає введення та передає кожну команду диспетчеру"""
    todos = functions.get_todos()
    while True:
        user_action = input("add, show, edit, complete, exit: ")
        if not commands.dispatch(todos, user_action):
            break


def build_parser():
    parser = argparse.ArgumentParser(
        prog="cli.py", description="Todo: діалог або команда під час запуску."
    )
    return parser


def main():
    """Готує сховище та запускає діалог"""
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(functions.FILEPATH):
        with open(functions.FILEPATH, "w", encoding="utf-8"):
            pass

    repl()


if __name__ == "__main__":
    main()
    print("Babay!")
