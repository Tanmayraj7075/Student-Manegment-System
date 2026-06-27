from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk



# Code run karne ke liye terminal me "python login.py" likhna hoga



def login():
    if usernameEntry.get() == "" or passwordEntry.get() == "":
        messagebox.showerror("Error", "Please enter both username and password")

    elif usernameEntry.get() == '8172' and passwordEntry.get() == '8172':
        # messagebox.showinfo("Success", "Welcome")
        window.destroy()
        import SMS

    else:
        messagebox.showerror('Error', 'Please enter correct information')

window = Tk()

window.geometry('1530x790+0+0')
window.title('Login of Student Management System')

window.resizable(False, False)


# Add BackGround Image
# Image load and resize
img = Image.open("bg.jpg")
img = img.resize((1530, 790))

backgroundImage = ImageTk.PhotoImage(img)

# backgroundImage = ImageTk.PhotoImage(file='bg2.jpg')

bgLabel=Label(window, image=backgroundImage)
bgLabel.place(x=0, y=0)

# Add frame on Page
loginFrame=Frame(window, bg="#ffffff")
loginFrame.place(x=0, y=0)
loginFrame.place(x=750, y=150)

logoImage = PhotoImage(file='logo.png')
logoLabel=Label(loginFrame, image=logoImage)
logoLabel.grid(row=0, column=0, columnspan=2, pady=10)


# UserName

usernameImage = PhotoImage(file='user.png')
usernameLabel = Label(loginFrame, image=usernameImage, text='Username', compound=LEFT,
                      font=('times new roman', 20, 'bold'), bg='white')
usernameLabel.grid(row=1, column=0, pady=10, padx=10)

usernameEntry = Entry(loginFrame, font=('times new roman', 20, 'bold'), bd=5,
                      fg='royalblue')
usernameEntry.grid(row=1, column=1, pady=10, padx=10)


# PassWord

passwordImage = PhotoImage(file='pw.png')
passwordLabel = Label(loginFrame, image=passwordImage, text='PassWord', compound=LEFT,
                      font=('times new roman', 20, 'bold'), bg='white')
passwordLabel.grid(row=2, column=0, pady=10, padx=10)

passwordEntry = Entry(loginFrame, font=('times new roman', 20, 'bold'), bd=5,
                      fg='royalblue')
passwordEntry.grid(row=2, column=1, pady=10, padx=10)

# Login Button
loginButton=Button(loginFrame, text='Login', font=('times new roman', 14, 'bold'), width=15,
                   fg='white', bg='cornflowerblue', activebackground='cornflowerblue',
                   activeforeground='white', cursor='hand2', command=login)
loginButton.grid(row=3, column=1, pady=10, padx=10)


window.mainloop()






























