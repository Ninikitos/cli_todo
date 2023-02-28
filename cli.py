from functions import get_todos, write_todos
from time import strftime

now = strftime("%b %d, %Y %H:%M:%S")
print(now)

while True:
    print("")
    print("Options: ")
    print("- add [todo item]")
    print("- edit [index of todo item]")
    print("- complete [index of todo item]")
    print("- show")
    print("- exit")
    user_input = input("Enter your option: ")
    user_input = user_input.strip()
    print("")

    if user_input.startswith('add'):
        new_item = user_input[4:]

        todo_items = get_todos()
        todo_items.append(new_item.capitalize() + '\n')
        write_todos(items=todo_items)

    elif user_input.startswith('show'):
        todo_items = get_todos()
        new_todo = [item.strip('\n') for item in todo_items]
        print("Items: ")
        for index, item in enumerate(new_todo):
            output = f"{index+1}. {item}"
            print(output)

    elif user_input.startswith('edit'):
        try:
            edit_item = int(user_input[5:])
            todo_items = get_todos()

            new_item = input("Enter new text: ")
            todo_items[edit_item - 1] = new_item.capitalize() + '\n'
            write_todos(items=todo_items)

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_input.startswith('complete'):
        try:
            complete_item = int(user_input[9:])

            todo_items = get_todos()
            todo_items.pop(complete_item - 1)
            write_todos(items=todo_items)

        except IndexError:
            print("Your command is not valid")
            continue

    elif user_input.startswith('exit'):
        break
    else:
        print("Command is not valid")
print("Bye!")
