import best
import FreeSimpleGUI as fg
label=fg.Text("Type in a TODO")
input=fg.InputText(tooltip="Enter tour todo")
button=fg.Button("ADD!")
window=fg.Window("My To-Do App",layout=([[label],[input],[button]]))
window.read()
window.close()
