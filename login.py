from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk



# Code run karne ke liye terminal me "python login.py" likhna hoga


# Login Function Call
def login():
    if usernameEntry.get() == "" or passwordEntry.get() == "":
        messagebox.showerror("Error", "Please enter both username and password")

    elif usernameEntry.get() == '8172' and passwordEntry.get() == '8172':
        # messagebox.showinfo("Success", "Welcome")
        window.destroy()
        import SMS

    else:
        messagebox.showerror('Error', 'Please enter correct information')


# Window Import
window = Tk()

window.geometry('1530x790+0+0')
window.title('Login of Student Management System')

window.resizable(False, False)




# Add BackGround Image
# Image load and resize
img = Image.open("bg.jpg")
img = img.resize((1530, 790))

Image = ImageTk.PhotoImage(img)  # convert PIL image to Compatible image


bg=Label(window, image=Image)
bg.place(x=0, y=0)



# Add frame on Page
loginFrame=Frame(window, bg="#ffffff")
loginFrame.place(x=750, y=150)


# Add Logo Image
logoImage = PhotoImage(file='logo.png')
logoLabel=Label(loginFrame, image=logoImage)
logoLabel.grid(row=0, column=0, columnspan=2, pady=10)



# UserName --------------------------->
# Column 1
usernameImage = PhotoImage(file='user.png')
usernameLabel = Label(
    loginFrame, 
    image=usernameImage, 
    text='Username', 
    compound=LEFT,
    font=('times new roman', 20, 'bold'), bg='white'
)
usernameLabel.grid(row=1, column=0, pady=10, padx=10)

# Column 2
usernameEntry = Entry(
    loginFrame, 
    font=('times new roman', 20, 'bold'), 
    bd=5,
    fg='royalblue'
)
usernameEntry.grid(row=1, column=1, pady=10, padx=10)




# PassWord --------------------------->
# Column 1
passwordImage = PhotoImage(file='pw.png')
passwordLabel = Label(
    loginFrame, 
    image=passwordImage, 
    text='PassWord', 
    compound=LEFT,
    font=('times new roman', 20, 'bold'), 
    bg='white'
)
passwordLabel.grid(row=2, column=0, pady=10, padx=10)

# Column 2
passwordEntry = Entry(
    loginFrame,
    font=('times new roman', 20, 'bold'),
    bd=5,
    fg='royalblue'
)
passwordEntry.grid(row=2, column=1, pady=10, padx=10)




# Login Button ------------------------->
loginButton=Button(
    loginFrame,
    text='Login',
    font=('times new roman', 14, 'bold'),
    width=15,
    fg='Green',
    bg='pink',
    activebackground='cornflowerblue',
    activeforeground='white',
    cursor='hand2',
    command=login
)
loginButton.grid(row=3, column=0, columnspan=2, pady=10, padx=10)


# Show the window
window.mainloop()