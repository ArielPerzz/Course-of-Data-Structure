"""
Ariel Pérez
which is the best choise of data structure to implement one pile.
explain why. 
"""
my_pile = ["a","b","c","d","e"]
print(f"the pile is: {my_pile}")
number_of_iterations = len(my_pile)
i=0
#erase_add = int(input("write 1 to add new element or 2 to erase the last element or 3 to finish"))
for i in range(number_of_iterations):
    erase_add = int(input("write 1 to add new element or 2 to erase the last element or 3 to finish: "))
    if erase_add == 1:
        new_element = input("enter the new element ")
        my_pile.append(new_element)
        print(f"the new pile is: {my_pile}")
    elif erase_add == 2:
        my_pile.pop()
        print(f"the last element of the pile was deleted. \nthe new pile is: {my_pile}")
    elif erase_add == 3:
        print(f"your pile after all changes is: {my_pile}")
        break
