FILEPATH = "todos.txt"


def get_todos(file_path=FILEPATH):
    """
    Read a list of items out of a text file.
    """
    with open(file_path, 'r') as file_to_read:
        todos_list = file_to_read.readlines()
    return todos_list


def write_todos(todos_list, file_path=FILEPATH):
    """
    Write items to a text file.
    """
    with open(file_path, 'w') as file_to_write:
        file_to_write.writelines(todos_list)


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
