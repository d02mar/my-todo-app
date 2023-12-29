def get_todos(filepath="files/todos.txt"):
    """ Read the text file and
    return the list of to-do items.
    """
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local

def write_todos(todos_arg, filepath = "files/todos.txt"):
    with open(filepath, "w") as file:
        todos = file.writelines(todos_arg)

