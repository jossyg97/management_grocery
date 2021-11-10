
Grocery management is a package for people who are running a grocery or managing one, and want to make use of this package to manage their items/product in store.

There are five function in my project: add_product which allows the user to add products to the grocery, decrement which allows the user to take out products from the grocery, show_inventory which will show all product in inventory. check_inventory which will check if the item you are looking for is in inventory and last check_expiration which will check for expiration dates from product let you know where a product has expired or not. 

To use my program first you will have to import the package as from grocery_m import Grocery. Then you will have to create a Grocery which you could name whatever you wish it to be. Once you have named it you can start using the functions with the name given. 

For add_products you will have to give the following information as attributes in the given order: Name of the product, the amount of that product, the date added to inventory, which has to be in the following format: yyyy-mm-dd as a string, and last the shelftime of that product.  

To decrement product from inventory you can call the function decrement and give the name of the product ,as added to inventory, and the amount you want to decrement as attibutes in that order, assuming this items were bought or have expired and you want to take them out of your shelf. 

Next, to show inventory you actually do not need to input any attributes to the show_inventory function, all you have to do is call it and it will give you the products in inventory. 

And to check for a specific item to see if it is in iventory all you have to do is include the products name ,as added to inventory, and it should let you know if the product is in inventory and how much of it is available. 

The last function you can use is check_expiration, and what you have to do to call it is: include the product's name, as added to inventory, in the function, and the date you are checking on in the following format: yyyy-mm-dd. The output should be to let you know whether those products are expired or not. 

***Important: 
In order to use my project you will need to have the datetime module installed in your system. ***


To explain a little about why I created this package is mainly because a lot of times with small groceries what I have noticed is that they can have a product for a long time and they do not notice that the product is already expired and needs to be taken out of the shelf. With my program they can easily check for a product and maybe even install it to a system they already have to make sure that when product are being checked out that they are not expired. Another thing it can do is let the manager/worker know that specific items are put of stock and need to be added. This program looks like a fairly easy program to create, but for me who only knows Java and has just started learning pything the set up to make sure that it made sense and worked how I want it it to was not as easy. I could figure out the idea of what I wanted it to do and a bit on how for each function individually, but to make sure that it all came together and was visually understandable was complicated. But overall, I feel like I succeeded at making sure that my program is readable and understanable. 