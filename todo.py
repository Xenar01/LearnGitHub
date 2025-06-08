# الملف: todo.py
import sys

tasks = []

def add(task: str):
    tasks.append(task)
    print(f"أُضيفت مهمة: {task}")

def list_tasks():
    if not tasks:
        print("لا توجد مهام بعد.")
    for i, t in enumerate(tasks, 1):
        print(f"{i}. {t}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("استعمل: python todo.py add <مهمة> | list")
    elif sys.argv[1] == "add":
        add(" ".join(sys.argv[2:]))
    elif sys.argv[1] == "list":
        list_tasks()
