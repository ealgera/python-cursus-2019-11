lijst_a = [1, 2, 3, 4]
lijst_b = [2, 3, 4, 5]

for a in lijst_a:
    for b in lijst_b:
        if a == b:
            print(b)

gelijke_nrs = [b for a in lijst_a for b in lijst_b if a == b]
print(gelijke_nrs)