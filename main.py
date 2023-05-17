from Resturant import Restaurant
from Table import Table, TableData
from Product import Product, ProductData
from Person import Person
from PermissionManagement import PermissionManagement, PermissionManagementData
from Order import Order, OrderData
from Menu import MenuData, Menu
from InventoryManagement import InventoryManagement, InventoryManagementData
from Ingredient import Ingredient, IngredientData, TestIngredient
from IncomeReport import IncomeReport
from Employee import Employee, EmployeeData
from Duty import Duty, DutyData
from Customer import Customer

# def main():
#     restaurant = Restaurant("Tokyo", "dizingof 59 tel aviv", "03-972657")
#     restaurant.printName()

#     # Create an instance of TableData
#     table_data = TableData("tables.csv")

#     # Create a list of tables
#     tables = [
#         Table(1, 4, "available"),
#         Table(2, 6, "available"),
#         Table(3, 2, "occupied"),
#     ]

#     # Save the tables to a CSV file
#     table_data.save(tables)

#     # Load the tables from the CSV file
#     loaded_tables = table_data.load()

#     # Print the loaded tables
#     for table in loaded_tables:
#         print(table.table_id, table.capacity, table.status)

#     # Create an instance of ProductData
#     product_data = ProductData("products.csv")

#     # Create a list of products
#     products = [
#         Product("Sushi", 72, False),
#         Product("Burger", 50, False),
#         Product("Salad", 30, True),
#     ]

#     # Save the products to a CSV file
#     product_data.save(products)

#     # Load the products from the CSV file
#     loaded_products = product_data.load()

#     # Print the loaded products
#     for product in loaded_products:
#         print(product.name, product.price, product.is_vegetarian)

#     # Create an instance of Person
#     person = Person("Lian Pahima", "053-3354332", "lianpahima0812@gmail.com", "233939")

#     # Print the person's details
#     print(person.name, person.phone, person.email, person.id)

#         # Create an instance of PermissionManagementData
#     permission_data = PermissionManagementData("permissions.csv")

#     # Create a list of permission managements
#     permission_management = PermissionManagement({}, {})

#     # Define the set_permissions method in the PermissionManagement class
#     def set_permissions(self, read, write):
#         self.customerPermission['read'] = read
#         self.customerPermission['write'] = write

#     # Bind the set_permissions method to the PermissionManagement class
#     PermissionManagement.set_permissions = set_permissions

#     # Set the permissions for the permission management instance
#     permission_management.set_permissions(read=True, write=False)

#     # Save the permission managements to a CSV file
#     permission_data.save([permission_management])

#     # Load the permission managements from the CSV file
#     loaded_permission_managements = permission_data.load()

#     # Print the loaded permission managements
#     for permission_management in loaded_permission_managements:
#         print(permission_management.customerPermission)

#     # Create an instance of Customer
#     customer = Customer("John Doe", "123-456-7890", "johndoe@example.com", "C001")

#     # Place an order for the customer
#     order_id = "O001"
#     table_id = "T001"
#     products = ["P001", "P002"]
#     total_amount = 100.0
#     reservation_status = "reserved"


# if __name__ == "__main__":
#       main()








