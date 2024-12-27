import time
print(time.strftime("It's %d-%b-%Y , %H:%M:%S"))
import best
while True:
    choice = input("Type add,show,continue,exit to exit,complete to delete an item : ")
    choice = choice.strip()

    # To add some todo
    if choice.startswith('add'):
        todo = choice[4:]

        todos = best.get_todos()

        todos.append(todo + '\n')

        best.write_todos(todos)

    # To print todo
    elif choice.startswith('show'):
        todos =best.get_todos()

        for i, j in enumerate(todos):
            print(i + 1, j.strip('\n'))


    elif choice.startswith('continue'):
        continue
    elif choice.startswith('exit'):
        print("BYE")
        break
    # To delete todo
    elif choice.startswith('complete'):
        try:
            delete = int(choice[9:])
            todos = best.get_todos()

            delete=todos.pop(delete - 1)

            best.write_todos(todos)

            print("Todo deleted : ",delete)
        except IndexError:
            print("There is no todo with that index!")
            continue

    # To edit todo

    elif choice.startswith('edit'):
        try:
            number = int(choice[5:])
            number = number - 1

            todos = best.get_todos()

            todo = input("Enter a new todo : ")
            todos[number] = todo + '\n'

            best.write_todos(todos)

            print("Item Successfully Edited!")
        except ValueError:
            print("You entered the wrong command!")
            continue

    else:
        print("Invalid Command")

