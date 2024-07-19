import pymysql
from tkinter import messagebox

def connect_database():
    try:
        conn = pymysql.connect(
                            host = "localhost",
                            user = "root",
                            password = "Mike2024"
                            )
        myCursor = conn.cursor()
    except:
        messagebox.showerror("Error","Something went wrong")
        return
    
    myCursor.execute("CREATE DATABASE IF NOT EXISTS employee_data")
    myCursor.execute("USE employee_data")
    myCursor.execute("CREATE TABLE IF NOT EXISTS data (Id VARCHAR(20),Name VARCHAR(50),Phone VARCHAR(40),Role VARCHAR(60),Gender VARCHAR(20),Salary DECIMAL(10,2))")



def insert(id,name,phone,role,gender,salary):
    print(id,name,phone,role,gender,salary)

connect_database()