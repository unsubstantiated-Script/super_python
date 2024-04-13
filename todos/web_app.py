import streamlit as st
import functions

todos = functions.get_todos('./txt_files/todos.txt')


def add_todo():
    todo_input = st.session_state["new_todo"] + "\n"
    todos.append(todo_input)
    functions.write_todos(todos, './txt_files/todos.txt')


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity!")

for index, todo in enumerate(todos):
    # dis returns un bool
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos, './txt_files/todos.txt')
        del st.session_state[todo]
        st.rerun()
st.text_input(label="", placeholder="Add new todo...", on_change=add_todo, key='new_todo')
