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
    cursor = mycon.cursor()

    while True:
        print("\n===== EMPLOYEE MANAGEMENT SYSTEM =====")
        print("1. Insert Employee")
        print("2. Display All Employees")
        print("3. Search by Department")
        print("4. Update Employee")
        print("5. Average Salary by Department")
        print("6. Exit")

        choice = input("Enter your choice: ")

        # INSERT EMPLOYEE
        if choice == '1':
            id = int(input("Enter ID: "))
            name = input("Enter Name: ")
            department = input("Enter Department: ")
            salary = int(input("Enter Salary: "))
            gender = input("Enter Gender: ")
            age = int(input("Enter Age: "))
            city = input("Enter City: ")

            cursor.execute(
                "SELECT id FROM Emp_details WHERE id = %s",
                (id,)
            )

            result = cursor.fetchone()

            if result:
                print("ID already exists! Cannot insert.")

            else:
                cursor.execute(
                    """INSERT INTO Emp_details
                    VALUES (%s, %s, %s, %s, %s, %s, %s)""",
                    (id, name, department, salary, gender, age, city)
                )

                mycon.commit()
                print("Employee inserted successfully!")

        # DISPLAY ALL EMPLOYEES
        elif choice == '2':
            cursor.execute("SELECT * FROM Emp_details")

            result = cursor.fetchall()

            for row in result:
                print(row)

        # SEARCH BY DEPARTMENT
        elif choice == '3':
            department = input("Enter Department: ")

            cursor.execute(
                """SELECT name, age, department
                FROM Emp_details
                WHERE department = %s""",
                (department,)
            )

            result = cursor.fetchall()

            if result:
                for row in result:
                    print(row)
            else:
                print("No employee found!")

        # UPDATE EMPLOYEE
        elif choice == '4':
            id = int(input("Enter Employee ID: "))

            cursor.execute(
                "SELECT * FROM Emp_details WHERE id = %s",
                (id,)
            )

            result = cursor.fetchone()

            if result:
                print("Existing Record:", result)

                field = input(
                    "Update Name (n), Salary (s), "
                    "Department (d): "
                )

                if field == 'n':
                    name = input("Enter New Name: ")

                    cursor.execute(
                        "UPDATE Emp_details SET name = %s WHERE id = %s",
                        (name, id)
                    )

                elif field == 's':
                    salary = int(input("Enter New Salary: "))

                    cursor.execute(
                        "UPDATE Emp_details SET salary = %s WHERE id = %s",
                        (salary, id)
                    )

                elif field == 'd':
                    department = input("Enter New Department: ")

                    cursor.execute(
                        "UPDATE Emp_details SET department = %s WHERE id = %s",
                        (department, id)
                    )

                else:
                    print("Invalid choice!")
                    continue

                mycon.commit()
                print("Employee updated successfully!")

            else:
                print("Employee ID not found!")

        # AVERAGE SALARY BY DEPARTMENT
        elif choice == '5':
            cursor.execute(
                """SELECT department, AVG(salary), AVG(age)
                FROM Emp_details
                GROUP BY department"""
            )

            result = cursor.fetchall()

            for row in result:
                print(row)

        # EXIT
        elif choice == '6':
            print("Thank you!")
            break

        else:
            print("Invalid choice! Try again.")

except pymysql.Error as e:
    print("Database Error:", e)
    mycon.rollback()

except ValueError:
    print("Please enter valid numeric values.")

finally:
    mycon.close()