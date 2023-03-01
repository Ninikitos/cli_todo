import functions
import PySimpleGUI as sg
import time
import os


if not os.path.exists("todos.txt"):
    with open("todos.txt", 'w') as file:
        pass


sg.theme("DarkTeal12")
clock_label = sg.Text("", key="clock")
label = sg.Text("Enter To Do item: ")
input_box = sg.InputText(tooltip="Todo item", key="todo")
todo_btn = sg.Button("Add", mouseover_colors="DarkBlue", tooltip="Add todo to a list")
todo_list = sg.Listbox(values=functions.get_todos(),
                       key="todo_item",
                       enable_events=True,
                       size=(30, 10))
edit_btn = sg.Button("Edit", mouseover_colors="DarkBlue", tooltip="Edit todo item")
complete_btn = sg.Button("Complete", mouseover_colors="DarkBlue", tooltip="Complete todo item")
exit_btn = sg.Button("Exit", mouseover_colors="DarkBlue", tooltip="Close application")

window = sg.Window("My To Do app",
                   layout=[[clock_label],
                           [label],
                           [input_box, todo_btn],
                           [todo_list, edit_btn, complete_btn],
                           [exit_btn]],
                   font=("Helvetica", 16))

while True:
    event, value = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %Y %H:%M:%S"))
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = value['todo'] + '\n'
            if len(new_todo) == 1:
                sg.Popup("Field is empty=( Please enter todo item.", font=("Helvetica", 14))
            else:
                todos.append(new_todo)
                functions.write_todos(todos)

            window['todo_item'].update(values=todos)
            window['todo'].update(value="")
        case 'Edit':
            try:
                todo_to_edit = value['todo_item'][0]
                new_todo = value['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)

                window['todo_item'].update(values=todos)
            except IndexError:
                sg.Popup("Please select item that you want to edit.", font=("Helvetica", 14))
        case 'Complete':
            try:
                todos = functions.get_todos()
                todo_to_complete = value['todo_item'][0]
                todos.remove(todo_to_complete)
                functions.write_todos(todos)

                window['todo_item'].update(values=todos)
                window['todo'].update(value=" ")
            except IndexError:
                sg.Popup("Please select item that you want to complete", font=("Helvetica", 14))
        case 'todo_item':
            window['todo'].update(value=value['todo_item'][0])
        case 'Exit':
            break
        case sg.WINDOW_CLOSED:
            break

window.close()
