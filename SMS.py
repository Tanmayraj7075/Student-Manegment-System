from tkinter import *
import time
import ttkthemes
from tkinter import ttk, messagebox, filedialog
import pymysql
import pandas as pd




# Functionality Part

# Common Code for Add, Search, and Update Student Functionality Start ----------->
def toplevel_data(title, button_text, command):
    global idEntry, nameEntry, dobEntry, mobileEntry, addressEntry, screen
    screen = Toplevel()
    screen.title(title)
    screen.grab_set()
    screen.resizable(False, False)

    idLavel = Label(screen, text='Id', font=('times new roman', 20, 'bold'), fg="maroon")
    idLavel.grid(row=0, column=0, padx=30, pady=15, sticky=W)
    idEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, padx=10, pady=15)

    nameLavel = Label(screen, text='Name', font=('times new roman', 20, 'bold'), fg="maroon")
    nameLavel.grid(row=1, column=0, padx=30, pady=15, sticky=W)
    nameEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, padx=10, pady=15)

    dobLavel = Label(screen, text='D.O.B.', font=('times new roman', 20, 'bold'), fg="maroon")
    dobLavel.grid(row=2, column=0, padx=30, pady=15, sticky=W)
    dobEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    dobEntry.grid(row=2, column=1, padx=10, pady=15)

    mobileLavel = Label(screen, text='Mobile', font=('times new roman', 20, 'bold'), fg="maroon")
    mobileLavel.grid(row=3, column=0, padx=30, pady=15, sticky=W)
    mobileEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    mobileEntry.grid(row=3, column=1, padx=10, pady=15)

    addressLavel = Label(screen, text='Address', font=('times new roman', 20, 'bold'), fg="maroon")
    addressLavel.grid(row=4, column=0, padx=30, pady=15, sticky=W)
    addressEntry = Entry(screen, font=('roman', 15, 'bold'), width=24)
    addressEntry.grid(row=4, column=1, padx=10, pady=15)

    student_buttton = ttk.Button(screen, text=button_text, command=command)
    student_buttton.grid(row=5, columnspan=2, pady=15)


    # It is for Update Student Functionality specially
    if title=='Update Student':
        indexing = studentTable.focus()

        if indexing == '':
            messagebox.showerror('Error', 'Please select a student first')
            screen.destroy()
            return

        content = studentTable.item(indexing)
        listdata = content['values']

        if len(listdata) == 0:
            messagebox.showerror('Error', 'Please select a valid student')
            screen.destroy()
            return

        idEntry.insert(0, listdata[0])
        nameEntry.insert(0, listdata[1])
        dobEntry.insert(0, listdata[2])
        mobileEntry.insert(0, listdata[3])
        addressEntry.insert(0, listdata[4])

# Common Code for Add, Search, and Update Student Functionality END ----------->





# BOX - 4

# Add Student Functionality Start ------->

def add_data():
    if idEntry.get()=='' or nameEntry.get()=='' or dobEntry.get()=='' or mobileEntry.get()=='' or addressEntry.get()=='':
        messagebox.showerror('Error', 'All Fields are Required', parent=screen)
    else:
        try:
            query = 'insert into student values(%s, %s, %s, %s, %s, %s, %s)'
            mycursor.execute(query, (idEntry.get(), nameEntry.get(), dobEntry.get(), mobileEntry.get(), addressEntry.get(), date, currenttime))
            con.commit()
            result = messagebox.askyesno('Confirm', 'Data added successfully. Do you want to clean the form?')
            if result:
                idEntry.delete(0, END)
                nameEntry.delete(0, END)
                dobEntry.delete(0, END)
                mobileEntry.delete(0, END)
                addressEntry.delete(0, END)
            else:
                pass

        except:
            messagebox.showerror('Error', 'Id cannot be repeated', parent=screen)
            return
        

        # Show the data in box number 05
        query = 'select *from student'
        mycursor.execute(query)
        fetched_data = mycursor.fetchall()
        studentTable.delete(*studentTable.get_children())
        for data in fetched_data:
            studentTable.insert('', END, values=data)

# Add Student Functionality END ------->






# Search Student Functionality Start ------->

def search_data():
    query = 'select *from student where id=%s or name=%s or dob=%s or mobile=%s or address=%s'
    mycursor.execute(query, (idEntry.get(), nameEntry.get(), dobEntry.get(), mobileEntry.get(), addressEntry.get()))
    studentTable.delete(*studentTable.get_children())
    fetched_data = mycursor.fetchall()
    for data in fetched_data:
        studentTable.insert('', END, values=data)

# Search Student Functionality END ------->






# Delete Student Functionality Start ------->

def delete_student():
    indexing = studentTable.focus()

    if indexing == '':
        messagebox.showwarning('Warning', 'Please select at least one student record')
        return
    
    content = studentTable.item(indexing)
    content_id=content['values'][0]

    query='delete from student where id=%s'
    mycursor.execute(query, content_id)
    con.commit()

    messagebox.showinfo('Deleted', f'ID {content_id} is deleted successfully')

    show_student()

