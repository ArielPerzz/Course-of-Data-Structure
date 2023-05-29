"""
verify if the list is sort in ascendant order
browse the list and compare every element with the next one.
if some element is major than the last one, the list will not be ordered in ascendant form
"""
my_list = [1, 3, 4, 5, 6, 7, 8]
is_sorted = True
#use of one for to compare the elements with each other

for i in range(len(my_list)-1):
    #use if to comprove if the list is sorted
    if my_list[i] > my_list[i+1]:
        is_sorted = False
        break

if is_sorted:
    print("The list is sorted in ascending order")
else:
    print("The list is not sorted in ascending order")

