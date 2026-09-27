def search_employee(employees, employee_id):
    for employee in employees:
        if employee.employee_id == employee_id:
            return employee
    return None