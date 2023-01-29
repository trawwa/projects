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


def listUpdate():
    clearList()
    for task in tasks:
        taskListbox.insert('end', task)


def deleteTask():
    try:
        valueFromList = taskListbox.get(taskListbox.curselection())
        if valueFromList in tasks:
            tasks.remove(valueFromList)
            listUpdate()
            cursor.execute('delete from tasks where title = ?', (valueFromList,))
    except:
        messagebox.showinfo('Error!', 'No Task Selected. Cannot Delete.')


def deleteAllTasks():
    messageBox = messagebox.askyesno('Delete All', 'Are You Sure?')
    if messageBox == True:
        while(len(tasks) != 0):
            tasks.pop()
        cursor.execute('delete from tasks')
        listUpdate()

def clearList():
    taskListbox.delete(0, 'end')


def close():
    print(tasks)
    guiWindow.destroy()


def retrieveDatabase():
    while(len(tasks) != 0):
        tasks.pop()
    for row in cursor.execute('select title from tasks'):
        tasks.append(row[0])


