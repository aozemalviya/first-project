class Payroll:
    def __init__(self, employee_id, basic_salary):
        self.employee_id = employee_id
        self.basic_salary = basic_salary

    def calculate_salary(self):
        hra = self.basic_salary * 0.10
        da = self.basic_salary * 0.05
        ta = self.basic_salary * 0.05

        gross_salary = self.basic_salary + hra + da + ta
        return gross_salary

    def display_salary(self):
        salary = self.calculate_salary()

        print("Employee ID:", self.employee_id)
        print("Basic Salary:", self.basic_salary)
        print("Gross Salary:", salary)


payroll = Payroll(101, 30000)
payroll.display_salary()