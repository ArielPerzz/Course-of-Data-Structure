list = []
print (type(list))

list=[1,2,3,4,5]
print(list)

list = ["Ariel",True,2,3.14,4j,["a", "b"],4]
print(list)

list.append("Ariel")
print(list)

list2 = list.copy()
print(list2)

list2.clear()
print(list2)

list2 = ["a", "b", "c", "d", "e"]
print(list2.count("e"))

list2 = ["a", "b", "c", "d", "e", "e"]
print(list2.count("e"))

print(len(list2))

print(list2[4])
print(list2[5])

list2.remove("a")
list2.remove("e")
list2.remove("e")

print(list2)

list2.reverse()
print(list2)

list2.sort()
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

#lista = list(tupla)
#print(lista)
#print(tupla)

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

