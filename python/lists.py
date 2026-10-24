# LISTS IN PYTHON
# Lists are initiated with [square brackets]

num = [1, "Aditya",35.5 , "This is a list"]
# A list in python can contain any datatype , lists are 0 indexed .

for n in num:
    print(n)

random =[]

for i in range (10)  :
    random.append(i) # .append()function is used to add single element to the end of a list

print(random)
# .insert() is used to add an element at a specific index .
num.insert(1,"inserted") # This inserts string "inserted" at index number 1.

print(num)

