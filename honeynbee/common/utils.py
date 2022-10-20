def takeInput():
    while True:
        try:
            n = int(input("Enter the number of bees in the hive : "))
        except ValueError:
            print("Enter a valide number positive number")
            continue
        if n <= 0:
            print("Enter a valide number positive number")
            continue
        break
    pop = n
    while True:
        try:
            n = int(input("Enter the number of flowers in the field : "))
        except ValueError:
            print("Enter a valide number positive number (less than 999)")
            continue
        if n >= 999:
            print("Enter a valide number positive number (less than 999)")
            continue
        break
    flowercount = n
    while True:
        try:
            n = int(input("Enter the number of generation : "))
        except ValueError:
            print("Enter a valide number positive number (less than 999)")
            continue
        break
    gen = n
    return (pop, flowercount, gen)