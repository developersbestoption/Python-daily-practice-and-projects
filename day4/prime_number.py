number = int(input("Enter the number: "))

if number <= 1:
    print(f"{number} is not a prime number")
else:
    switch = True

    for i in range(2, number):
        if number % i == 0:
            switch = False
            break

    if switch:
        print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")