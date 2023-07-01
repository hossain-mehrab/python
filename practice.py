# Variables and Data-types in Python
name1 = "Hossain Md Mehrab"
number1 = 3.1415
number2 = True
number3 = 2+3j

print (name1)
type(name1)

print (number1)
type(number1)

print (number2)
type(number2)


print (number3)
type(number3)


# Operators in Python
a = 10
b = 20
## + - * / Arithmetic
print(a+b)
print(a-b)
print(a*b)
print(a/b)
## > < == != Relational
print(a>b)
print(a<b)
print(a==b)
print(a!=b)
## & (AND), | (OR) Logical(Bitwise) 
a = True
b = False
print(a&b)
print(a|b)

# Tokens in Python
## Keywords
if (a>b):
 print("Hello World")
## Identifiers
my_name = "Mehrab"
## Literals 
a1 = 30
a2 = "Hossain"
a3 = 60
print(a1)
print(a2)
## Operators
print (a1+a3)


# Strings
# %%
name_by_adress = 'Hossain'
name_by_adress = "Hossain"
name_by_adress = '''Hossain-1, Hossain-2, Hossain-3, Hossain-3'''
print(name_by_adress)
type(name_by_adress)
name_by_adress[0]
name_by_adress[-2]

## Strings Function
print(len(name_by_adress))
print(name_by_adress.upper())
print(name_by_adress.lower())
print(name_by_adress.replace("H", "B"))
print(name_by_adress.replace("H", "B"))
print(name_by_adress.count("Hossain-3"))
print(name_by_adress.find("Hossain-2"))
print(name_by_adress.split(','))

# Tuples (It is imutable and can't change the value)
tup1 = ("a", True, 1234, "Sat")
tup2 = ("b", False, 5, "Mon")
tup3 = (1, 2, 3, 4)
type(tup1)
tup1 
tup1[0]
tup1[0:2]
# tup1[0] ="b"
len(tup1)
tup1+tup2
tup2+tup1
tup2*3+tup1
min(tup3)
max(tup3)

# List (It is mutable and can change the value)
l1 = ["a", True, 1234, "Sat"]
l2 = ["b", False, 5, "Mon"]
l3 = [1, 2, 3, 4]
l4 = ["c", "a", "f"]
l5 = [2, 7, 4, 3]
l1[0] = "b"
print(l1)
print(l1[0])
print(l1[-1])
print(l1[0:3])

l1 [0] = (100)
print(l1)

l2.append("Mehrab")
print(l2)

l3.pop()
print(l3)

l3.reverse()
print(l3)

l3.insert(0, "Mehrab")
print(l3)

l4.sort()
print(l4)

l5*3
print(l5)
print(l4+l5)

# Dictionary (mutable, item and value of key)
fruit1 ={
  "Mango": 100, 
  "Apple": 200, 
  "Orange": 300
}
print(type(fruit1))
print(fruit1.items())
print(fruit1.keys())
print(fruit1.values())
fruit1["Lemon"]= 400
print(fruit1)
fruit1["Mango"]= 50
print(fruit1)

fruit2 ={
  "Mango1": 100, 
  "Apple2": 200, 
  "Orange3": 300
}

fruit1.update(fruit2)
print(fruit1)

fruit1.pop("Lemon")
print(fruit1)

# Set (duplicate value are not accepted)
# %%
set1 = {1, "man", True, 1, "man", True}
print(set1)

set2 = {1, "man", True}
set2.add("a")
print(set2)

set2.remove("man")
print(set2)

set2.update(["run",3, False])
print(set2)

set1.union(set2)
print(set1)

set1.intersection(set2)
print(set1)

# If statement
a = 10
b = 20
if a>b:
  print("a is greater than b")
else:
  print("a is not greater than b")

a1 = 5
b1 = 10
c1 = 15
if (a1>b1 & a1>c1):
  print("a1 is greater than b1, and c1")

elif (b1>a1 & b1>c1):
  print("b1 is greater than a1, and c1")

else:
  print("c1 is greater than a1, and b1")

# If statement (Tuples)
a3 = (1, 3, 4)
if 1 in a3:
  print("1 in the Tuple")
else:
  print("1 is not in the Tuple")

# If statement (List)
a4 = [1, 3, 4]
if a4[0]==1:
  a4[0]=a4[0]+100
  print(a4)
else:
  print("Nothing")

# If statement (Dictonary)
a5 = {
  "Man":20,
  "Women":30
}
if a5["Man"]==20:
  a5["Man"]=a5["Man"]+100
  print(a4)
else:
  print("Nothing")

# %%
