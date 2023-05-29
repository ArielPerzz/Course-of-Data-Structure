"""
Implement one queue using one list.
add the elements in the end of the queue using metod (append)
and delete elements of the queue using metod (pop(0))
"""
my_queue = ["a","b","c","d","e"]
#implement the condition to add or erase one element in the queue
erase_add = int(input("write 1 to add new element or 2 to erase the last element "))

if erase_add == 1:
    new_element = input("enter the new element ")
    #chosing the list that we will add//.append: metod to add item
    my_queue.append(new_element)
    print(f"the new queue is: {my_queue}")
elif erase_add == 2:
    #chosing the list that we will add//.pop metod to delete item//
    my_queue.pop(0)
    print(f"the first element of the queue was deleted. \nthe new pile is: {my_queue}")
else:
    print("you commit a miskate entering the options")