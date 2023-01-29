# GUI To-Do List

from tkinter import *
from tkinter import messagebox
import sqlite3 as sql

def addTask():
    taskString = taskField.get()
    if len(taskString) == 0:
        messagebox.showinfo('Error!', 'Field is empty.')
    else:
        tasks.append(taskString)
        cursor.execute('Insert into task values (?)', (taskString ,))
        listUpdate()
        taskField.delete(0, 'end')

