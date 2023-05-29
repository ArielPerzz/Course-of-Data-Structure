"""
comprove if the word is palindrome
use piles and te metod (reverse) to do this exercices
"""
#we use tuples to enter one word
tupla = input("enter te word to know if it's palindrome: ")
#here the comand "list" was used to transform the characters to elements in te list
pile_word = list(tupla)
print(f"The word that you wrote was: {pile_word}")
reverse_pile_word = pile_word.copy()
#we use this metod to reverse te copy of the original word
reverse_pile_word.reverse() #don't forget the parentesis in the end.
print (f"The same word in reverse is: {reverse_pile_word}")
if reverse_pile_word == pile_word:
    print("the word that u gave us is palindrome")
else:
    print("the word that you gave us isn't palindrome")