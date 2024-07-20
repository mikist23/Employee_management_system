from customtkinter import *
from PIL import Image
from tkinter import ttk,messagebox
import database


# *********************Functions **************************


# *********************Delete_All Employee **************************
def delete_all_employee():
    result = messagebox.askyesno("Confirm",'Do you really want to delete all the records?')
    if result:
        database.delete_all_employees()
    else:
        messagebox.showinfo('Cancelled', "Delete operation cancelled")


# *********************Show_all Employee **************************
def showall_employee():
    treeview_data()
    searchEntry.delete(0,END)
    searchBox.set("Search By")



# *********************Search Employee **************************
def search_employee():
    if searchEntry.get()=="":
        messagebox.showerror("Error","Enter value to search")
    elif searchBox.get()=="":
        messagebox.showerror("Error","Please select an option")
    else:
        searched_data = database.search(searchBox.get(),searchEntry.get())
        tree.delete(*tree.get_children())
        for employee in searched_data:
            tree.insert("",END,values=employee)



# *********************Delete Employee **************************
def delete_employee():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror('Error', "Select data to delete")
    else:
        confirm = messagebox.askyesno('Confirm Delete', 'Are you sure you want to delete this employee?')
        if confirm:
            database.delete(idEntry.get())
            treeview_data()
            clear()
            messagebox.showinfo('Success', "Data deleted successfully")
        else:
            messagebox.showinfo('Cancelled', "Delete operation cancelled")


# *********************Update Employee**************************
def update_employee():
    selected_item = tree.selection()
    if not selected_item:
        messagebox.showerror("Error","Select data to update")
    else:
        database.update(idEntry.get(),nameEntry.get(),phoneEntry.get(),roleBox.get(),genderBox.get(),salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo("Success","Data updated successful")


# *********************Row data selection**************************
def selection(event):
    selected_item = tree.selection()
    if selected_item:
        row =tree.item(selected_item)["values"]
        clear()
        idEntry.insert(0,row[0])
        nameEntry.insert(0,row[1])
        phoneEntry.insert(0,row[2])
        roleBox.set(row[3])
        genderBox.set(row[4])
        salaryEntry.insert(0,row[5])
    



# *********************Reseting the fields**************************
def clear(value=False):
    if value:
        tree.selection_remove(tree.focus())
    idEntry.delete(0,END)
    nameEntry.delete(0,END)
    phoneEntry.delete(0,END)
    roleBox.set("Web Developer")
    genderBox.set("Male")
    salaryEntry.delete(0,END)

# *********************Fetch Employees**************************
def treeview_data():
    employees = database.fetch_employees()
    tree.delete(*tree.get_children())
    for employee in employees:
        tree.insert("",END,values=employee)

# *********************Add Employee **************************
def add_employee():
    if idEntry.get()==""or phoneEntry.get()=="" or nameEntry.get()==""or salaryEntry.get()=="":
        messagebox.showerror("Error","All Fields Are required ")
    elif database.id_exists(idEntry.get()):
        messagebox.showerror('Error',"Id already exists")
    elif not idEntry.get().startswith("EMP"):
        messagebox.showerror('Error',"Invalid id formart! Use 'EMP' followed by a number (ie EMP1...)")
    else:
        database.insert(idEntry.get(),nameEntry.get(),phoneEntry.get(),roleBox.get(),genderBox.get(),salaryEntry.get())
        treeview_data()
        clear()
        messagebox.showinfo("Success","Record is adedd successful")




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

rightFrame = CTkFrame(window,)
rightFrame.grid(row=1,column=1)



search_options = ["Id","Name","Phone","Role","Gender","Salary"]
searchBox= CTkComboBox(rightFrame,values=search_options,state="readonly")
searchBox.grid(row=0,column=0,)
searchBox.set("Search By")


searchEntry = CTkEntry(rightFrame,font=("arial",15,"bold"))
searchEntry.grid(row=0,column=1)


serchButton = CTkButton(rightFrame,text="Search",width=100,corner_radius=10,command=search_employee)
serchButton.grid(row=0,column=2)

show_allButton = CTkButton(rightFrame,text="Show All",width=100,corner_radius=10,command=showall_employee)
show_allButton.grid(row=0,column=3,pady=10)

tree = ttk.Treeview(rightFrame,)
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
style.configure("Treeview",font=("arial",15,"bold"),rowheight=30,foreground= "white",background="#161C30")

#Scroll Bar
scrollBar = ttk.Scrollbar(rightFrame,orient=VERTICAL,command=tree.yview)
scrollBar.grid(row=1,column=4,sticky="ns",padx=4)
tree.config(yscrollcommand=scrollBar.set)


# *********************Button frame **************************

buttonFrame = CTkFrame(window,fg_color="#161C30")
buttonFrame.grid(row=2,column=0,columnspan=2)

newButton = CTkButton(buttonFrame,text="New Employee",width=160,corner_radius=15,font=("arial",15,"bold"),command=lambda : clear(True))
newButton.grid(row=0,column=0,pady=10)

addButton = CTkButton(buttonFrame,text="Add Employee",width=160,corner_radius=15,font=("arial",15,"bold"),command=add_employee)
addButton.grid(row=0,column=1,pady=10,padx=5)

updateButton = CTkButton(buttonFrame,text="Update Employee",width=160,corner_radius=15,font=("arial",15,"bold"),command=update_employee)
updateButton.grid(row=0,column=2,pady=10,padx=5)

deleteButton = CTkButton(buttonFrame,text="Delete Employee",width=160,corner_radius=15,font=("arial",15,"bold"),command=delete_employee)
deleteButton.grid(row=0,column=3,pady=10,padx=5)

delete_allButton = CTkButton(buttonFrame,text="Delete All",width=160,corner_radius=15,font=("arial",15,"bold"),command=delete_all_employee)
delete_allButton.grid(row=0,column=4,pady=10,padx=5)



#Tree view  data update
treeview_data()

#Row Selection data
window.bind("<ButtonRelease>",selection)



window.mainloop()
