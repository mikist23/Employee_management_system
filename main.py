from customtkinter import *
from PIL import Image
from tkinter import messagebox

root = CTk()
root.resizable(0,0)
root.geometry("1300x778")
root.title("Login page")

def login():
    if usernameEntry.get() == "" or  passwordEntry.get == "":
        messagebox.showerror("Error","All fields are required")
    elif usernameEntry.get() == "mike" and passwordEntry.get() == "1234":
        messagebox.showinfo("Success", "Login successful")
    else:
        messagebox.showerror("Error","Wrong credentials")





image = CTkImage(Image.open("resources/cover5.jpg"), size=(1300,778))
imageLabel = CTkLabel(root,image=image, text="")
imageLabel.place(x=0,y=0)

headingLabel = CTkLabel(root,text="Employee Management System",bg_color="#3498eb",font=("Goudy Old Style",40,"bold"))
headingLabel.place(x=550,y=10)

usernameEntry = CTkEntry(root,placeholder_text="Enter your username", width=280,height=40,
                        corner_radius=10, bg_color="#3498eb",
                        font=("Arial", 14),)
usernameEntry.place(x=20,y=260)

passwordEntry = CTkEntry(root,placeholder_text="Enter your password", width=280,height=40,
                        corner_radius=10, bg_color="#3498eb",
                        font=("Arial", 14),show="*")
passwordEntry.place(x=20,y=310)

loginButton = CTkButton(root,text="Login",height=40,
                        corner_radius=10,bg_color="#3498eb",
                        font=("Arial", 14),fg_color="#4CAF50", 
                        hover_color="#45A049",cursor = "hand2",command=login) 
loginButton.place(x=80,y=360)

root.mainloop()