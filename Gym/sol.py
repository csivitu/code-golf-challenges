oddmonths = [1, 3, 5, 7, 8, 10, 12]
for i in range(int(input())):
    date = [int(j) for j in input().split(":")]
    if (date[0] % 4 == 0 and date[0] % 100 != 0) or (date[0] % 400 == 0):
        if date[1] == 2:
            print((((29 - date[2]) + 1) % 2) + (((29 - date[2]) + 1) // 2))
        elif date[1] in oddmonths:
            print((((31 - date[2]) + 1) % 2) + (((31 - date[2]) + 1) // 2))
        else:
            print((((30 - date[2]) + 32) % 2) + (((30 - date[2]) + 32) // 2))
    else:
        if date[1] == 2:
            print((((28 - date[2]) + 32) % 2) + (((28 - date[2]) + 32) // 2))
        elif date[1] in oddmonths:
            print((((31 - date[2]) + 1) % 2) + (((31 - date[2]) + 1) // 2))
        else:
            print((((30 - date[2]) + 32) % 2) + (((30 - date[2]) + 32) // 2))