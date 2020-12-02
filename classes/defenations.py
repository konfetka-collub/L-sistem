def multi(a, b):
    c = a*b
    return c


def OddorNot(a):
    if a % 2 == 0:
        print("Even")
    else:
        print("Odd")


OddorNot(multi(11, 7))
