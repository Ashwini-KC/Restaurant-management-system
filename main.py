from src import Employee
from prettytable import PrettyTable

main_menu = PrettyTable(["Options", "Operations"])
main_menu.add_row(["1", "Employees"])
main_menu.add_row(["2", "Menu"])
main_menu.add_row(["3", "Bill"])
main_menu.add_row(["4", "Table"])
main_menu.add_row(["5", "Order"])
main_menu.add_row(["6", "Exit"])

employee_menu = PrettyTable(["Options", "Operations"])
employee_menu.add_row(["1", "Add Employee"])
employee_menu.add_row(["2", "Delete Employee"])
employee_menu.add_row(["3", "Update Employee"])
employee_menu.add_row(["4", "Employee details"])
employee_menu.add_row(["5", "List All Employees"])
employee_menu.add_row(["6", "Previous menu"])

emp_table = PrettyTable(["Options", "Attributes"])
emp_table.add_row(["1", "empName"])
emp_table.add_row(["2", "empType"])
emp_table.add_row(["3", "Update"])
emp_table.add_row(["4", "Previous menu"])

def main():
    flag = True

    while flag:
        print(main_menu)
        option = input("Choose an option.\n")
        match option:
            case "1":
                employee_flag = True
                while employee_flag:
                    print(employee_menu)
                    employee_option = input("Choose an option.\n")
                    match employee_option:
                        case "1":
                            emp = Employee()
                            employee = {}
                            employee["empID"] = input("Employee ID:\t")
                            employee["empName"] = input("Employee Name:\t")
                            employee["empType"] = input("Employee Type:\t")
                            emp.add_employee(empID=employee["empID"], empName=employee["empName"], empType=employee["empType"])
                        case "2":
                            emp = Employee()
                            empID = input("Enter the Employee ID:\t")
                            emp.delete_employee(empID)
                        case "3":
                            empID = input("Enter the Employee ID:\t")
                            emp = Employee()
                            new_emp = emp.employee_details(empID)
                            update_flag = True
                            while update_flag:
                                print(emp_table)
                                update_option = input("Enter option.\n")
                                match update_option:
                                    case "1":
                                        new_emp["empName"] = input("Enter new empName:\t")
                                        print(new_emp)
                                    case "2":
                                        new_emp["empType"] = input("Enter nea empType:\t")
                                        print(new_emp)
                                    case "3":
                                        update_flag = False
                                        emp.update_employee(new_emp['empID'], new_emp)
                                    case "4":
                                        update_flag = False
                            print(new_emp)
                        case "4":
                            empID = input("Enter the Employee ID:\t")
                            emp = Employee()
                            emp = emp.employee_details(empID)
                            emp_table = PrettyTable([key for key, value in emp.items()])
                            emp_table.add_row([value for key, value in emp.items()])
                            print(emp_table)
                        case "5":
                            all_EMPLOYEE = PrettyTable(["empID", "empName", "empType"])
                            emp = Employee()
                            for employee in emp.get_all_employees():
                                all_EMPLOYEE.add_row([employee['empID'], employee['empName'], employee['empType']])
                            print(all_EMPLOYEE)
                        case "6":
                            employee_flag = False
            case "6":
                flag = False
    
if __name__ == "__main__":
    main()
    