import best
import FreeSimpleGUI as fg
label=fg.Text("Type in a Todo")
input=fg.InputText(tooltip="Enter your todo",key="todo")
button=fg.Button("Add")
window=fg.Window("My To-Do App",
                 layout=([[label],[input,button]]),
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

        case fg.WIN_CLOSED:
            break

window.close()
