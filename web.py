import streamlit as st
import functions

def add_todo():
    todo = st.session_state['new_todo']
    todos.append(todo + '\n')
    functions.write_todos(todos)
    print(todo)
todos = functions.get_todos()


st.title('My Todo App')
st.subheader('This is my todo app')
st.write('This app is to incease your productivity')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label='Test1', placeholder='Add new todo...',
              on_change=add_todo, key='new_todo',
              label_visibility='hidden')
