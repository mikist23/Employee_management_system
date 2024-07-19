from customtkinter import *
from PIL import Image
from tkinter import ttk



# *********************Gui part **************************
window = CTk()
window.resizable(False,False)
window.geometry("1300x778+100+100")
window.configure(fg_color="#161C30")
window.title("Employee management system")
logo = CTkImage(Image.open("resources/cover7.jpg"),size=(1300,280))
logoLabel = CTkLabel(window, image=logo,text="")
logoLabel.grid(row=0,column=0,columnspan=2)


# *********************Left frame **************************
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


# *********************Right frame **************************

rightFrame = CTkFrame(window)
rightFrame.grid(row=1,column=1)



search_options = ["Id","Name","Phone","Role","Gender","Salary"]
searchBox= CTkComboBox(rightFrame,values=search_options,state="readonly")
searchBox.grid(row=0,column=0,)
searchBox.set("Search By")


searchEntry = CTkEntry(rightFrame,font=("arial",15,"bold"))
searchEntry.grid(row=0,column=1)


serchButton = CTkButton(rightFrame,text="Search",width=100,corner_radius=10)
serchButton.grid(row=0,column=2)

show_allButton = CTkButton(rightFrame,text="Show All",width=100,corner_radius=10)
show_allButton.grid(row=0,column=3,pady=10)

tree = ttk.Treeview(rightFrame)
tree.grid(row=1,column=0,columnspan=4)

tree["columns"]=("Id","Name","Phone","Role","Gender","Salary")

tree.heading("Id",text="Id")
tree.heading("Name",text="Name")
tree.heading("Phone",text="Phone")
tree.heading("Role",text="Role")
tree.heading("Gender",text="Gender")
tree.heading("Salary",text="Salary")

#Remove extra empty column
tree.config(show="headings")

tree.column("Id",width=100)
tree.column("Name",width=170)
tree.column("Phone",width=170)
tree.column("Role",width=210)
tree.column("Gender",width=100)
tree.column("Salary",width=140)

#Styles
style = ttk.Style()
style.configure("Treeview.Heading",font=("arial",18,"bold"))



window.mainloop()
