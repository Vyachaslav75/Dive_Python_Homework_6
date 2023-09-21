from random import randint as ri
from sys import argv


def ugadayka(min, max, count):
    num = ri(min, max + 1)
    while count > 0:
        temp = int(input("Введите угадываемое число: "))
        if num == temp:
            print("Вы угадали, поздравляем!")
            break
        elif num > temp:
            print("Загаданное число больше.")
        elif num < temp:
            print("Загаданное число меньше.")
        count -= 1
    else:
        print("Вы проиграли.")


if __name__ == "__main__":
    if len(argv) == 1:
        ugadayka(ri(1, 5), ri(50, 100), 10)
    elif len(argv) == 2:
        ugadayka(int(argv[1]), ri(50, 100), 10)
    elif len(argv) == 3:
        ugadayka(int(argv[1]), int(argv[2]), 10)
    elif len(argv) == 4:
        ugadayka(int(argv[1]), int(argv[2]), int(argv[3]))
