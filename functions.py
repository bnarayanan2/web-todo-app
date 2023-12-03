def get_todos(filepath="todos.txt"):
    """ Read the text file and return the list of to-do items."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_local, filepath_local="todos.txt"):
    """ Write the to-do items list in text file."""
    with open(filepath_local, 'w') as file_local:
        file_local.writelines(todos_local)

