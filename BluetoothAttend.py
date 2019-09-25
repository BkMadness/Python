#Import tKinter , Bluetooth ,MYSQL Modules

from Tkinter import *
import Tkinter as tk 
import bluetooth 
from  tkMessageBox import *
import MySQLdb

#Database Connection
db = MySQLdb.connect("localhost","root","root" , "studentregister")
cur = db.cursor()


#Create TK root Widget 
root = Tk()
root.title('Bluetooth Register ')


#Read Text from user 
studentno = StringVar()
firstname= StringVar()
lastname = StringVar()
DOBent  = StringVar()
address1= StringVar()
address2= StringVar()
town = StringVar()
postcode=StringVar()
email = StringVar()
select=StringVar()

#Display Text for Entry
studentNolabel = Label(text="Student No").grid(row=0)
studentEntry = Entry(root,textvariable=studentno)
studentEntry.grid(row=0,column=1)


firstNamelabel = Label(text="First Name").grid(row=1)
firstNameEntry = Entry(root,textvariable=firstname)
firstNameEntry.grid(row=1,column=1)


lastNamelabel = Label(text="Last Name").grid(row=2)
LastNameEntry = Entry(root,textvariable=lastname)
LastNameEntry.grid(row=2,column=1)

dOBlabel = Label(text="DOB").grid(row=3)
DOBEntry = Entry(root,textvariable=DOBent)
DOBEntry.grid(row=3,column=1)

address1label= Label(text="Address 1 ").grid(row=4)
adddress1Entry = Entry(root,textvariable=address1)
adddress1Entry.grid(row=4,column=1)

address2label = Label(text="Address 2 ").grid(row=5)
address2Entry = Entry(root,textvariable=address2)
address2Entry.grid(row=5,column=1)

townlabel= Label(text="Town").grid(row=6)
TownEntry = Entry(root,textvariable=town)
TownEntry.grid(row=6,column=1)

Postcodelabel= Label(text="City").grid(row=7)
postcodeEntry = Entry(root,textvariable=postcode)
postcodeEntry.grid(row=7,column=1)

emaillabel= Label(text="Module").grid(row=8)
emailEntry = Entry(root,textvariable=email)
emailEntry.grid(row=8,column=1)



#A function that reads Entries from the users , the entry boxes validate the enteries and saved to Database 
def submitenteries():
    cur = db.cursor()
    cur.execute("""INSERT INTO studentdetail2s(studentno,firstname,lastname,DOB,Address1,Address2,Town,City,Module,MacAddress) VALUES('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" %(studentno.get(),firstname.get(),lastname.get(),DOBent.get(),address1.get(),address2.get(),town.get(),postcode.get(),email.get(),nameVar.get()))
    db.commit()
    
    if not studentno.get():
        showerror("Student Number", "Please Enter Student Number")
    if not firstname.get():
        showerror("Student Name", "Please Enter Student Name")
    if not lastname.get():
        showerror("Student Last Name", "Please Enter Student's Last Name")
    if not DOBent.get():
        showerror("DOB","Please Enter Student's Date of Birth")
    if not address1.get():
       showerror("Address 1","Please Enter Address 1")
    if not address2.get():
        showerror("Address 2", "Please Enter Address 2")
    if not town.get():
         showerror("Town", "Please Enter Student's Town")
    if not postcode.get():
         showerror("Post", "Please Enter Student's Postcode")
    if not email.get():
         showerror("Email", "Please Enter Student's Email")
    if not nameVar.get():
        showerror("Device Scan", "Please Scan ")
    print 'Sucessfully Addeded to Database ! '

#Buttons that Register Students with Bluetooth and Exits 
b = Button(text="Register" , command=submitenteries).grid(row=19 ,column=2)
c = Button(text="Exit",command=root.destroy).grid(row=19,column=3)

#Displays the Bluetooth Devices that are detected 
listbox = Listbox()
listlabel= Label(text="Student Devices").grid()
listbox.grid()

#allows users to select the macaddresses and displays in the Label
selectedlabel= Label(text= "Mac Address").grid(row=12)
nameVar = StringVar()
seletedEntry= Entry(textvariable=nameVar).grid(row=12, column=1)

#A method for a Bluetooth Scan and pairs
def bluetoothscan():
    nearby_devices = bluetooth.discover_devices(lookup_names=True)
    for addr, name in nearby_devices:
        listbox.insert(END,"  %s" % (addr))


#A method that selects a single set in a listbox
def CurSelet(event):
    widget = event.widget
    selection=widget.curselection()
    picked = widget.get(selection[0])
    nameVar.set(picked)

#bind the listbox selections to the root window 
root.bind('<<ListboxSelect>>',CurSelet)
#Bluetooth Scan Buttton 
d = Button(text="Scan",command=bluetoothscan).grid(row=19,column=5)
root.geometry('500x800')
#Update Records to Database 
db.commit()

#render objects and widgets created and render them to the screen
root.mainloop()
