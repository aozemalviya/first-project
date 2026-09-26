
import json
import os

FILE_NAME = "employees.json"


# -------------------------------
# LOAD EMPLOYEE DATA
# -------------------------------
def load_data():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []
# -------------------------------
# SAVE EMPLOYEE DATA
# -------------------------------
def save_data(employees):
    with open(FILE_NAME, "w") as file:
        json.dump(employees, file, indent=4)


# -------------------------------
# LOGIN MODULE
# -------------------------------
def login():
    print("\n================================")
    print(" EMPLOYEE PAYROLL")
    print("================================")

    username = input("Username: ")
    password = input("Password: ")

    if username == "admin" and password == "1234":
        print("\nLogin Successful!")
        return True
    else:
        print("\nInvalid Username or Password.")
        return False


# -------------------------------
# ADD EMPLOYEE
# -------------------------------
def add_employee(employees):

    print("\n---------- ADD EMPLOYEE ----------")

    emp_id = input("Enter Employee ID: ")

    # Check duplicate ID
    for emp in employees:
        if emp["id"] == emp_id:
            print("Employee ID already exists!")
            return

    name = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    designation = input("Enter Designation: ")

    while True:
        try:
            basic_salary = float(input("Enter Basic Salary: "))

            if basic_salary < 0:
                print("Salary cannot be negative.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    employee = {
        "id": emp_id,
        "name": name,
        "department": department,
        "designation": designation,
        "basic_salary": basic_salary,
        "working_days": 30,
        "present_days": 30
    }

    employees.append(employee)
    save_data(employees)

    print("\nEmployee added successfully!")


# -------------------------------
# VIEW EMPLOYEES
# -------------------------------
def view_employees(employees):

    print("\n---------- EMPLOYEE LIST ----------")

    if len(employees) == 0:
        print("No employees found.")
        return

    for emp in employees:
        print("--------------------------------")
        print("Employee ID :", emp["id"])
        print("Name :", emp["name"])
        print("Department :", emp["department"])
        print("Designation :", emp["designation"])
        print("Basic Salary:", emp["basic_salary"])


# -------------------------------
# SEARCH EMPLOYEE
# -------------------------------
def search_employee(employees):

    print("\n---------- SEARCH EMPLOYEE ----------")

    emp_id = input("Enter Employee ID: ")

    for emp in employees:
        if emp["id"] == emp_id:

            print("\nEmployee Found!")
            print("Employee ID :", emp["id"])
            print("Name :", emp["name"])
            print("Department :", emp["department"])
            print("Designation :", emp["designation"])
            print("Basic Salary:", emp["basic_salary"])

            return emp

    print("Employee not found.")
    return None


# -------------------------------
# DELETE EMPLOYEE
# -------------------------------
def delete_employee(employees):

    print("\n---------- DELETE EMPLOYEE ----------")

    emp_id = input("Enter Employee ID: ")

    for emp in employees:

        if emp["id"] == emp_id:

            employees.remove(emp)
            save_data(employees)

            print("Employee deleted successfully!")
            return

    print("Employee not found.")


# -------------------------------
# ATTENDANCE MANAGEMENT
# -------------------------------
def attendance(employees):

    print("\n---------- ATTENDANCE ----------")

    emp_id = input("Enter Employee ID: ")

    for emp in employees:

        if emp["id"] == emp_id:

            while True:
                try:
                    working_days = int(
                        input("Enter total working days: ")
                    )

                    present_days = int(
                        input("Enter present days: ")
                    )

                    if working_days <= 0:
                        print("Working days must be greater than 0.")
                        continue

                    if present_days < 0 or present_days > working_days:
                        print("Invalid present days.")
                        continue

                    break

                except ValueError:
                    print("Please enter valid numbers.")

            emp["working_days"] = working_days
            emp["present_days"] = present_days

            save_data(employees)

            print("\nAttendance saved successfully!")
            print("Working Days:", working_days)
            print("Present Days:", present_days)
            print("Absent Days :", working_days - present_days)

            return

    print("Employee not found.")


# -------------------------------
# SALARY CALCULATION
# -------------------------------
def calculate_salary(emp):

    basic_salary = emp["basic_salary"]

    # Fixed allowance and deduction
    allowance = 5000
    deduction = 2000

    working_days = emp["working_days"]
    present_days = emp["present_days"]

    # Calculate salary according to attendance
    attendance_salary = (
        basic_salary / working_days
    ) * present_days

    gross_salary = attendance_salary + allowance

    net_salary = gross_salary - deduction

    return allowance, deduction, gross_salary, net_salary


# -------------------------------
# SALARY SLIP
# -------------------------------
def salary_slip(employees):

    print("\n---------- SALARY SLIP ----------")

    emp_id = input("Enter Employee ID: ")

    for emp in employees:

        if emp["id"] == emp_id:

            allowance, deduction, gross, net = calculate_salary(emp)

            print("\n================================")
            print(" SALARY SLIP")
            print("================================")

            print("Employee ID :", emp["id"])
            print("Employee Name :", emp["name"])
            print("Department :", emp["department"])
            print("Designation :", emp["designation"])

            print("--------------------------------")

            print("Basic Salary : ₹", round(emp["basic_salary"], 2))
            print("Allowance : ₹", allowance)
            print("Deduction : ₹", deduction)

            print("--------------------------------")

            print("Working Days :", emp["working_days"])
            print("Present Days :", emp["present_days"])

            print("--------------------------------")

            print("Gross Salary : ₹", round(gross, 2))
            print("Net Salary : ₹", round(net, 2))

            print("================================")

            return

    print("Employee not found.")


# -------------------------------
# MAIN MENU
# -------------------------------
def main():

    employees = load_data()

    if not login():
        return

    while True:

        print("\n================================")
        print(" EMPLOYEE PAYROLL SYSTEM ")
        print("================================")


        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Delete Employee")
        print("5. Manage Attendance")
        print("6. Calculate Salary")
        print("7. Generate Salary Slip")
        print("8. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_employee(employees)

        elif choice == "2":
            view_employees(employees)

        elif choice == "3":
            search_employee(employees)

        elif choice == "4":
            delete_employee(employees)

        elif choice == "5":
            attendance(employees)

        elif choice == "6":

            emp = search_employee(employees)

            if emp:
                allowance, deduction, gross, net = calculate_salary(emp)

                print("\n---------- SALARY DETAILS ----------")
                print("Basic Salary :", emp["basic_salary"])
                print("Allowance :", allowance)
                print("Deduction :", deduction)
                print("Gross Salary :", round(gross, 2))
                print("Net Salary :", round(net, 2))

        elif choice == "7":
            salary_slip(employees)

        elif choice == "8":
            print("\nThank you for using Employee Payroll System!")
            break

        else:
            print("\nInvalid choice. Please try again.")


# -------------------------------
# START PROGRAM
# -------------------------------
main()
