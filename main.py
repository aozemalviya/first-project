from employee import Employee
from attendance import Attendance
from payroll import Payroll

print("EMPLOYEE PAYROLL MANAGEMENT SYSTEM")

employee = Employee(101, "Rahul", "IT", 30000)
employee.show_details()

print("\nAttendance")
attendance = Attendance(101, 24, 30)
attendance.display()

print("\nPayroll")
salary = Payroll(101, 30000)
salary.display_salary()
