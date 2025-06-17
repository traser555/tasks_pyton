a = int(input())
if a > 36 or a < 0:
    print("ошибка ввода")
if a == 0:
    print("зеленый")
if 0 < a <= 10 :
    if a % 2 != 0:
        print("красный")
    else:
        print("черный")
if 10 < a <= 18 :
    if a % 2 != 0:
        print("черный")
    else:
        print("красный")
if 18 < a <= 28:
    if a % 2 != 0:
        print("красный")
    else:
        print("черный")
if 28 < a <= 36 :
    if a % 2 != 0:
        print("черный")
    else:
        print("красный")