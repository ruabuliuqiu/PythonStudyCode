#cheng fa biao
#liufang 20200216
i = 1
print("_" * 50)
while i < 11:
    n = 1
    while n <= 10:
        print("{:5d}".format(i * n), end = ' ')
        n += 1
    print()
    i += 1
print("_" * 50)

