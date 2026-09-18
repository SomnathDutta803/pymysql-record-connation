
import pymysql

mycon = pymysql.connect(
    host="localhost",
    user="root",
    passwd="Abcd1234",
    database="nila",
    port=3310
)

try:
    id = input("Enter ID for updating: ")

    cursor = mycon.cursor()

    cursor.execute(
        "SELECT * FROM Emp_details WHERE id = %s",
        (id,)
    )

    result = cursor.fetchone()

    if result:
        print("\nExisting Record:")
        print(f"ID: {result[0]}")
        print(f"Name: {result[1]}")
        print(f"Department: {result[2]}")
        print(f"Salary: {result[3]}")
        print(f"Gender: {result[4]}")
        print(f"Age: {result[5]}")
        print(f"City: {result[6]}")

        print("\nWhich fields do you want to update?")
        print("Name (1)")
        print("Department (2)")
        print("Salary (3)")
        print("Gender (4)")
        print("Age (5)")
        print("City (6)")

        choices = input(
            "Enter choices separated by space: "
        ).split()

        fields = {
            '1': ('name', "Enter new Name: "),
            '2': ('department', "Enter new Department: "),
            '3': ('salary', "Enter new Salary: "),
            '4': ('gender', "Enter new Gender: "),
            '5': ('age', "Enter new Age: "),
            '6': ('city', "Enter new City: ")
        }

        query_fields = []
        params = []

        if not choices or any(c not in fields for c in choices):
            print("Invalid choice!")

        elif len(set(choices)) != len(choices):
            print("Duplicate choices are not allowed!")

        else:
            for c in choices:
                field, message = fields[c]
                value = input(message)

                if field in ('salary', 'age'):
                    value = int(value)

                query_fields.append(f"{field} = %s")
                params.append(value)

            sql = (
                "UPDATE Emp_details SET "
                + ", ".join(query_fields)
                + " WHERE id = %s"
            )

            params.append(id)

            confirm = input(
                "Confirm Update? (y/n): "
            )

            if confirm.lower() == 'y':
                cursor.execute(sql, tuple(params))
                mycon.commit()

                cursor.execute(
                    "SELECT * FROM Emp_details WHERE id = %s",
                    (id,)
                )

                result = cursor.fetchone()

                print("\nRecord Updated Successfully!")

                print(f"ID: {result[0]}")
                print(f"Name: {result[1]}")
                print(f"Department: {result[2]}")
                print(f"Salary: {result[3]}")
                print(f"Gender: {result[4]}")
                print(f"Age: {result[5]}")
                print(f"City: {result[6]}")

            else:
                print("Update cancelled!")

    else:
        print("\nNo record found for this ID!")

except pymysql.Error as e:
    print("Database Error:", e)
    mycon.rollback()

except ValueError:
    print("Please enter valid numbers for salary and age.")

finally:
    mycon.close()