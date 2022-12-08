from src import Employee, Item, Menu
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


menu_table_menu = PrettyTable(["Options", "Operations"])
menu_table_menu.add_row(["1", "Add an Item to the Menu"])
menu_table_menu.add_row(["2", "Delete an Item to the Menu"])
menu_table_menu.add_row(["3", "Update an Item to the Menu"])
menu_table_menu.add_row(["4", "List Menu"])
menu_table_menu.add_row(["5", "Previous menu"])

menu_item_update_table = PrettyTable(["Options", "Attributes"])
menu_item_update_table.add_row(["1", "itemName"])
menu_item_update_table.add_row(["2", "itemPrice"])
menu_item_update_table.add_row(["3", "itemType"])
menu_item_update_table.add_row(["4", "Update"])
menu_item_update_table.add_row(["5", "Previous menu"])

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
                            print(emp.delete_employee(empID))
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
            case "2":
                menu_loop_flag = True
                while menu_loop_flag:
                    print(menu_table_menu)
                    menu_option = input("Choose an option.\n")
                    match menu_option:
                        case "1":
                            menu = Menu()
                            itemID = input("Item ID:\t")
                            itemName = input("Item Name:\t")
                            itemPrice = input("Item Price:\t")
                            itemType = input("Item Type:\t")

                            item = Item(itemID, itemName, itemPrice, itemType)

                            print(menu.add_item(item), " Added to the menu.\n")
                        case "2":
                            menu = Menu()
                            itemID = input("Item ID:\t")
                            print(menu.delete_item(itemID), "Deleted.")
                        case "3":
                            itemID = input("Enter the Item ID:\t")
                            menu_update_flag = True
                            menu = Menu()
                            new_item = menu.find_by_id(itemID)
                            while menu_loop_flag:
                                print(menu_item_update_table)
                                menu_update_options = input("Enter option.\n")
                                match menu_update_options:
                                    case "1":
                                        new_item["itemName"] = input("Item Name:\t")
                                        print(new_item)
                                    case "2":
                                        new_item["itemPrice"] = input("Item Price:\t")
                                        print(new_item)
                                    case "3":
                                        new_item["itemType"] = input("Item Type:\t")
                                        print(new_item)
                                    case "4":
                                        menu_loop_flag = False
                                        menu.update_item(itemID, new_item)
                                    case "5":
                                        menu_update_flag = False

                        case "4":
                            menu = Menu()
                            MENU_ITEMS = PrettyTable(["itemID", "itemName", "itemPrice", "itemType"])
                            emp = Employee()
                            for item in menu.get_all_items():
                                MENU_ITEMS.add_row([item['itemID'], item['itemName'], item['itemPrice'], item['itemType']])
                            print(MENU_ITEMS)

                        case "5":
                            menu_loop_flag = False
            case "3":
                print("Bill")
            case "4":
                print("Table")
            case "5":
                print("Order")
            
            case "6":
                flag = False
    
if __name__ == "__main__":
    main()