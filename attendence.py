class Attendance:
    def __init__(self, employee_id, present, total):
        self.employee_id = employee_id
        self.present = present
        self.total = total

    def calculate_attendance(self):
        if self.total == 0:
            return 0
        return (self.present / self.total) * 100

    def display(self):
        print("Employee ID:", self.employee_id)
        print("Present Days:", self.present)
        print("Total Working Days:", self.total)
        print("Attendance Percentage:", self.calculate_attendance(), "%")


attendance = Attendance(101, 24, 30)
attendance.display()
