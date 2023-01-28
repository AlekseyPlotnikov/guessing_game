from random import randint
from math import ceil, log2


def is_valid(num, x, y):
    return num.isdigit() and x <= int(num) <= y


def num_input(x, y):
    print(f'Введите целое число от {x} до {y}:')
    while True:
        num = input()
        if is_valid(num, x, y):
            return int(num)
        else:
            print(f'А может быть все-таки введем целое число от {x} до {y}?')


def continue_game():
    ans = input('Если хотите повторить ещё раз введите "да"\n').lower()
    if ans == 'да':
        return True
    else:
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
        return False


def count_attempt(x, y):
    return ceil(log2(y - x))


def compare_game(attempt, x, y):
    a = randint(x, y)
    total = 0
    while True:
        num = num_input(x, y)
        total += 1
        attempt -= 1
        if num < a and attempt > 0:
            print(f'Ваше число {num} меньше загаданного. Осталось {attempt} попыток.')
            print('Попробуйте еще разок.')
        elif num > a and attempt > 0:
            print(f'Ваше число {num} больше загаданного, Осталось {attempt} попыток.')
            print('Попробуйте еще разок.')
        elif num == a and attempt >= 0:
            print(f'Вы угадали, поздравляем!, Загаданное число: {num}. Попыток: {total}')
            break
        else:
            print(f'Попытки закончились. Загаданное число: {a}')
            break


def game():
    print('Добро пожаловать в числовую угадайку')
    while True:
        print('Введите диапозон, от скольки до скольки будем угадывать:')
        x, y, = int(input()), int(input())
        if x > y:
            x, y = y, x
        attempt = count_attempt(x, y)
        print(f'Колличество попыток {attempt}')
        compare_game(attempt, x, y)
        if continue_game():
            continue
        else:
            break


game()
