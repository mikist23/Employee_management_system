from customtkinter import *
from PIL import Image

root = CTk()
root.resizable(0,0)
root.geometry("1300x778")
root.title("Login page")

image = CTkImage(Image.open("resources/cover5.jpg"), size=(1300,778))
imageLabel = CTkLabel(root,image=image, text="")
imageLabel.place(x=0,y=0)

headingLabel = CTkLabel(root,text="Employee Management System")
headingLabel.place(x=20,y=100)

root.mainloop()