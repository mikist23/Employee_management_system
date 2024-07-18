from customtkinter import *
from PIL import Image

window = CTk()
window.resizable(False,False)
window.geometry("1300x778")
window.configure(fg_color="#161C30")
window.title("Employee management system")
logo = CTkImage(Image.open("resources/cover7.jpg"),size=(1300,280))
logoLabel = CTkLabel(window, image=logo,text="")
logoLabel.grid(row=0,column=0,columnspan=2)



leftFrame = CTkFrame(window,fg_color="#161C30")
leftFrame.grid(row=1,column=0)


idLabel = CTkLabel(leftFrame,text="Id",font=("arial",18,"bold"))
idLabel.grid(row=0,column=0,padx=20,pady=15,sticky="w")

idEntry = CTkEntry(leftFrame,font=("arial",15,"bold"),width=200)
idEntry.grid(row=0,column=1)

nameLabel = CTkLabel(leftFrame,text="Name",font=("arial",18,"bold"))
nameLabel.grid(row=1,column=0,padx=20,pady=15,sticky="w")

nameEntry = CTkEntry(leftFrame,font=("arial",15,"bold"),width=200)
nameEntry.grid(row=1,column=1)

phoneLabel = CTkLabel(leftFrame,text="Phone",font=("arial",18,"bold"))
phoneLabel.grid(row=2,column=0,padx=20,pady=15,sticky="w")

phoneEntry = CTkEntry(leftFrame,font=("arial",15,"bold"),width=200)
phoneEntry.grid(row=2,column=1)


roleLabel = CTkLabel(leftFrame,text="Role",font=("arial",18,"bold"))
roleLabel.grid(row=3,column=0,padx=20,pady=15,sticky="w")

role_options = ["Web Developer", "UI Disigner", "UX Disigner", "ML Engineer", "Software Developer", 
                "Project Manager", "Product Manager", "Human Resource"]
roleBox= CTkComboBox(leftFrame,values=role_options,width=200,font=("arial",15,"bold"),state="readonly")
roleBox.grid(row=3,column=1,)
roleBox.set(role_options[0])


genderLabel = CTkLabel(leftFrame,text="Gender",font=("arial",18,"bold"))
genderLabel.grid(row=4,column=0,padx=20,pady=15,sticky="w")

gender_options = ["Male","Female"]
genderBox= CTkComboBox(leftFrame,values=gender_options,width=200,font=("arial",15,"bold"),state="readonly")
genderBox.grid(row=4,column=1,)
genderBox.set(gender_options[0])


salaryLabel = CTkLabel(leftFrame,text="Salary",font=("arial",18,"bold"))
salaryLabel.grid(row=5,column=0,padx=20,pady=15,sticky="w")

salaryEntry = CTkEntry(leftFrame,font=("arial",15,"bold"),width=200)
salaryEntry.grid(row=5,column=1)



rightFrame = CTkFrame(window)
rightFrame.grid(row=1,column=1)



window.mainloop()
