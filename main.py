from src import Employee, Customer, Chef

# employee_1 = Employee(21, "Akhil", 2)
# employee_1.add_employee()

# emp_2 = Employee(22, "Shreyas", 1)

# employee_1.update_employee({"EmpID": 69, "EmpName": "Kundrotte"})

# employee_1.delete_employee()


from src import Item, Menu, Order

'''
item_1 = Item(1, "Chapati", 2, "Bread")
item_2 = Item(2, "Chicken", 3, "Main-course")
item_3 = Item(3, "Lamb", 3, "Main-course")
item_4 = Item(4, "Noodles", 1, "Chinese")
item_5 = Item(5, "Chicken Nuggets", 10, "Starters")

menu = Menu()
menu.add_item(item_1)
menu.add_item(item_2)
menu.add_item(item_3)
menu.add_item(item_4)
menu.add_item(item_5)

print(menu.find_by_id(1))
# print(menu.delete_item(1))
menu.update_item(item_3, {"itemID": 69, "itemName": "Garlic Naan"})


print(menu.get_menu())

'''
customer1 =Customer('2222PP','JJ BUXTOM','Eat-In')
customer2 =Customer('223LPX','Harry Maguire','Takeaway')
customer1.add_customer()
customer2.add_customer()


employee1 = Employee('WS12','HARRY STYLES','WAITER')
employee1.add_employee()
'''
order1 = Order()
order1.add_items("100",employee1,customer1,8)
order1.place_order_items()
'''
order2 = Order()

order2.add_items("17",employee1,customer2,2)
order2.place_order_items()
