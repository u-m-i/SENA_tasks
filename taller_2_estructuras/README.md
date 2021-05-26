# Taller 2:

# Estructuras de control :smiley:

###### Miguel Andrés Rendón Reyes 海
###### RAP28
####### Also see: [docment](https://docs.google.com/document/d/1TyDuHOgzXclkU1_Akw_3DBk6D9O9YdZ4OIZJIh3SFAc/edit?usp=sharing)
****

## Activity 1  :heavy_exclamation_mark:


### A) Realice un código que permita ingresar el producto, cantidad, valor unitario, ciudad de venta. :sleeping:
### Que calcule el valor total de la venta Utilizando un condicional OR Si la ciudad ingresada es Medellín o Cali, dar un descuento de 5% sobre el valor de la venta, para las demás ciudades *no aplica el descuento.* 
*****
#### Code :blue_book:

    def outfit(city_name):
        if city_name == 'Medellin' or city_name == 'Medellín':
            return f" El valor total del producto es {(product_quant*product_value_unit)-(product_quant*product_value_unit)*0.05}"
        else:
            return False
    
    
    if __name__ == '__main__':
        i = ''
        while i != 'Y':
    
            # Product characteristics 
            product_name = input("Nombre del producto: ")
            product_quant = int(input("Cantidad que llevará: "))
            product_value_unit = int(input("Valor por unidad: "))
            product_city = input("Nombre de la ciudad de venta: ").capitalize()
            # Confirmation
            j = outfit(product_city)
            i = input("Escribe Y para confirmar los datos o cualquier letra si quieres reiniciar: ")
    
        if j:
            print(j)
        else:
            print(f"El valor total del producto es {product_quant*product_value_unit} en la ciudad de {product_city}\n")
        print("#"*60)
        print("""Recuerde ver este trabajo completo en:
    https://github.com/u-m-i/SENA_tasks/tree/master/taller_2_estructuras""")

*******

### B)  Cree un código que permita identificar para que programa puede aplicar, los requisitos son los siguientes:
### Si la edad es mayor o igual a 18 y menor o igual a 22 y los puntos de evaluación obtenidos fueron superiores o iguales a 80, pasa para el programa de LIGA PROFESIONAL DE FUTBOL :boy:
### Si la edad es mayor o igual a 18 y menor o igual a 22 y los puntos de evaluación obtenidos fueron menores a 80, pasa para el programa de LIGA SEMIPROFESIONAL

*****
#### Code :blue_book:
    # Function to determinate the player status
    
    def liga(age,accurate):
    
        if age >= 18 and age <= 22 and accurate >= 80:
            return f"Bro felicitaciones puedes pertenecer a: LIGA PROFESIONAL DE FUTBOL"
        elif age >= 18 and age <= 22 and accurate < 80:
            return f"Bro felicitaciones puedes pertencer a: LIGA SEMIPROFESIONAL"
        else:
            return False
    
    
    if __name__ == '__main__':
    
        # Ask to user
    
        user_age = int(input("Porfavor ingrese la edad del jugador entre los 18-22 años: "))
        user_accurate = int(input("Ahora ingrese el puntaje del jugador "))
    
        # Invocate the function into a variable
    
        j = liga(user_age, user_accurate)
    
        if j:
            print(j)
        else:
            print("Por el momento no puedes aplicar a ningún nivel semi o profesinal")
    
        print("#"*60)
        print("""Recuerde ver este trabajo completo en:
    https://github.com/u-m-i/SENA_tasks/tree/master/taller_2_estructuras""")

****
## Activity 2 :sparkle:

### A) Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas. Ejemplo: n=4, Rta/ 4, 3, 2, 1, 0. :electric_plug:
*****
#### Code :blue_book:
****
    if __name__ == '__main__':
    
        n = int(input("Escribe un número entero: "))
        print("cuenta regresiva:")
    
        for i in range(n):
            print(n-i)
    
        print("#"*60)
        print("""Recuerde ver este trabajo completo en:
    https://github.com/u-m-i/SENA_tasks/tree/master/taller_2_estructuras""")
    
### B)   Cree un programa que permita ingresar el nombre de la fruta y que desglose en forma vertical cada carácter de palabra
****
#### Code :blue_book:
****
    def decomp(fruit):
        for i in fruit:
            print(i)
        return "Done!"
    
    if __name__ == '__main__':
    
        # User favorite fruit the mine is the mango
    
        user_fruit = input("Escribe tu fruta favorita bien: ")
        decomp(user_fruit)
    
        print("#"*60)
        print("""Recuerde ver este trabajo completo en:
    https://github.com/u-m-i/SENA_tasks/tree/master/taller_2_estructuras""")
	
## Activity  :three:

### A)  Escriba un programa en Python el cual encuentre todos los números que se encuentren en el rango de 2000 y 8000 estos números también deben ser divisibles por 11 y múltiplos de 5.
 
*****
#### Code :blue_book:
    if __name__ == '__main__':
        my_list = [ i for i in range(2000,8000) if i % 55 == 0]
        print(f"""La lista de número entre el 2000 y el 8000 que son múltiplos de 11 y 55 son 
        {my_list}""")
    
        print("#"*60)
        print("""Recuerde ver este trabajo completo en:
    https://github.com/u-m-i/SENA_tasks/tree/master/taller_2_estructuras""")

### B)  Escriba un programa en python que mediante un ciclo While imprima la siguiente figura:

    
    * 
    * * 
    * * * 
    * * * * 
    * * * * * 
    * * * * 
    * * * 
    * * 
    *
    

 
*****
#### Code :blue_book:
    if __name__ == '__main__':
        i = 9
        j = 1
        k = 4
        while i != 0:
            while j != 6:
                print("* "*j)
                j +=1
            while k != 0 :
                print("* "*k)
                k -=1
            i -= 1
    
    
    
            #j = abs((i*(5-(i-4)))/9)
            #print(f"#"*j)
            #i -= 1
    
        print("#"*60)
        print("""Recuerde ver este trabajo completo en:
    https://github.com/u-m-i/SENA_tasks/tree/master/taller_2_estructuras""")
	
****

### That's it.

### Random art:
<div>
░░▄▄░▄███▄
▄▀▀▀▀░▄▄▄░▀▀▀▀▄
█▒▒▒▒█░░░█▒▒▒▒█
█▒▒▒▒▀▄▄▄▀▒▒▒▒█
▀▄▄▄▄▄▄▄▄▄▄▄▄▄▀
</div>
