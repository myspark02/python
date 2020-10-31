employee_file = open("/Volumes/Data/Documents/scpark/VSC/workspace/python/.vscode/employees.txt", "r") # "w", "a", "r+"

print(employee_file.readable())
# print(employee_file.read())
# print(employee_file.readline())
# print(employee_file.readline())
# print(employee_file.readline())
for employee in employee_file.readlines() :
    print(employee)
# print(employee_file.readlines()[1])

employee_file.close()
