from tkinter import *
from tkinter import messagebox
import ast

# Function to switch to the Signup page
def switch_to_signup():
    root.withdraw()  # Hide the login window
    window.deiconify()  # Show the signup window

# Function to switch to the Login page
def switch_to_login():
    window.withdraw()  # Hide the signup window
    root.deiconify()  # Show the login window

# Login Function
def signin():
    username = user.get()
    password = code.get()

    try:
        # Read the stored data from the file
        with open(r'C:\Users\hetva\Downloads\dataseet.txt', 'r') as file:
            data = file.read()
            users = ast.literal_eval(data)  # Convert string to dictionary

        # Check if the username and password match
        if username in users and users[username] == password:
            messagebox.showinfo("Login", "Login Successful!")
            # Open a new window or perform further actions
            screen = Toplevel(root)
            screen.title("App")
            screen.geometry('925x500+300+200')
            screen.config(bg="white")
            Label(screen, text='Hello Everyone!', bg='#fff', font=('Calibri(Body)', 50, 'bold')).pack(expand=True)
        else:
            messagebox.showerror("Invalid", "Invalid username or password!")
    except FileNotFoundError:
        messagebox.showerror("Error", "No user data found. Please sign up first.")

# Signup Function
def signup():
    username = user_signup.get()
    password = code_signup.get()
    conform_password = conform_code_signup.get()

    if password == conform_password:
        try:
            # Read existing data
            with open(r'C:\Users\hetva\Downloads\dataseet.txt', 'r') as file:
                data = file.read()
                users = ast.literal_eval(data)
        except FileNotFoundError:
            # If the file doesn't exist, create an empty dictionary
            users = {}

        # Check if the username already exists
        if username in users:
            messagebox.showerror("Error", "Username already exists!")
        else:
            # Add the new user to the dictionary
            users[username] = password

            # Write the updated dictionary back to the file
            with open(r'C:\Users\hetva\Downloads\dataseet.txt', 'w') as file:
                file.write(str(users))

            messagebox.showinfo("Ragistration", "Successfully signed up!")
            switch_to_login()  # Switch to the login page after successful signup
    else:
        messagebox.showerror("Invalid", "Both passwords should match")

# Login Page
root = Tk()
root.title('Login')
root.geometry('925x500+300+200')
root.configure(bg='#fff')
root.resizable(False, False)

img = PhotoImage(file=r"C:\Users\hetva\Downloads\login.png")
Label(root, image=img, bg='white').place(x=50, y=50)

frame = Frame(root, width=350, height=350, bg="white")
frame.place(x=480, y=70)

heading = Label(frame, text='Login', fg='#57a1f8', bg='white', font=('Microsoft Yahei UI Light', 30, 'bold'))
heading.place(x=100, y=7)

# Username Entry
user = Entry(frame, width=35, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
user.place(x=30, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', lambda e: user.delete(0, 'end'))
user.bind('<FocusOut>', lambda e: user.insert(0, 'Username') if user.get() == '' else None)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

# Password Entry
code = Entry(frame, width=35, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
code.place(x=30, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', lambda e: code.delete(0, 'end'))
code.bind('<FocusOut>', lambda e: code.insert(0, 'Password') if code.get() == '' else None)

Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

# Login Button
Button(frame, width=30, pady=7, text='Login', bg='#57a1f8', fg='white', border=0, command=signin).place(x=35, y=204)

# Ragistration Link
label = Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label.place(x=70, y=270)

sign_up = Button(frame, width=10, text="Ragistration", border=0, bg='white', cursor='hand2', fg='#57a1f8', command=switch_to_signup)
sign_up.place(x=215, y=263)

# Ragistration Page
window = Toplevel(root)
window.title('Ragistration')
window.geometry('925x500+300+200')
window.configure(bg='#fff')
window.resizable(False, False)
window.withdraw()  # Hide the signup window initially

img_signup = PhotoImage(file=r"C:\Users\hetva\Downloads\register.png")
Label(window, image=img_signup, bg='white').place(x=50, y=100)

frame_signup = Frame(window, width=350, height=390, bg="white")
frame_signup.place(x=480, y=50)

heading_signup = Label(frame_signup, text='Sign up', fg='#57a1f8', bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
heading_signup.place(x=120, y=5)

# Username Entry (Signup)
user_signup = Entry(frame_signup, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
user_signup.place(x=30, y=80)
user_signup.insert(0, 'Username')
user_signup.bind('<FocusIn>', lambda e: user_signup.delete(0, 'end'))
user_signup.bind('<FocusOut>', lambda e: user_signup.insert(0, 'Username') if user_signup.get() == '' else None)

Frame(frame_signup, width=295, height=2, bg='black').place(x=25, y=107)

# Password Entry (Signup)
code_signup = Entry(frame_signup, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
code_signup.place(x=30, y=150)
code_signup.insert(0, 'Password')
code_signup.bind('<FocusIn>', lambda e: code_signup.delete(0, 'end'))
code_signup.bind('<FocusOut>', lambda e: code_signup.insert(0, 'Password') if code_signup.get() == '' else None)

Frame(frame_signup, width=295, height=2, bg='black').place(x=25, y=177)

# Confirm Password Entry (Signup)
conform_code_signup = Entry(frame_signup, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
conform_code_signup.place(x=30, y=220)
conform_code_signup.insert(0, 'Confirm Password')
conform_code_signup.bind('<FocusIn>', lambda e: conform_code_signup.delete(0, 'end'))
conform_code_signup.bind('<FocusOut>', lambda e: conform_code_signup.insert(0, 'Confirm Password') if conform_code_signup.get() == '' else None)

Frame(frame_signup, width=295, height=2, bg='black').place(x=25, y=247)

# Signup Button
Button(frame_signup, width=30, pady=7, text='Register', bg='#57a1f8', fg='white', border=0, command=signup).place(x=35, y=280)

# Login Link
label_signup = Label(frame_signup, text="I have an account", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
label_signup.place(x=90, y=340)

sign_in = Button(frame_signup, width=6, text="Login", border=0, bg='white', cursor='hand2', fg='#57a1f8', command=switch_to_login)
sign_in.place(x=200, y=333)

root.mainloop()