# Delete Student Functionality END ------->






# Update Student Functionality Start ------->

def update_data():
    query='update student set name=%s, dob=%s, mobile=%s, address=%s, date=%s, time=%s where id=%s'
    mycursor.execute(query, (nameEntry.get(), dobEntry.get(), mobileEntry.get(), addressEntry.get(), date, currenttime, idEntry.get()))
    con.commit()
    messagebox.showinfo('Updated', f'ID {idEntry.get()} is updated successfully', parent=screen)
    screen.destroy()
    show_student()

# Update Student Functionality END --->





# Show Student Functionality Start ------->

def show_student(): 
    query='select *from student'
    mycursor.execute(query)
    fetched_data=mycursor.fetchall()
    studentTable.delete(*studentTable.get_children())
    for data in fetched_data:
        studentTable.insert('', END, values=data)

# Show Student Functionality END ------->







# Export Student Data Functionality Start ------->

def export_data():
    indexing=studentTable.get_children()

    if len(indexing) == 0:
        messagebox.showwarning('Warning', 'Please show at least one record before exporting')
        return

    url=filedialog.asksaveasfilename(defaultextension='.csv')
    
    if url == '':
        return

    newlist=[]

    for index in indexing:
        content=studentTable.item(index)
        datalist=content['values']
        newlist.append(datalist)
    
    table=pd.DataFrame(newlist, columns=['ID', 'Name', 'D.O.B.', 'Mobile', 'Address', 'Add Date', 'Add Time'])
    table.to_csv(url, index=False)
    messagebox.showinfo('Success', 'Data is saved successfully')

# Export Student Data Functionality END ------->









# Exit Button Functionality Start ------->

def iexit():
    result=messagebox.askyesno('Confirm', 'Do you want to exit?')
    if result:
        root.destroy()
    else:
        pass

# Exit Button Functionality Start ------->

        



# For connect button to connect the database
def connect_database():
    # For connect from database
    def connect():
        global con, mycursor
        try:
            # HostName = localhost
            # UserName = root
            # Password = 8172
            # this line use for write the host name, username, and also password
            # con=pymysql.connect(host=hostEntry.get(), user=userEntry.get(), password=passwordEntry.get())

            # when this line use don't need to write hostname and username, simply use password and connect the database
            con=pymysql.connect(host='localhost', user='root', password='8172')
            mycursor=con.cursor()

        except:
            messagebox.showerror("Error", "Invalid Details", parent=connectWindow)
            return

        try:
            # Create DataBase
            query='create database studentmanagementsystem'
            mycursor.execute(query)

            # Create Table
            query='use studentmanagementsystem'
            mycursor.execute(query)
            query="""CREATE TABLE student(
                id INT PRIMARY KEY,
                name VARCHAR(30),
                dob VARCHAR(80),
                mobile VARCHAR(15),
                address VARCHAR(100),
                date VARCHAR(50),
                time VARCHAR(50))"""
            mycursor.execute(query)

        except:
            query = 'use studentmanagementsystem'
            mycursor.execute(query)

        # messagebox.showinfo('Success', 'Database Connected', parent=connectWindow)
        connectWindow.destroy()
        addstudentButton.config(state=NORMAL)
        searchstudentButton.config(state=NORMAL)
        deletestudentButton.config(state=NORMAL)
        updatestudentButton.config(state=NORMAL)
        showstudentButton.config(state=NORMAL)
        exportdataButton.config(state=NORMAL)
        exitButton.config(state=NORMAL)



    connectWindow = Toplevel()
    connectWindow.grab_set()
    connectWindow.geometry('470x250+730+230')
    connectWindow.title('Database Connection')
    connectWindow.resizable(False, False)

    
    # Connection Window Start ------------>

    # Host Name
    hostnameLabel = Label(connectWindow, text='Hostname', font=('arial', 20, 'bold'), fg="maroon")
    hostnameLabel.grid(row=0, column=0, padx=20)

    hostEntry=Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    hostEntry.grid(row=0, column=1, padx=40, pady=20)


    # User_Name
    usernameLabel = Label(connectWindow, text='UserName', font=('arial', 20, 'bold'), fg="maroon")
    usernameLabel.grid(row=1, column=0, padx=20)

    userEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    userEntry.grid(row=1, column=1, padx=40, pady=20)


    # Password
    passwordLabel = Label(connectWindow, text='Password', font=('arial', 20, 'bold'), fg="maroon")
    passwordLabel.grid(row=2, column=0, padx=20)

    passwordEntry = Entry(connectWindow, font=('roman', 15, 'bold'), bd=2)
    passwordEntry.grid(row=2, column=1, padx=40, pady=20)

    # For Connect Button
    connectButton = ttk.Button(connectWindow, text='Connect', command=connect)
    connectButton.grid(row=3, columnspan=2)

    # Connection Window End ------------>




