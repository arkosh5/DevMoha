print("employee management system")
table = []
employee_info = []
check_emp_num = []
occupation = []
firstname = ""
surname = ""
num = 0
choice = ""
length = 0
while True:
    choice = input(" do you want to add,remove,update, search, or q to quit: ")
    if choice.lower() == "add":
        try:
            length = int(input("how many employees to add?: "))
            for i in range(length):
                firstname = input("enter the name of the employee: ").lower().capitalize()
                if firstname.isdigit():
                    print("firstname name can't contain numbers")
                    length += 1
                surname = input("enter the employee surname").lower().capitalize()
                if surname.isdigit():
                    print("The surname can't contain numbers")
                    continue
                occupation = input("What is the occupation? ").lower().capitalize().strip()
                if occupation.isdigit():
                    continue
                emp_num = int(input("Enter the employee number"))
                if emp_num in check_emp_num:
                    while emp_num in check_emp_num:
                        emp_num = int(input("Employee number already exist try again: "))

                if firstname.isalpha() and surname.isalpha():
                    check_emp_num.append(emp_num)
                    num += 1
                    employee_info = firstname + " " + surname + " Occupation: " + occupation + ": employee number: " + str(
                        emp_num)
                    table.append(f"{num}: employee: " + employee_info)
                    table.sort()
        except ValueError as e:
            print(e)

    if choice.lower() == 'remove':
        try:
            length = int(input("how many employees to remove? "))

            for i in range(length):
                removeFirstname = input("enter the name you want to remove").lower()
                removeSurname = input("enter the surname you want to remove").lower()
                remove = (removeFirstname + " " + removeSurname)
                print(f"are you sure you want to remove?{remove}")
                choice = input(">")

                if choice == "yes":
                    print(f"{remove} have been removed")
                    table[::] = [check for check in table if remove not in check]
                    num -= 1
                    choice = input("remove from file as well? ")
                    if choice == "yes":
                        file_remove = " "
                        with open("employee.txt", "w") as f:
                            for line in file_remove:
                                if line.strip("\n") != remove:
                                    f.write(line)
                else:
                    print("employee not found! ")
                if choice == "no":
                    continue
        except ValueError as e:
            print(e)
    if choice == "search":
        employee_search = input("enter the employee number or name to search")
        for search in table:
            if employee_search in search:
                print(search)

    if choice == "update":
        employee_search = input("enter the employee number to update")

        for update in table:
            if employee_search in update and employee_search.isdigit():
                choice = input("what do you want to update(e.g, occupation,surname or firstname) ")
                if choice == "Occupation":
                    update_employee = input("what is the new occupation? ")
                    # using list comprehension + replace()
                    # Replace substring in list of strings
                    index = occupation
                    table = [sub.replace(index, update_employee) for sub in table]
                if choice == "Surname":
                    update_employee = input("what is the new Surname? ")
                    # using list comprehension + replace()
                    # Replace substring in list of strings
                    index = surname
                    table = [sub.replace(index, update_employee) for sub in table]
                if choice == "firstname":
                    update_employee = input("what is the new firstname? ")
                    # using list comprehension + replace()
                    # Replace substring in list of strings
                    index = firstname
                    table = [sub.replace(index, update_employee) for sub in table]
            else:
                choice = "update"

    with open('employee.txt', 'a') as employee_file:
        for item in table:
            employee_file.write("%s\n" % item)
        employee_file.close()
    print(f"current employees are {table}")

    if choice.lower() == "q":
        break

