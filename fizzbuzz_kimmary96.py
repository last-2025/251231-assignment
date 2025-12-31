for i in range(1, 31 + 1):
    if i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    elif i % 15 == 0:
        print("fizzbuzz")
    else:
        print(i)

