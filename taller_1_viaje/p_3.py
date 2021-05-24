if __name__ == '__main__':

    # Ask again to the user, 'bout 4 numbers
    a = int(input("Hello\n pls enter a integer number "))
    b = int(input("a second of the same type "))
    c = int(input("and a third "))
    # Remember the float one
    d = float(input("Now a float number "))

    # Make the comparition
    if a > b and a > c and a > d:
        print(f"The first:{a} is the major")
    elif b > a and b > c and b > d:
        print(f"The biggest one is the second: {b} number")
    elif c > a and c > b and c > d:
        print(f"The upper one is the third : {c}")
    elif d > a and d > b and d > c:
        print(f"The fourth: {d} is the first tier")
    elif a == b and a > c and a > d:
        print(f"The second {b} and the first {a} are the biggest numbers")
    elif a == c and a > b and a > d:
        print(f"The third {c} and the first {a} are the top numbers ")
    elif a == d and a > c and a > b:
        print(f"The first {a} and the last number {d} are the biggest numbers")
    elif b == c and b > a and b > d:
        print(f"Second {b} and thirds {c} both are the major numbers")
    elif b == d and b > a and b > c:
        print(f"Second {b} and fourth {d} number are the biggest numbers")
    print("#"*50)
    print(""" Recuerde checar todo el trabajo en mi repositorio
	   https://github.com/u-m-i/SENA_tasks.git""")
