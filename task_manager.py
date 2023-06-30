import tkinter as tk
from tkinter import messagebox

# The main window
window = tk.Tk()
window.title("To-Do List Application")

# Create the to-do list
todo_list = []


def add_task():
    task = task_entry.get()
    if task:
        todo_list.append(task)
        task_entry.delete(0, tk.END)
        update_listbox()


def delete_task():
    try:
        selected_index = listbox.curselection()[0]
        todo_list.pop(selected_index)
        update_listbox()
    except IndexError:
        pass


def update_listbox():
    listbox.delete(0, tk.END)
    for task in todo_list:
        listbox.insert(tk.END, task)


# Create the user interface elements
frame = tk.Frame(window)
frame.pack(pady=10)

listbox = tk.Listbox(
    frame,
    width=80,
    height=20,
    font=("Helvetica", 14)
)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

task_entry = tk.Entry(
    window,
    font=("Helvetica", 14)
)
task_entry.pack(pady=10)

add_button = tk.Button(
    window,
    text="Add Task",
    command=add_task
)
add_button.pack(pady=5)

delete_button = tk.Button(
    window,
    text="Delete Task",
    command=delete_task
)
delete_button.pack(pady=5)

window.mainloop()
