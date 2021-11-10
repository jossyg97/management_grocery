from grocery_m import Grocery
Jos = Grocery()
Jos.add_product("Oranges", 100, "2021-10-17", 30)
Jos.add_product("Apples", 150, "2021-10-17", 40)
Jos.add_product("Grapes", 200, "2021-10-17", 20)
Jos.add_product("Tomato", 200, "2021-10-17", 30)
Jos.add_product("Cabbage", 150, "2021-10-17", 40)


Jos.show_inventory()
Jos.check_inventory("Oranges")
Jos.check_inventory("Apples")
Jos.decrement_product("Oranges", 99)
Jos.show_inventory()
Jos.check_expiration("Oranges", "2021-11-15")
Jos.check_expiration("Apples", "2021-12-25")