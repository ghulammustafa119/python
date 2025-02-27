# list...

shopping_items : list[str] = ["Cake", "Eggs", "Juice", "Chips", "Bread"]
# print(shopping_items)
# print(shopping_items[2])
# print(shopping_items[3])
# length of list---
# print(len(shopping_items))
# slice---
# print(shopping_items[0:3]) 
# memberShip---
# print("Cake" in shopping_items)
# adding and removing items from the list---
print(shopping_items)

shopping_items.append("Sugur")
# print(shopping_items)

shopping_items.append("Flour")
# print(shopping_items)

shopping_items.append("Oil")
# print(shopping_items)

shopping_items.remove("Sugur")
# print(shopping_items)

shopping_items.remove("Flour")
# print(shopping_items)

shopping_items.remove("Oil")
# print(shopping_items)

shopping_items.insert(3,"Tea")
print(shopping_items)

shopping_items.pop(4)
print(shopping_items)