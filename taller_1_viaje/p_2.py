if __name__ == '__main__':
    # Ask the user 

    user_number = int(input("Put on a number "))
    user_number_2 = int(input("Put the another "))

    # Make the comparition

    if user_number > user_number_2:
        print("The first number is bigger than the second")
    elif user_number < user_number_2:
        print("The second one is the biggest")
    else:
        print("The numbers are equal")
