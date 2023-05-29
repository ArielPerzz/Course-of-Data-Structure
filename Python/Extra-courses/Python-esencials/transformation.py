name = "Nicolas"
print(type(name))
# name = 12
# print(type(name))
# name = True
# print(type(name))
age = 12
print("My age is: " + str(age)) #one way to print int with string
print(f"my age is: {age}") #another way to print int whith one string using "format"

#age = input"'write your age => ")
age = int(input("write your age => ")) #this is another way to asing the type of data in the same line
print(type(age))
age += 10 #adding age 10 units 
print(f"your age in 10 year will be {age}")