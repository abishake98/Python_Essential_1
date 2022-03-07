# Python_Essential_1

No_of_Employees = 0

First_Name = input("Enter your first name: ")

Last_Name = input("Enter your last name: ")

Age_str = None

while Age_str == None:
    Age=int(input("Please enter your age: "))
    if Age < 18:
        Age = None
    elif Age > 100:
        Age = None
    else:
        output = Age
        break


Employee_Data = ("First Name : " + First_Name, "Last Name : " + Last_Name, "Age : " + str(Age))

print(Employee_Data)
