from tkinter import *
from tkinter import messagebox
import pickle

root=Tk()
root.title("To Do List App")

# Function for Adding Task 
def add_task():
    task=entry_task.get()
    if task != "":
        list_tasks.insert(END,task)
        entry_task.delete(0,END)
    else:
        messagebox.showwarning(title="Warning!",message="You must Enter a Task!")

# Function for Delete Task         
def delet_task():
    try:
        task_index=list_tasks.curselection()[0]
        list_tasks.delete(task_index)
    except:
        messagebox.showwarning(title="Warning!",message="Please Select a Task!")
def save_tasks():
    tasks=list_tasks.get(0,list_tasks.size())
    pickle.dump(tasks,open('Tasks.dat','wb'))

# Function for Read all Task     
def load_tasks():
    try:
        tasks=pickle.load(open('Tasks.dat','rb'))
        list_tasks.delete(0,END)
        for task in tasks:
            list_tasks.insert(END,task)
    except:
        messagebox.showwarning(title="Warning!",message="Cannot Find any Task File!")
                                  

fram_tasks=Frame(root)
fram_tasks.pack()

#   list_Task
list_tasks=Listbox(fram_tasks,width=38,height=10,bg="#34282C",fg="white")
list_tasks.pack()
list_tasks.config(font=("vardan",12,'bold'))

#  Entry
entry_task=Entry(root,width=43,bg="#FFFDD0",fg="black")
entry_task.pack()
entry_task.config(font=("vardan",10,'bold'))

#  Adding Button
btn_add=Button(root,text="Add Task", width=43,bg="#EE9A4D",fg="black",command=add_task)
btn_add.pack()
btn_add.config(font=("vardan",10,'bold'))

#  Delete Button
btn_delete=Button(root,text="Delete Task", width=43,bg="#EE9A4D",fg="black",command=delet_task)
btn_delete.pack()
btn_delete.config(font=("vardan",10,'bold'))

#  Load Button
btn_load=Button(root,text="Read All Task", width=43,bg="#EE9A4D",fg="black",command=load_tasks)
btn_load.pack()
btn_load.config(font=("vardan",10,'bold'))

#  Saving Button
btn_save=Button(root,text="Save Task", width=43,bg="#EE9A4D",fg="black",command=save_tasks)
btn_save.pack()
btn_save.config(font=("vardan",10,'bold'))

root.mainloop()