def main():
    print("hello")
    menuData =  MenuData("./MenuData.csv")
    menu_list = menuData.load()
    menu = Menu(menu_list)
    productm  = ProductData("./lala.csv")
    productlist = productm.load()


   
    while True:
            print("\nMenu Manager Options:")
            print("1. View Menu")
            
            print("2. Add Product to Menu")
            print("3. Edit Product in Menu")
            print("4. Delete Product from Menu")
            print("5. View Products List")
            print("6. Add New Product")
            print("7. Remove Product")
            print("8. Edit Product Details")
            
            print("9. Save Menu")
            print("10. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                  print(menu_list)
                  print(productlist)
            if choice == '2':
                  prd = Product('HUMUS','123',True)
                  menu.add_product(prd)
            if choice == '10':
                 break





main()

#         elif choice == '2':
#             menu = Menu(["some product"])
#         elif choice == '3':
#             menu = Menu(["some product"])
#         elif choice == '4':
#             delete_product_from_menu()
#         elif choice == '5':
#             view_products_list()
#         elif choice == '6':
#             add_new_product()
#         elif choice == '7':
#             remove_product()
#         elif choice == '8':
#             edit_product_details()
#         elif choice == '9':
#             save_menu()
#             print("Menu has been saved.")
#         elif choice == '10':
#             print("Exiting Menu Manager...")
#             break
#         else:
#             print("Invalid choice. Please try again.")
        
#         print(menu)

# if __name__ == "__main__":
#     main()













# def main():
#     # Load initial data from files
#     menu = Menu()
#     menu.load_menu("menu.csv")

#     table_data = TableData()
#     table_data.load_tables("tables.csv")

#     employee_data = EmployeeData()
#     employee_data.load_employees("employees.csv")

#     while True:
#         print("Welcome to the Restaurant Management System!")
#         print("1. View Menu")
#         print("2. Manage Tables")
#         print("3. Manage Employees")
#         print("4. Place Order")
#         print("5. Generate Report")
#         print("6. Exit")

#         choice = input("Enter your choice: ")

#         if choice == "1":
#             # View Menu functionality
#             menu.display_menu()

#             item_choice = input("Enter the item number to view details (or '0' to go back): ")
#             if item_choice == "0":
#                 continue

#             item = menu.get_item(int(item_choice))
#             if item:
#                 item.display_details()
#             else:
#                 print("Invalid item number.")

#         elif choice == "2":
#             # Manage Tables functionality
#             table_data.display_tables()

#             table_choice = input("Enter the table number to assign or release (or '0' to go back): ")
#             if table_choice == "0":
#                 continue

#             table = table_data.get_table(int(table_choice))
#             if table:
#                 table_status = table.get_status()
#                 if table_status == "occupied":
#                     table.release_table()
#                     print(f"Table {table_choice} has been released.")
#                 elif table_status == "available":
#                     customer_name = input("Enter the customer name: ")
#                     table.assign_table(customer_name)
#                     print(f"Table {table_choice} has been assigned to {customer_name}.")
#                 else:
#                     print(f"Table {table_choice} is reserved and cannot be assigned.")
#             else:
#                 print("Invalid table number.")

#         elif choice == "3":
#             # Manage Employees functionality
#             employee_data.display_employees()

#             employee_action = input("Enter 'add', 'update', or 'remove' to perform an action (or '0' to go back): ")
#             if employee_action == "0":
#                 continue

#             if employee_action == "add":
#                 employee_name = input("Enter the employee name: ")
#                 employee_data.add_employee(employee_name)
#                 print(f"Employee {employee_name} has been added.")
#             elif employee_action == "update":
#                 employee_id = input("Enter the employee ID to update: ")
#                 employee_name = input("Enter the updated employee name: ")
#                 employee_data.update_employee(employee_id, employee_name)
#                 print(f"Employee {employee_id} has been updated.")
#             elif employee_action == "remove":
#                 employee_id = input("Enter the employee ID to remove: ")
#                 employee_data.remove_employee(employee_id)
#                 print(f"Employee {employee_id} has been removed.")
#             else:
#                 print("Invalid action.")

#         elif choice == "4":
#             # Place Order functionality
#             order_id = input("Enter the order ID: ")
#             table_id = input("Enter the table ID: ")
#             reservation_status = input("Enter the reservation status (reserved/available): ")

#             products = []
#             while True:
#                 product_name = input("Enter the product name (or 'done' to finish): ")
#                 if product_name == "done":
#                     break

#                 quantity = input("Enter the quantity: ")
#                 products.append({"name": product_name, "quantity": int(quantity)})

#             total_amount = 0
#             for product in products:
#                 product_name = product["name"]
#                 quantity = product["quantity"]
#                 product_price = menu


# def main():
#     # Load initial data
#     menu = load_menu("menu.csv")

#     # Create employees
#     employee1 = Employee("John Doe", "1234567890", "john@example.com", "E001", "Waiter", 2000)
#     employee2 = Employee("Jane Smith", "9876543210", "jane@example.com", "E002", "Chef", 3000)

#     # Add tables to employees
#     employee1.add_table(Table("T001", "Occupied"))
#     employee1.add_table(Table("T002", "Available"))
#     employee2.add_table(Table("T003", "Reserved"))

#     # Create customer
#     customer = Customer("Alice", "1111111111", "alice@example.com", "C001")

#     # Display options
#     print("Welcome to the restaurant management system.")
#     while True:
#         print("\nOptions:")
#         print("1. View menu")
#         print("2. View tables")
#         print("3. View employees")
#         print("4. Place order")
#         print("5. Quit")
#         choice = input("Enter your choice: ")

#         if choice == "1":
#             display_menu(menu)
#         elif choice == "2":
#             display_tables(employee1.tables + employee2.tables)
#         elif choice == "3":
#             display_employees([employee1, employee2])
#         elif choice == "4":
#             table_id = input("Enter table ID: ")
#             product_names = input("Enter product names (comma-separated): ").split(",")
#             reservation_status = input("Enter reservation status (reserved/available): ")
#             place_order(customer,employee1, table_id, product_names, reservation_status)
#         elif choice == "5":
#             break
#         else:
#             print("Invalid choice. Please try again.")

#         if name == "main":
#             main()

# def main():
#     # Load initial data
#     menu = load_menu("menu.csv")

#     # Create employees
#     employee1 = Employee("John Doe", "1234567890", "john@example.com", "E001", "Waiter", 2000)
#     employee2 = Employee("Jane Smith", "9876543210", "jane@example.com", "E002", "Chef", 3000)

#     # Add tables to employees
#     employee1.add_table(Table("T001", "Occupied"))
#     employee1.add_table(Table("T002", "Available"))
#     employee2.add_table(Table("T003", "Reserved"))

#     # Create customer
#     customer = Customer("Alice", "1111111111", "alice@example.com", "C001")

#     # Display options
#     print("Welcome to the restaurant management system.")
#     while True:
#         print("\nOptions:")
#         print("1. View menu")
#         print("2. View tables")
#         print("3. View employees")
#         print("4. Place order")
#         print("5. Quit")
#         choice = input("Enter your choice: ")

#         if choice == "1":
#             display_menu(menu)
#         elif choice == "2":
#             display_tables(employee1.tables + employee2.tables)
#         elif choice == "3":
#             display_employees([employee1, employee2])
#         elif choice == "4":
#             table_id = input("Enter table ID: ")
#             product_names = input("Enter product names (comma-separated): ").split(",")
#             reservation_status = input("Enter reservation status (reserved/available): ")
#             employee1.place_order(order_id, table_id, product_names, total_amount, reservation_status)  # Assuming you have the required variables
#         elif choice == "5":
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#     main()



# def main():
#     menu_data = MenuData('menu.csv')
#     menu_manager = MenuManager(menu_data)

#     while True:
#         print("Menu Manager")
#         print("1. View Menu")
#         print("2. Add Product")
#         print("3. Edit Product")
#         print("4. Delete Product")
#         print("5. Save Menu")
#         print("6. Exit")

#         choice = input("Enter your choice: ")

#         if choice == '1':
#             menu_manager.view_menu()
#         elif choice == '2':
#             product = input("Enter the name of the product: ")
#             menu_manager.add_product(product)
#         elif choice == '3':
#             name = input("Enter the name of the product: ")
#             price = input("Enter the new price: ")
#             menu_manager.edit_product(name, price)
#         elif choice == '4':
#             product_name = input("Enter the name of the product to delete: ")
#             menu_manager.delete_product(product_name)
#         elif choice == '5':
#             menu_manager.save_menu()
#             print("Menu saved successfully.")
#         elif choice =='6':
#              print("Exiting...")
            
#         else:
#              print("Invalid choice. Please try again.")

#         if name == "main":
#              main()




# def main():
#     while True:
#         print("\nMenu Manager Options:")
#         print("1. View Menu")
#         print("2. Add Product to Menu")
#         print("3. Edit Product in Menu")
#         print("4. Delete Product from Menu")
#         print("5. View Products List")
#         print("6. Add New Product")
#         print("7. Remove Product")
#         print("8. Edit Product Details")
#         print("9. Save Menu")
#         print("10. Exit")

#         choice = input("Enter your choice: ")

#         if choice == '1':
#             self.view_menu()
#         elif choice == '2':
#             self.view_products()
#             product_name = input("Enter the product name to add to the menu: ")
#             product = self.get_product_by_name(product_name)
#             if product:
#                 self.add_product(product)
#             else:
#                 print(f"Error: {product_name} not found in the products list.")
#         elif choice == '3':
#             self.view_menu()
#             product_name = input("Enter the product name to edit in the menu: ")
#             product = self.get_product_by_name(product_name)
#             if product:
#                 new_price = float(input("Enter the new price: "))
#                 self.edit_product(product_name, new_price)
#             else:
#                 print(f"Error: {product_name} not found in the menu.")
#         elif choice == '4':
#             self.view_menu()
#             product_name = input("Enter the product name to delete from the menu: ")
#             self.delete_product(product_name)
#         elif choice == '5':
#             self.view_products()
#         elif choice == '6':
#             name = input("Enter the name of the new product: ")
#             price = float(input("Enter the price of the new product: "))
#             is_vegetarian = input("Is the new product vegetarian? (yes/no): ").lower() == 'yes'
#             self.add_new_product(name, price, is_vegetarian)
#         elif choice == '7':
#             name = input("Enter the name of the product to remove: ")
#             self.remove_product(name)
#         elif choice == '8':
#             name = input("Enter the name of the product to edit: ")
#             price = float(input("Enter the new price: "))
#             is_vegetarian = input("Is the product vegetarian? (yes/no): ").lower() == 'yes'
#             self.edit_product_details(name, price, is_vegetarian)
#         elif choice == '9':
#             self.save_menu()
#             print("Menu has been saved.")
#         elif choice == '10':
#             print("Exiting Menu Manager...")
        
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == "__main__":
#       main()





# from Resturant import Restaurant

# def main():
#         restaurant = Restaurant("Tokyo", "dizingof 59 tel aviv", "03-972657")
#         restaurant.printName()

# if __name__ == "__main__":
#     main()




