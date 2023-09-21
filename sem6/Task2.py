def zagadka(zagadk, answers, count=5):
    print(zagadk)
    answers = list(map(lambda x: x.lower(), answers))
    num = 1
    while num < count:
        answ = input("Введите ответ: ").lower()
        if answ in answers:
            print(f"Угадали с {num} раза")
            break
        else:
            num += 1


def zagadki():
    zagad_dict = {
        'Зимой и летом одним цветом.': ['ель', 'ёлка', 'ёлочка'],
        'Не лает не кусает, а дом не пускает': ['замок', 'замочек']
    }
    for key, item in zagad_dict.items():
        zagadka(key, item, 10)


if __name__ == "__main__":
    zag = 'Зимой и летом одним цветом.'
    answ = ['ель', 'ёлка', 'ёлочка']
    zagadka(zag, answ, 5)
    zagadki()
