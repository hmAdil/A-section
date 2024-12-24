print("Q5. Shopping List/Dict:")
dict1 = {"apple": 2,"banana": 1,"orange": 3}
dict2 = {"banana": 2,"grape": 4,"pear": 2}
dict3 = {"apple": 3,"grape": 3,"watermelon": 5}
fdict = {}
print("A Bought", dict1); print("B Bought",dict2), print("C Bought",dict3)

for shopdict in [dict1, dict2, dict3]:
    for item, qty in shopdict.items():
        fdict[item] = qty  

print("Final shopping list (actually a dictionary) without duplicates: ")
print(fdict)
totalamt = sum(fdict.values())

