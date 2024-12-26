def get_todos(filepath="Files/todos.txt"):
    """Read the file in which to-dos
    are stored and print the to-dos
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg,filepath="Files/todos.txt"):
    """
    Write the to-dos given by user in
    the file
    """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)


while True:
    choice = input("Type add,show,continue,exit to exit,complete to delete an item : ")
    choice = choice.strip()

    # To add some todo
    if choice.startswith('add'):
        todo = choice[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        write_todos(todos)

    # To print todo
    elif choice.startswith('show'):
        todos = get_todos()

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
            todos = get_todos()

            delete=todos.pop(delete - 1)

            write_todos(todos)

            print("Todo deleted : ",delete)
        except IndexError:
            print("There is no todo with that index!")
            continue

    # To edit todo

    elif choice.startswith('edit'):
        try:
            number = int(choice[5:])
            number = number - 1

            todos = get_todos()

            todo = input("Enter a new todo : ")
            todos[number] = todo + '\n'

            write_todos(todos)

            print("Item Successfully Edited!")
        except ValueError:
            print("You entered the wrong command!")
            continue

    else:
        print("Invalid Command")
