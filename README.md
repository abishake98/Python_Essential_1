# Python_Essential_1

No_of_Employees = input("Please enter the number of employees in the company: ")

for index in range(int(No_of_Employees)):

    y = None

    while y == None:
        First_Name = input("Enter your first name: ")
        x = len(First_Name)
        if x == 0:
            x = None
        else:
            output = First_Name
            print(First_Name)
            break

    while y == None:
        Last_Name = input("Enter your last name: ")
        x = len(Last_Name)
        if x == 0:
            x = None
        else:
            output = Last_Name
            print(Last_Name)
            break

    while y == None:
        Age=int(input("Please enter your age: "))
        if Age < 18:
            Age = None
        elif Age > 100:
            Age = None
        else:
            output = Age
            print(Age)
            break
    Employee_Data = ["First Name : " + First_Name, "Last Name : " + Last_Name, "Age : " + str(Age)]
    print(Employee_Data)
