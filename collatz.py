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

while collatz(n) != 1:
    print(str(n).rjust(3), collatz(n))
    n = collatz(n)

print(str(n).rjust(3), collatz(n))