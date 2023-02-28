FILE_PATH = "todos.txt"


def get_todos(filepath=FILE_PATH):
    """Read a file and return list of to-dos"""
    with open(filepath, "r") as file:
        todo_items = file.readlines()
    return todo_items


def write_todos(items, filepath=FILE_PATH):
    """Writes todos into file"""
    with open(filepath, "w") as file:
        file.writelines(items)
