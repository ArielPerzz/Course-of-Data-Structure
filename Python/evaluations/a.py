"""
Ariel Pérez
which is the the temporal complexity of search some element in one list?
"""
List_search = [1, 6, 3, 2, 8, 5, 4, 7, 9]
number_of_elements = len(List_search)
i = 0
number_to_search = int(input("enter one number to search in te list. "))
for i in range(number_of_elements):
    if List_search[i] == number_to_search:
        print(f"the number that you search {number_to_search} where in the position: {i} of the list")
        print(f"the complexity of this search was: O({number_of_elements})")
        break
    else:
        print(f"the number that you search {number_to_search} can't be find in the position {i} of the list")
