# Import the operations

from operations import Operation 

def main():
    i = 0

    print("="*70)
    print("""\n****************BIENVENIDO A LA CALCULADORA MÁS BÁSICA QUE EXISTE***********************\n""")
    print("""Eliga la operación que desea:
    [S] Sumar
    [R] Restar
    [D] Dividir (inexacta) """)

    while i != 1 :
        try:
            desition = input("Elija porfavor: ".upper())
        except ValueError:
            print("Pon una letra porfavor")
            continue
        if desition != ("R" , "S" , "D"):
            i += 1
        else:
            continue

    print(run(desition))


def run(desition):
    op = Operation()
    if desition == "S":
        return op.sumar()
    elif desition == "R":
        return op.restar()
    elif desition == "D":
        return op.dividir()

            

if __name__ == '__main__':
    i = 0
    while i < 1:
        main()
        finish = input("¿Quieres hacer otra operación? [Y] para sí, cualquier letra para cerrar: \n").upper()
        if finish == "Y":
            continue
        else:
            break
