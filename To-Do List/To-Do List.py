#CODSOFT Task - To-Do List
import tkinter as tk                    
from tkinter import ttk                
from tkinter import messagebox
from tkinter import *         
from tkinter.ttk import *
import sqlite3 as sql                   


#Functions
def add_task():  
    task_name = task_field.get()  
    if len(task_name) == 0:  
        messagebox.showinfo("Error!","Field can't be Empty")  
    else:  
        tasks.append(task_name)  
        the_cursor.execute('insert into tasks values (?)', (task_name ,))  
        list_update()  
        task_field.delete(0,'end')  
  
def list_update():  
    clear_list()  
    for task in tasks:  
        task_list.insert('end', task)  
  
def delete_task():  
    try:  
        value_dem = task_list.get(task_list.curselection())  
        if value_dem in tasks:  
            tasks.remove(value_dem)  
            list_update()  
            the_cursor.execute('delete from tasks where title = ?', (value_dem,))  
    except:  
        messagebox.showinfo('Error!', 'No Task Selected!')        
  
def delete_all_tasks():  
    message1 = messagebox.askyesno('Delete All!', 'Are you sure?!')  
    if message1 == True:  
        while(len(tasks) != 0):  
            tasks.pop()  
        the_cursor.execute('delete from tasks')  
        list_update()  
  
def clear_list():  
    task_list.delete(0, 'end')  
  
def exists():  
    message2 = messagebox.askyesno('Exit!', 'Do you want to exit?')  
    if message2 == True:  
        print(tasks)  
        guiWindow.destroy()  
  
def retrieve_database():  
    while(len(tasks) != 0):  
        tasks.pop()  
    for row in the_cursor.execute('select title from tasks'):  
        tasks.append(row[0])  
  
#Window
if __name__ == "__main__":  
    guiWindow = tk.Tk()  
    guiWindow.title("To-Do List - CODSOFT")  
    guiWindow.geometry("500x450+750+250")  
    guiWindow.resizable(False, False)  
    guiWindow.configure(bg = "#595258")  
    the_connection = sql.connect('TaskList.db')  
    the_cursor = the_connection.cursor()  
    the_cursor.execute('create table if not exists tasks (title text)')  
  
    tasks = []  
    
    #Frames  
    header_frame = tk.Frame(guiWindow, bg = "#d5f0f7")  
    functions_frame = tk.Frame(guiWindow, bg = "#d5f0f7")  
    listbox_frame = tk.Frame(guiWindow, bg = "#d5f0f7")  
  
    header_frame.pack(fill = "both")  
    functions_frame.pack(side = "left", expand = True, fill = "both")  
    listbox_frame.pack(side = "right", expand = True, fill = "both")  
      
    header_label = ttk.Label(  
        header_frame,  
        text = "To-Do List",  
        font = ("Georgia bold", "30", "underline"),  
        background = "#d5f0f7",  
        foreground = "#10213d"  
    )  
    header_label.pack(padx = 20, pady = 20)  
  
    task_label = ttk.Label(  
        functions_frame,  
        text = "Enter the Task Name:",  
        font = ("Georgia", "13", "bold"),  
        background = "#d5f0f7",  
        foreground = "#10213d"  
    )  
    task_label.place(x = 30, y = 10)  
      
    task_field = ttk.Entry(  
        listbox_frame,  
        font = ("Georgia bold", "12"),  
        width = 18,  
        background = "#10213d",  
        foreground = "#10213d"  
    )  
    task_field.place(x = 10, y = 10)  
    style = Style()
    style1 = Style()
 
    #Button Configurations
    style.configure('W.TButton', font =
               ('calibri', 10, 'bold'),
                foreground = 'red')
    style.configure('M.TButton', font =
               ('calibri', 10, 'bold'),
                foreground = 'black')
    style1.configure('TButton', font =
               ('calibri', 10, 'bold'),
                foreground = 'green')
    
    add_button = ttk.Button(  
        functions_frame,  
        text = "Add Task",  
        style='TButton',
        width = 20,  
        command = add_task  
    )
    del_button = ttk.Button(  
        functions_frame,  
        text = "Delete Task", 
        style='W.TButton', 
        width = 20,  
        command = delete_task  
    )  
    del_all_button = ttk.Button(  
        functions_frame,  
        text = "Delete All Tasks!!",  
        style='W.TButton', 
        width = 20,  
        command = delete_all_tasks  
    )  
    exit_button = ttk.Button(  
        functions_frame,  
        style='M.TButton',
        text = "Exit!",  
        width = 20,  
        command = exists  
    )  
    add_button.place(x = 30, y = 80)  
    del_button.place(x = 30, y = 136.55)  
    del_all_button.place(x = 30, y = 193.33)  
    exit_button.place(x = 30, y = 250)  
  
    task_list = tk.Listbox(  
        listbox_frame,  
        width = 30,  
        height = 12,  
        selectmode = 'SINGLE',  
        background = "#fcffe6",  
        foreground = "#000000",  
        selectbackground = "#CD853F",  
        selectforeground = "#FFFFFF"  
    )  
    task_list.place(x = 10, y = 80)  
  
    retrieve_database()  
    list_update()  
    
    guiWindow.mainloop()  
    Image_icon = PhotoImage(file="Images/ListLogo.png")
    guiWindow.iconphoto(False, Image_icon)
    the_connection.commit()  
    the_cursor.exists()  
