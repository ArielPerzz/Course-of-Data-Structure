lista1 = []
print (type(lista1))

lista1 =[1,2,3,4,5]
print(lista1)

lisa1 = ["Ariel",True,2,3.14,4j,["a", "b"],4]
print(lista1)

lista1.append("Ariel") #agrega un elemento al final de la lista
print(lista1)

list2 = lista1.copy() #copia la lista en otra mas para modificarla y no dañar la original.
print(list2)

list2.clear() #borra todos los elementos de la lista
print(list2)

list2 = ["a", "b", "c", "d", "e"]
print(list2.count("e")) #cuenta los elementos de la lista ubicados en el parentesis
#devuelve el valor en numeros

list2 = ["a", "b", "c", "d", "e", "e"]
print(list2.count("e")) #aqui se ve un ejemplo de la linea 20.

print(len(list2)) #imprime el tamaño de la lista. o la cantidad de elementos que en ella existen

print(list2[4]) #imprime el elemento de la lista que esta entre parentesis
print(list2[5])

list2.remove("a")  
list2.remove("e") #elimina un solo elemento de la lista 
list2.remove("e")

print(list2)

list2.reverse() #da la vuelta a la lista, la pone en reversa
print(list2)

list2.sort() #arregla la lista, la ordena en orden ascendente
print(list2)

list2 = ["a", "b", "B", "c"]
list2.sort()
print(list2)

tupla = ("quito", "guayaquil", "cuenca", "quito")
print(type(tupla))
print(tupla)
#tomar en cuenta esto 
tupla2 = set(tupla)
print(type(tupla2))
print(tupla2)

#tupla.append("machala")
#print(tupla)

print(tupla.count("quito"))
print(tupla.count("cuenca"))
#print(tupla.index("quito"))

lista = list(tupla)
print(lista)
print(tupla)

rango = range(5, 10, 2)
print(type(rango))
print(rango)

#sets
conjunto = {"i", "a", "e", "o", "u", "i", "i", "o", "p" }
print(type(conjunto))
print(conjunto)

#diccionarios 
client001 = {"nombre":"Ariel", "apellido":"perez", "telefono":"0963680863", "correo":"amprez5@espe.edu.ec"}

print(client001["nombre"])
print(client001["apellido"])

print(client001.get("telefono"))
client001["nombre"] = "Mateo"
print(len(client001))

client001.popitem()
print(client001)

client001.pop("apellido")
print(client001)

del client001["telefono"]
print(client001)

perros = {
    "Tobby":{
    "name": "Tobby",
    "age": 6
    },
    "Leo":{
    "name": "Leo",
    "age": 1
    }
}
print(perros)

perritos = dict(name="Rocky", age=7)
print(perritos)

perros["Rokcky"] = perritos
print(perros)

# Bolean

mayorEdad = True
open = False

