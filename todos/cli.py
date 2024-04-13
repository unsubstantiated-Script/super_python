import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is: ", now)
while True:
    user_action = input("Type add, show, edit, complete, or exit: ")
    user_action = user_action.strip()

    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = functions.get_todos()

        todos.append(todo + '\n')

        functions.write_todos(todos, '../txt_files/todos.txt')

    elif user_action.startswith("show"):
        todos = functions.get_todos()

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1} - {item}"
            print(row)
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = functions.get_todos()
            # Error handling numbers out of range
            if number > len(todos):
                print("That number is out of range.")
                continue

            new_todo = input("Enter the new value for this todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos(todos, '../txt_files/todos.txt')
        # Error handling wrong input
        except ValueError:
            print("Your command is not valid.")
            continue
    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = functions.get_todos()
            if number > len(todos):
                print("That number is out of range.")
                continue

            index = number - 1
            todo_to_remove = todos[index].strip('\n')

            todos.pop(index)

            functions.write_todos(todos, '../txt_files/todos.txt')

            message = f"Todo \"{todo_to_remove}\" was removed from the list."
            print(message)
        except ValueError:
            print("Your command is not valid.")
            continue
    elif user_action.startswith("exit"):
        break
    else:
        print("Command is not valid.")

        print("Adios!")
