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


if __name__ == "__main__":
    guiWindow = Tk()
    guiWindow.title("To-Do List")
    guiWindow.geometry("665x400+550+250")
    guiWindow.resizable(0, 0)
    guiWindow.configure(bg="#B5E5CF")

    connection = sql.connect('listOfTasks.db')
    cursor = connection.cursor()
    cursor.execute('create table if not exists tasks (little text)')

    tasks = []

    functionsFrame = Frame(guiWindow, bg="black")
    functionsFrame.pack(side='top', expand=True, fill='both')
    taskLabel = Label(functionsFrame,
                      text='Enter The Task:',
                      font=("arial", "14", "bold"),
                      background="black",
                      foreground="white")

    taskLabel.place(x=20, y=30)

    taskField = Entry(functionsFrame,
                      font=("arial", "14", "bold"),
                      width=42,
                      background="black",
                      foreground="white")

    taskField.place(x=180, y=30)

    addButton = Button(functionsFrame,
                       text="Add Task",
                       width=15,
                       bg='#D4AC0D',
                       font=("arial", "14", "bold"),
                       command=addTask)

    delButton = Button(functionsFrame,
                       text="Delete Task",
                       width=15,
                       bg='#D4AC0D',
                       font=('arial', '14', 'bold'),
                       command=deleteTask)

    delAllButton = Button(functionsFrame,
                          text="Delete All Button",
                          width=15,
                          bg='#D4AC0D',
                          font=('arial', '14', 'bold'),
                          command=deleteAllTasks)

    exitButton = Button(functionsFrame,
                        text='Exit',
                        width=52,
                        bg='#D4AC0D',
                        font=('arial', '14', 'bold'),
                        command=close)

    addButton.place(x=18, y=80)
    delButton.place(x=240, y=80)
    delAllButton.place(x=460, y=80)
    exitButton.place(x=17, y=330)

    taskListbox = Listbox(functionsFrame,
                          width=57,
                          height=7,
                          font='bold',
                          selectmode='SINGLE',
                          background='WHITE',
                          foreground='BLACK',
                          selectbackground='#D4AC0D',
                          selectgoreground='BLACK')
