"""
data structures
1. list
2. Tuple
3. Dictionary
"""
# list - store a collection of variables and other data structures.
myList = []
# checking the type of variable
print(type(myList))
myList = [1,2,3,4,5]
print(myList)
mylist2 = [1.1,1.2,1.3,1.4,1.5]
mylist3 = ["bread","milk","eggs"]

daysOfTheWeek =["Monday","Tuesday","Wen","Thur","Fri","Sat","Sun"]

# Creating a lists inside a list
list1 = [True,False]
List2 = ["kelvin","Johnson","David"]
ls = [list1,List2]
# Retriving a list inside a list
print(ls[1][2])
print(ls)

# Option b
ls1 = [True,False],["kelvin","David"]
print(ls1)
# Accessing a particular item in a list
print(daysOfTheWeek[6])
# Slicing in lists
print(daysOfTheWeek[1:6])

"""
List Operation
len()
Adding of list (concat) eg list2 = [list1 + List2}
deleting inside a list

"""

# Tuple looks like a list, difference it uses commas () unlike list plus one can't edit (Immutable)

tup = (1,"str",True,[1,"cake",12.3],["Kenya","Uganda","Tanzania"],12)
print(tup[2:5])
print(tup[3])
print(tup[:5])
print(tup[:-3])
print(tup[::-1])

# appending or adding an item inside a list inside a tuple
x = tup [4]
x.append("Rwanda")
print(tup[4])

# dictionary
mydict = {}
print(type(mydict))
"""
dictionary contains a key and a value i.e "age":30 . Note they are separated by a full colon.

Another example
"language":"English"
"language":["English","Kiswahili"]
"""

mylife ={
    "name":"Kelvin",
    "Age":30,
"languagesSpoken":["French","Swahili"],
"myparents":{
    "Father":"Johnson",
    "Mother":"Wanja",

},
"PrimarySchools":["School1","School2"]
}
print(mylife)

# to call an item in the dictionary

print(mylife["name"])
print(mylife["myparents"])
