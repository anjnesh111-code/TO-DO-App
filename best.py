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


