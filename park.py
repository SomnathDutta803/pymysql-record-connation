import pandas as pd
import pymysql

mycon = pymysql.connect(
    host="localhost",
    user="root",
    passwd="Abcd1234",
    database="nila",
    port=3310
)

try:
    id = input("Enter id no: ")
    name = input("Enter student name: ")
    department = input("Enter department: ")
    salary = int(input("Enter salary: "))
    gender = input("Enter gender: ")
    age = int(input("Enter age: "))
    city = input("Enter city: ")

    cursor = mycon.cursor()

    cursor.execute(
        "INSERT INTO Emp_details VALUES (%s, %s, %s, %s, %s, %s, %s)",
        (id, name, department, salary, gender, age, city)
    )

    mycon.commit()

    print(f"Record Inserted: {id}, {name}, {department}, {salary}, {gender}, {age}, {city}")

except pymysql.Error as e:
    print("Error:", e)
    mycon.rollback()

finally:
    mycon.close()