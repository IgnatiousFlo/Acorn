def binary(n):
    print(bin(n))

binary(9)

# prints odd numbers in a range, makes x odd if it's even.
def odd_nums(x, y):
    odd_list = []
    if x % 2 == 0:
        x  = x - 1
    for i in range(x, y, 2):
        odd_list.append(i)
    print(odd_list)

odd_nums(1, 45)


