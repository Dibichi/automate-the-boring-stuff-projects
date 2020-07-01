#! python3
#inventory.py - displays and adds to an inventory of items

def displayInventory(inventory):
    print("Inventory:")
    itemTotal = 0
    for k, v in inventory.items():
        print(str(v)+ ' ' + k)
        itemTotal+= v
    print("Total number of items: " + str(itemTotal))

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0) #this adds a (defaulted to zero value) key to the inventory dict if it's not already there
        inventory[item] += 1 #and this increases that value by one, each time that item appears in the loot list
    return inventory

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)


