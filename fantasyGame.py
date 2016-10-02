
Inventory ={'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
Inven = {'gold coin': 42, 'rope':1}

def displayInventory(inv):
    print('Inventory:')
    count = 0
    for k, v in inv.items():
        count += v
        print(str(v) + ' '+ k)
    print('Total number of items: ' + str(count))

def addToInventory(inv, addedItems):
    for L in addedItems:
        for k, v in list(inv.items()):
            if k==L:
                inv[k] = v + 1
            else:
                inv.setdefault(L,1)
    return inv

Inven= addToInventory(Inven,dragonLoot)
displayInventory(Inven)
            
            
