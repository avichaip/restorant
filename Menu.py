import csv
import unittest
from Product import Product as _product


class MenuData:
    def __init__(self, filename):
        self.filename = filename
        print(self.filename)

    def save(self, menus):
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['product'])
            for menu in menus:
                writer.writerow([menu.products])

    def load(self):
        menus = []
        with open(self.filename, 'r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                menus.append(row)   
        return menus
    



class Menu:
    def __init__(self, products):
        self.products = products

    def view_menu(self):
        for product in self.products:
            return(product)

    def add_product(self, product):
        self.products.append(product)
        print(f"{product.name} has been added to the menu.")

    def edit_product(self, name, price):
        for i, product in enumerate(self.products):
            if product.name == name:
                product.price = price
                print(f"{product.name} has been updated with a new price of ${product.price}")
                return
        print(f"Error: {name} not found in the menu.")

    def delete_product(self, product_name):
        for i, product in enumerate(self.products):
            if product.name == product_name:
                del self.products[i]
                print(f"{product_name} has been deleted from the menu.")
                return
        print(f"Error: {product_name} not found in the menu.")

def view_menu(products):
    for product in products:
        print(product)

def add_product(products, product):
    products.append(product)
    print(f"{product.name} has been added to the menu.")

def edit_product(products, name, price):
    for i, product in enumerate(products):
        if product.name == name:
            product.price = price
            print(f"{product.name} has been updated with a new price of ${product.price}")
            return
    print(f"Error: {name} not found in the menu.")

def delete_product(products, product_name):
    for i, product in enumerate(products):
        if product.name == product_name:
            del products[i]
            print(f"{product_name} has been deleted from the menu.")
            return
    print(f"Error: {product_name} not found in the menu.")

