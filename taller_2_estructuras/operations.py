#Business model

class Operation:
    def __init__ (self):
        return 

    def sumar(self):

        print("*************SUMA************")
        arg1 = int(input("Ingresa el primer número que quieres sumar: " ))
        print(f"Nuestra se ve así: {arg1} + x ")
        arg2 = int(input("Ingresa el ahora el segundo número por sumar: " ))
        return f"La suma de {arg1} + {arg2} es igual a {arg1+arg2}"
    
    def restar(self):

        print("*************RESTA************")
        arg1 = int(input("Ingresa el primer número que quieres restar: " ))
        print(f"Nuestra se ve así: {arg1} - x ")
        arg2 = int(input("Ingresa el ahora el segundo número por restar: " ))
        return f"La resta de {arg1} - {arg2} es igual a {arg1-arg2}"
    
    def dividir(self):
        print("*************DIVISIÓN************")
        arg1 = int(input("Ingresa el primer número que quieres dividir: " ))
        print(f"\nNuestra se ve así: {arg1} / x  ")
        arg2 = int(input("Ingresa el ahora el segundo número por el que vas a dividir: " ))
        return f"La división de {arg1} / {arg2} es igual a {arg1/arg2}" 
