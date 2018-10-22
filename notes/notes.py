from datetime import datetime

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


def time_left():
    today = datetime.today()
    str_today = today.strftime("%d %B %Y")
    moving = datetime(2019, 6, 15)
    str_moving = moving.strftime("%d %B %Y")
    diff = abs(today - moving).days

    print(f"Today is {str_today} and I move on {str_moving} , which is in {diff} days")


time_left()
