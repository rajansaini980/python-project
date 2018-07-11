# rajan todo list programme
from tkinter import *
from tkinter import messagebox
import sys          #System Module For Exit Function
import random
import tkinter.messagebox as msg
from tkinter import Text ,Tk

root=Tk()

#Title of Root Window
root.title("To-Do")

root.config()

#Creating an empty list for some operations like asc_order and desc_order,remove,num_of_tasks etc.As these operatios on Listbox are not applicable.
task_list=[]


#Method for Update the task_list(ListBox) after every operation
def update_mylist():
    delete_task()
    for task in task_list:
        mylist.insert("end",task)


#Method for deleting all the tasks.
def delete_task():
    mylist.delete(0,END)


# #Method for removing placeholder.
# press=False
# def Add_Task(event):
#     entry.delete(0,END)
#     press = True


def add_task():
    task=entry.get("1.0",END)
    task_list.append(task)
    update_mylist()



#Method for deleting all the tasks.
def clear_task():
    sure=msg.askyesno("Are you really want to delete the all tasks ???")
    if sure==True:
        global task_list       #OR--->>just write it in if block--->>mylist.delete(0,END)
        task_list=[]
        update_mylist()



#Method for removing a particular task or in sequence.
def remove():
    task = mylist.get("active")
    # Try Block for not producing error on python console if there is no task for removal and we press the remove button.
    if task in task_list:
            task_list.remove(task)
            update_mylist()
    else:
        error = "There is no task in task_list(ListBox)."
        msg.showerror("Error", error)

#Method for putting the tasks in ascending order in task_list(ListBox).
def asc_order():
    task_list.sort()
    update_mylist()


#Method for putting the tasks in descending order in task_list(ListBox).
def desc_order():
    task_list.sort()
    task_list.reverse()
    update_mylist()


#Method for picking up a random task from task_list(ListBox).
def choose_random():
    task=mylist.get("active")
    if task in task_list:
       random.shuffle(task_list)
       random_task=task_list[0]
       msg.showinfo("Randomly chosen task is",random_task)
    else:
        error="There is no task in task_list(ListBox).Please add some task"
        msg.showerror("Error",error)


#Method for calculating the number os tasks in task_list(ListBox).
def num_of_task():
    # OR--->>To calculate number of tasks just check len(task_list)
    j=0
    for i in task_list:
        j=j+1
    msg.showinfo("Number of tasks", j)


#Method to exit from the root window.
def exit():
    result=messagebox.askyesno('exit','Are you sure want to exit')
    if result==True:
        sys.exit()
    else:
        pass


#Label for printing -->>To-Do List<<-- on root wimdow.
label=Label(root,text="To-Do List",width="9",font='10')
label.place(x=42,y=25)



#Entry for input as here user will enter the task to add in task_list(ListBox).
entry=Text(root,width=30,height="1")
# entry.insert("end",'Enter your task')
# entry.bind("<Button>",Add_Task)
entry.place(x=42,y=55)


#ListBox for keeping the all tasks.
mylist=Listbox(root,width=50,height=20)
mylist.place(x=42,y=100)


#Button for adding new tasks in task_list(ListBox).
add_item_button=Button(root,text="Add to-do item",command=add_task,width=15)
add_item_button.place(x=435,y=170)


#Button for deleting all tasks from task_list(ListBox).
clr_task_button=Button(root,text="Clear all tasks",width=15,command=clear_task)
clr_task_button.place(x=435,y=200)


#Button for deleting one task from task_list(ListBox).
remove_button=Button(root,text="Remove",command=remove,width=15)
remove_button.place(x=435,y=230)


#Button to sort the tasks in ascending order.
asc_sort_button=Button(root,text="Ascending sort",command=asc_order,width=15)
asc_sort_button.place(x=435,y=260)


#Button to sort the tasks in descending order.
sort_desc_button=Button(root,text="Sort(DESC)",command=desc_order,width=15)
sort_desc_button.place(x=435,y=290)


#Button to choose a random task from the task_list(ListBox).
choose_random_button=Button(root,text="Choose Random",command=choose_random,width=15)
choose_random_button.place(x=435,y=320)
#Button to calculate the number of tasks in task_list(ListBox).
number_of_tasks_button=Button(root,text="Number of Tasks",command=num_of_task,width=15)
number_of_tasks_button.place(x=435,y=350)
#Button for exiting.
exit_button=Button(root,text="Exit",font=5,command=exit,width=8,bg="powder blue")  #For Exit above defined exit function is not needed here sys module invokes the exit function with only command=exit or "exit"
exit_button.place(x=440,y=420)
#OR-->>Instructions for exit function
# exit_button=Button(root,text="Exit",command=exit)
# exit_button=Button(root,text="Exit",command="exit")
root.minsize(600,600)
root.maxsize(900,650)
root.mainloop()