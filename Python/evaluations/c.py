"""
Ariel Pérez
How can be inplement a queue using one list in python:
"""
my_queue = ["a","b","c","d","e"]
#implement the condition to add or erase one element in the queue
number_of_iterations = len(my_queue)
i = 0
for i in range(number_of_iterations):
    erase_add = int(input("write 1 to add new element or 2 to erase the last element, or 3 to finish the program "))

    if erase_add == 1:
        new_element = input("enter the new element ")
    #chosing the list that we will add//.append: metod to add item
        my_queue.append(new_element)
        print(f"the new queue is: {my_queue}")
    elif erase_add == 2:
        #chosing the list that we will add//.pop metod to delete item//
        my_queue.pop(0)
        print(f"the first element of the queue was deleted. \nthe new queue is: {my_queue}")
    elif erase_add == 3:
        print(f"your queue after all changes is: {my_queue}")
        break
    else:
        print("you commit a miskate entering the options, try again")