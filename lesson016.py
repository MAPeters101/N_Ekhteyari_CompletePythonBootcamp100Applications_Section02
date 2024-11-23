
age = 26
#text = "Hello my name is Mark and i am " + age
text = "Hello my name is Mark and i am " + str(age)
print(text)
print()


text = "Hello my name is Mark and i am {}"
print(text.format(age))
print()

qty = 2
price = 34
itemno = 345
text = "I want {} pieces of item {} for {} dollars."
print(text.format(qty, itemno, price))
print()


text = "I want {0} pieces of item {2} for {1} dollars."
print(text.format(qty, itemno, price))
print()


text = f"I want {qty} pieces of item {itemno} for {price} dollars."
print(text)
print()


