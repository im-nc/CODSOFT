#CODSOFT Task - Contact Book
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk


#The Window Configuration
root = Tk()
root.geometry('700x550')
root.config(bg = '#2b2d30')
root.title("Contact Book - CODSOFT")
root.resizable(0,0)
contactlist = [['John', '12345', 'john@mail', '123G road'],
               ['Eva', '98765', 'eva@mail', '423R road']]

Name = StringVar()
Phone_no = StringVar()
email = StringVar()
address = StringVar()


#Creating the frame
frame = Frame(root)
frame.pack(side = RIGHT)

scroll = Scrollbar(frame, orient=VERTICAL)
select = Listbox(frame, yscrollcommand=scroll.set,font=('Georgia',13,'bold'),selectbackground="#2d2d2d",selectforeground="#ffffff",bg="#fcffe6",width=20,height=18,borderwidth=3,relief="groove")
scroll.config (command=select.yview)
scroll.pack(side=RIGHT, fill=Y)
select.pack(side=LEFT,  fill=BOTH, expand=1)

header_frame = tk.Frame(root, bg = "#2b2d30")
header_frame.pack(fill = "y")  
header_label = ttk.Label(  
        header_frame,  
        text = "My Contact Book",  
        font = ("Georgia bold", "20", "underline"),  
        background = "#2b2d30",  
        foreground = "#ffffff"  
    )
header_label.pack(padx = 20, pady = 20)

#Function to get the selected values
def Selected():
	print("hello",len(select.curselection()))
	if len(select.curselection())==0:
		messagebox.showerror("Error!", "Please Select the Name")
	else:
		return int(select.curselection()[0])

#Function to search a Contact
def SearchContact():
    for i in contactlist:
        if ((Name.get() in i) or (Phone_no.get() in i)):
            print("True")
            NAME = i[0]
            PHONE = i[1]
            EMAIL = i[2]
            ADDRESS = i[3]
            print(NAME,PHONE,EMAIL,ADDRESS)
            Name.set(NAME)
            Phone_no.set(PHONE)
            email.set(EMAIL)
            address.set(ADDRESS)
            
#Function to add a new contact
def AddContact():
    if Name.get()!="" and Phone_no.get()!="" and email.get()!="" and address.get()!="":
        contactlist.append([Name.get(), Phone_no.get(), email.get(), address.get()])
        print(contactlist)
        Select_set()
        EntryReset()
        messagebox.showinfo("Confirmed", "Successfully Added New Contact")

    else:
        messagebox.showerror("Error","Please fill all the informations")


#Function to edit existing contact
def UpdateDetail():
	if Name.get() and Phone_no.get() and email.get() and address.get():
		contactlist[Selected()] = [Name.get(), Phone_no.get(), email.get(), address.get()]
		messagebox.showinfo("Confirmation", "Successfully Updated Contact")
		EntryReset()
		Select_set()
  

	elif not(Name.get()) and not(Phone_no.get()) and not(email.get()) and not(address.get()) and not(len(select.curselection())==0):
		messagebox.showerror("Error", "Please all fill the information")

	else:
		if len(select.curselection())==0:
			messagebox.showerror("Error", "Please Select the Name and \n Press Load button")
		else:
			message1 = """To Load the all information of \n 
						  Selected Row Press Load button\n.
						  """   
			messagebox.showerror("Error", message1)

			messagebox.showerror("Error", message1)

def EntryReset():
    Name.set('')
    Phone_no.set('')
    email.set('')
    address.set('')

#Function to delete selected contact
def Delete_Entry():
    if len(select.curselection())!=0:
        result=messagebox.askyesno('Confirmation','Do you want to delete the contact\n which you selected?')
        if result==True:
            del contactlist[Selected()]
            Select_set()
    else:
        messagebox.showerror("Error", 'Please select the Contact')

   
#Function for viewing the contacts
def VIEW():
    NAME, PHONE, EMAIL, ADDRESS = contactlist[Selected()]
    Name.set(NAME)
    Phone_no.set(PHONE)
    email.set(EMAIL)
    address.set(ADDRESS)   
        

#Function to exist the window
def EXIT():
    root.destroy()


def Select_set() :
    contactlist.sort()
    select.delete(0,END)
    for name,phone,email,address in contactlist :
        select.insert (END, name)
Select_set()

def SearchContact():
    return 0

#Define all buttons, labels and entries

Label(root, text = 'Name', font=("Times new roman",12,"bold","underline"), bg = '#2b2d30', fg='#ffffff').place(x= 30, y=90)
Entry(root, textvariable = Name, width=30).place(x= 170, y=90)

Label(root, text = 'Contact No.', font=("Times new roman",12,"bold","underline"),bg = '#2b2d30', fg='#ffffff').place(x= 30, y=140)
Entry(root, textvariable = Phone_no, width=30).place(x= 170, y=140)

Label(root, text = 'Email', font=("Times new roman",12,"bold","underline"), bg = '#2b2d30', fg='#ffffff').place(x= 30, y=190)
Entry(root, textvariable = email, width=30).place(x= 170, y=190)

Label(root, text = 'Address', font=("Times new roman",12,"bold","underline"), bg = '#2b2d30', fg='#ffffff').place(x= 30, y=240)
Entry(root, textvariable = address, width=30).place(x= 170, y=240)

Button(root,text="Add", font='Georgia 10 bold',bg='#fdfdfd', command = AddContact, padx=50). place(x= 30, y=320)

Button(root,text="View", font='Georgia 10 bold',bg='#fdfdfd', command = VIEW ,padx=40).place(x= 260, y=320)

Button(root,text="Search", font='Georgia 10 bold',bg='#fdfdfd', command = SearchContact, padx=40). place(x= 30, y=380)

Button(root,text="Edit", font='Georgia 10 bold',bg='#fdfdfd',command = UpdateDetail, padx=42).place(x= 260, y=380)

Button(root,text="Delete", font='Georgia 10 bold',bg='#fdfdfd',command = Delete_Entry, padx=42).place(x= 30, y=440)

Button(root,text="Exit", font='Georgia 10 bold',bg='red',fg="White", command = EXIT, padx=42).place(x= 260, y=440)


root.mainloop()
  

