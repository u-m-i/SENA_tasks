# Function to determinate the player status

def liga(age,accurate):

    if age >= 18 and age <= 22 and accurate >= 80:
        return f"Bro felicitaciones puedes pertenecer a: LIGA PROFESIONAL DE FUTBOL"
    elif age >= 18 and age <= 22 and acurate < 80:
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
    

