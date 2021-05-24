# Primero una solución con recursividad

def atpower(n):
    if n == 1 or n == 0:
        return 1
    return n**3+atpower(n-1)


#Una función con if, pero que utiliza otra función ¯\_(ツ)_/¯
def true_solution(n):
    if n == 1 or n == 0 :
        return n
    elif n == 2:
        return atpower(n)
    elif n == 3:
        return atpower(n)
    elif n == 4:
        return atpower(n)
    elif n == 5:
        return atpower(n)
    elif n == 6:
        return atpower(n)
    elif n == 7:
        return atpower(n)
    elif n == 8:
        return atpower(n)
    elif n == 9:
        return atpower(n)
    elif n == 10:
        return atpower(n)
    elif n == 11:
        return atpower(n)

if __name__ == '__main__':
    
    i = ''
    while i != 'R' and 'N' :
        print("Hola profe, eliga porfavor cuál modo le gustaría")
        i = input("Modo recursivo[R], modo novato [N]: ")
        i = i.capitalize()

    if i == 'R':
        j = atpower(int(input("Escriba el número ")))
        print(f"Sigma de los números al cubo: {j}")
    elif i == 'N':
        j = true_solution(int(input("Escriba el número")))
        print(f"Sigama de los número al cubo: {j}")

    print("#"*50) 
    print(""" Recuerde checar el repositorio del trabajo en: 
             https://github.com/u-m-i/SENA_tasks.git""")



