"""
With the knowledge about one string with n characters,
please, create one function that count how many characters exists in de word

"""
simetric_pile = [1,2,2,1]
s = int(len(simetric_pile)/2)
#implementing the concept of slicing of one list
a = simetric_pile[:s][::-1]
b = simetric_pile[s:]
#using the ternary operator 
(print("it's asimetric") ) if (len(simetric_pile)%2==1) else (print("it's simetric") if a==b else print("it's simetric"))

