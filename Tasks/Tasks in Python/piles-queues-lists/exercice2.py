"""
Implement one pile using one list
add the elements in the end, and delete this elements
using the metod "Pop"
"""
my_pile = ["a","b","c","d","e"]
erase_add = int(input("write 1 to add new element or 2 to erase the last element "))
if erase_add == 1:
    new_element = input("enter the new element ")
    my_pile.append(new_element)
    print(f"the new pile is: {my_pile}")
elif erase_add == 2:
    my_pile.pop()
    print(f"the last element of the pile was deleted. \nthe new pile is: {my_pile}")