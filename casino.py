import random
from decouple import config


def casino():
    slot_of_win = random.randint(1,31)
    money = config('MY_MONEY', cast=int)
    balance = money
    while True:
        choose_slot = int(input('Выберите слот от 1 до 30: '))
        if choose_slot > 30:
            print('водите от 1 до 30')
        bet = int(input('Поставьте ставку: '))
        if bet > balance:
            print(f'у вас не так много денег ваш ьаланс составляет {balance}')
        if choose_slot == slot_of_win:
            balance += bet * 2
        else:
            balance -= bet

        y_n = input('Хотите продолжить ? y/n')
        if y_n == 'y':
            print(f'выиграшный слот {slot_of_win}')
            print(f'ваш баланс {balance}')
            continue
        elif y_n == 'n':
            print(f'выиграшный слот {slot_of_win}')
            print(f'ваш баланс {balance}')
            break
        else:
            print('Пишите y или n')