# 1st Box
# Show of Date and Time
def clock():
    global date, currenttime
    date = time.strftime("%d:%m:%Y ")
    currenttime = time.strftime("%H:%M:%S")
    datetimeLabel.config(text=f'     Date: {date} \nTime:{currenttime}')
    datetimeLabel.after(1000, clock)


# This is For 2nd
count=0
text=''
def slider():
    global text,count
    if count==len(s):
        count=0
        text=''
    text = text+s[count]
    sliderLabel.config(text=text)
    count+=1
    sliderLabel.after(200,slider)


# GUI part
root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')

root.geometry('1150x700+0+0')
root.title('Student Management System')
root.resizable(False, False)




# 1st Box - Time and Date
datetimeLabel = Label(root, font=('times new roman', 18, 'bold'), fg="maroon")
datetimeLabel.place(x=5, y=5)
clock()




# 2nd Box - Heading
s='Student Management System'
sliderLabel = Label(root, font=('arial', 28, 'italic bold'), fg="maroon", width=30)
sliderLabel.place(x=220, y=0)
slider()




# 3rd Box - Connection
connectButton = ttk.Button(root, text='Connect Database', command=connect_database)
connectButton.place(x=980, y=0)
# Local Host = localhost
# User_Name = root
# Password = 8172




# 4th Box - Function
leftFrame = Frame(root)
leftFrame.place(x=50, y=80, width=300, height=600)

logo_image = PhotoImage(file='student.png')
logo_label = Label(leftFrame, image=logo_image)
logo_label.grid(row=0, column=0)

addstudentButton = ttk.Button(leftFrame, text='Add Student', width=25, state=DISABLED, command=lambda: toplevel_data('Add Student', 'Add', add_data))
addstudentButton.grid(row=1, column=0, pady=20)

searchstudentButton = ttk.Button(leftFrame, text='Search Student', width=25, state=DISABLED, command=lambda: toplevel_data('Search Student', 'Search', search_data))
searchstudentButton.grid(row=2, column=0, pady=20)

deletestudentButton = ttk.Button(leftFrame, text='Delete Student', width=25, state=DISABLED, command=delete_student)
deletestudentButton.grid(row=3, column=0, pady=20)

updatestudentButton = ttk.Button(leftFrame, text='Update Student', width=25, state=DISABLED, command=lambda: toplevel_data('Update Student', 'Update', update_data))
updatestudentButton.grid(row=4, column=0, pady=20)

showstudentButton = ttk.Button(leftFrame, text='Show Student', width=25, state=DISABLED, command=show_student)
showstudentButton.grid(row=5, column=0, pady=20)

exportdataButton = ttk.Button(leftFrame, text='Export Data', width=25, state=DISABLED, command=export_data)
exportdataButton.grid(row=6, column=0, pady=20)

exitButton = ttk.Button(leftFrame, text='Exit', width=25, state=DISABLED, command=iexit)
exitButton.grid(row=7, column=0, pady=20)




# 5th - DataBase
rightFrame = Frame(root)
rightFrame.place(x=350, y=80, width=790, height=600)

scrollBarX = Scrollbar(rightFrame, orient=HORIZONTAL)
scrollBarY = Scrollbar(rightFrame, orient=VERTICAL)

studentTable = ttk.Treeview(rightFrame,
             columns=('ID', 'Name', 'D.O.B.', 'Mobile', 'Address', 'Add Date', 'Add Time'),
                            xscrollcommand=scrollBarX.set, yscrollcommand=scrollBarY.set)
             # show='tree', selectmode='extended',)

scrollBarX.config(command=studentTable.xview)
scrollBarY.config(command=studentTable.yview)

scrollBarX.pack(side=BOTTOM, fill=X)
scrollBarY.pack(side=RIGHT, fill=Y)

studentTable.pack(fill='both', expand=1)

studentTable.heading('ID', text='ID')
studentTable.heading('Name', text='Name')
studentTable.heading('D.O.B.', text='D.O.B.')
studentTable.heading('Mobile', text='Mobile')
studentTable.heading('Address', text='Address')
studentTable.heading('Add Date', text='Add Date')
studentTable.heading('Add Time', text='Add Time')

studentTable.column('ID', width=60, anchor=CENTER)
studentTable.column('Name', width=300, anchor=CENTER)
studentTable.column('D.O.B.', width=150, anchor=CENTER)
studentTable.column('Mobile', width=200, anchor=CENTER)
studentTable.column('Address', width=300, anchor=CENTER)
studentTable.column('Add Date', width=200, anchor=CENTER)
studentTable.column('Add Time', width=200, anchor=CENTER)

style = ttk.Style()

style.configure('Treeview', rowheight=40, font=('arial', 12, 'bold'), foreground='#5a6b6b', background="#bfd4ed", fieldbackground="#fff5eb")
style.configure('Treeview.Heading', font=('arial', 14, 'bold'), foreground='#094a85', background="#bfd4ed")

studentTable.config(show='headings')



# For OutPut
root.mainloop()