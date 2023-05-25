primerNumero = input("por favor, ingrese algo: ")
try: 
    primero =int(primerNumero)
except:
    primero = "cadena"
segundoNumero = input("por favor, ingrese algo: ")
try: 
    segundo =int(segundoNumero)
except:
    segundo = "cadena"
if primero == "cadena" or segundo == "cadena":
    print("ingreso mal un dato, pruebe por favor una vez mas ingresando numeros ")
else:
    print(primero + segundo)

