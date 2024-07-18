from customtkinter import *
from PIL import Image

window = CTk()
window.resizable(False,False)
window.geometry("1300x778")
window.title("Employee management system")
logo = CTkImage(Image.open("resources/cover7.jpg"),size=(1300,230))
logoLabel = CTkLabel(window, image=logo,text="")
logoLabel.grid(row=0,column=0)



window.mainloop()
