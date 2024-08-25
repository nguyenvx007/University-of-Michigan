# Provided is a list of data about a store’s inventory where each item in the list represents the name of an item, how much is in stock, and how much it costs. Print out each item in the list with the same formatting, using the .format method (not string concatenation). For example, the first print statment should read The store has 12 shoes, each for 29.99 USD.
#
# Pseudocode
#
# 1. Retrieve inventory list - Given "inventory" list variable
# 2. Define iterating "items" variable and iterate through inventory
# 2.a Remove spaces from iterating "items" variable
# 2.b Convert iterating variable "items" to a list type variable
# 3.b Using .format metthod, print each interating list variable "items" in the follwoing format: "The store has <iitem_number> <item_type>, each for <item_cost> USD."
# 
inventory = ["shoes, 12, 29.99", "shirts, 20, 9.99", "sweatpants, 25, 15.00", "scarves, 13, 7.75"]
## Pseudocode
# Iterate through inventory item (string)
# Remove spaces for consistency in printing with out spaces
# Convert inventory item (string) to item (list) using split
# Print items phrase using .format
for items in inventory:
    items = items.replace(" ","")
    items = items.split(",")
    print ("The Store has {} {}, each for {} USD.".format(items[1],items[0],items[2]))
           


