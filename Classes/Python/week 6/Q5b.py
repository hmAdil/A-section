print("Q5. Shopping List:")
list1 = [("apple", 2), ("banana", 1), ("orange", 3)]
list2 = [("banana", 2), ("grape", 4), ("pear", 2)]
list3 = [("apple", 3), ("grape", 3), ("watermelon", 5)]
flist = {}
print("A Bought", list1); print("B Bought", list2), print("C Bought", list3)

for shoplist in [list1, list2, list3]:
    for item, qty in shoplist:
        if item in flist:
            flist[item] += qty
        else:
            flist[item] = qty

print("Final shopping list : ")
print(flist)
total = sum(flist.values())
print("Total Billing Amount: ",total)

