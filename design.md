System Design

## 1. System Architecture

The project is divided into different modules.

- `main.py` - connects and runs the different modules
- `employee.py` - manages employee details
- `attendance.py` - calculates attendance
- `payroll.py` - calculates salary
- `search.py` - searches for employees
- `storage.py` - saves and loads employee data
- `test.py` - tests important calculations

## 2. System Workflow
---------------------------
User
↓
Main Program
↓
Employee Details
↓
Attendance
↓
Payroll Calculation
↓
Salary Result
↓
Save Employee Data
----------------------------
## 3. Main Components

### Employee
Stores:
- Employee ID
- Name
- Department
- Basic Salary

### Attendance
Stores:
- Employee ID
- Present Days
- Total Working Days

It calculates the attendance percentage.

### Payroll
Uses the basic salary to calculate:
- HRA
- DA
- TA
- Gross Salary

### Storage
Uses JSON to save and load employee information.

## 4. Data Storage

Employee information is stored in:

`employees.json`
The program uses Python's JSON module to read and write the data.

## 5. Testing

The `test.py` file checks whether attendance and salary calculations give the expected results.