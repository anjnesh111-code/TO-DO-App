import best
import FreeSimpleGUI as fg
label=fg.Text("Type in a Todo")
input=fg.InputText(tooltip="Enter your todo",key="todo")
button=fg.Button("Add")
listbox=fg.Listbox(values=best.get_todos(),key="todos",
                   enable_events=True,size=(45,10))
edit_button=fg.Button("Edit")

window=fg.Window("My To-Do App",
                 layout = ([[label],[input,button],[listbox,edit_button]]),
                 font=("Arial",15))
while True:
    event,values=window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos=best.get_todos()
            new_todo=values['todo']+"\n"

            todos.append(new_todo)
            best.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            todos_to_edit=values["todos"][0]
            new_todo=values["todo"]
            todos=best.get_todos()

            index=todos.index(todos_to_edit)
            todos[index]=new_todo+"\n"
            best.write_todos(todos)
            window["todos"].update(values=todos)
        case "todos":
            window["todo"].update(value=values['todos'][0])

        case fg.WIN_CLOSED:
            break

window.close()
