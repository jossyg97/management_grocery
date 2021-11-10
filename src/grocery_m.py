from datetime import datetime, timedelta

class Grocery:
    def __init__(self):
        self.inventory = []
    
    def add_product(self, p_name, count, date_added, shelf_l):
        new_product = Product(p_name, count, date_added, shelf_l)
        self.inventory.append(new_product)

    def decrement_product(self, item_bought, amount_bought):
        same_item = False
        for item in self.inventory:
            if item.p_name == item_bought:
                if amount_bought <= item.count:
                    item.count -= amount_bought
                    print("There are now", item.count, item_bought, "in inventory")
                elif item.count == 0:
                    print("There are no more", item_bought, "available. \nPlease restock")
                else:
                    print("That amount of", item_bought, "are not available in inventory. \nPlease check item and amount in inventory")
                same_item = True 
        if same_item == False:
            print("The item is not in inventory")



    def show_inventory(self):
        for item in self.inventory:
            print(item.p_name, item.count, item.date_added, item.shelf_l)


    def check_inventory(self, product_name):
        match_found = False
        for item in self.inventory:
            if item.p_name == product_name:
                print(product_name, "is in inventory and there are: ", item.count)
            match_found = True
        if match_found == False:
            print("This item is not in inventory")

        
    def check_expiration(self, item_purchased, date_checked):
        self.date_checked= datetime.strptime(date_checked, "%Y-%m-%d")
        for item in self.inventory:
            if item.p_name == item_purchased:
                if (item.date_added + timedelta(days = item.shelf_l)) <= self.date_checked:
                    print(item_purchased, "is expired")
                else:
                    print(item_purchased, "has not expired yet")

class Product:
    def __init__(self, p_name, count, date_added, shelf_l):
        self.p_name= p_name
        self.count= count
        self.shelf_l= shelf_l
        self.date_added= datetime.strptime(date_added, "%Y-%m-%d")


      
