import pymysql
from tkinter import messagebox


# *********************Creating a databse connection*************************
def connect_database():
    global myCursor,conn
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


#************************Inserting data to the database***********************
def insert(id,name,phone,role,gender,salary):
    myCursor.execute("INSERT INTO data VALUES (%s,%s,%s,%s,%s,%s)",(id,name,phone,role,gender,salary))
    conn.commit()

#************************Check if Id exists**********************
def id_exists(id):
    myCursor.execute("SELECT COUNT(*) FROM data WHERE id=%s",id)
    result = myCursor.fetchone()
    return result[0]>0


# *********************Fetch Employees**************************
def fetch_employees():
    myCursor.execute("SELECT * FROM data")
    result = myCursor.fetchall()
    return result

# *********************Update Employee**************************
def update(id,new_name,new_phone,new_role,new_gender,new_salary):
    myCursor.execute("UPDATE data SET name=%s,phone=%s,role=%s,gender=%s,salary=%s WHERE id=%s",(new_name,new_phone,new_role,new_gender,new_salary,id))
    conn.commit()
    


# *********************Delete Employee **************************
def delete(id):
    myCursor.execute("DELETE FROM data WHERE id=%s",(id,))
    conn.commit()


# *********************Search Employee **************************
def search(option,value):
    myCursor.execute(f"SELECT * FROM data WHERE {option}=%s",value)
    result = myCursor.fetchall()
    return result

connect_database()