c0 = int(input('Enter a number: '))

if c0 > 1:  # if number greater than 0
    steps = 0
    while c0 != 1:
        if c0 % 2 != 0:  # if odd number
            cnew = 3 * c0 + 1
        else:
            cnew = c0 // 2  # if even number
        print(c0)
        c0 = cnew
        steps += 1
    print("steps =", steps)

else:
    print("You need to enter a number greater than 0.")
