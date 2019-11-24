def is_odd(i):
    if (i % 2) == 0:
        return False
    else:
        return True

def collatz(nummer):
    if is_odd(nummer):
        return (3 * nummer) + 1
    else:
        return (nummer // 2)

n = int(input("Geef een getal: "))

while n > 1:
    print(collatz(n))
    n = collatz(n)
