class OnlyNumbers:
    numbers_list = []

    @staticmethod
    def add_number(user_number):
        try:
            x = float(user_number)
            OnlyNumbers.numbers_list.append(x)
        except ValueError:
            print('Вы ввели не число!')


u_input = input('Для просмотра результата нажмите Q. Введите число: ')
while u_input != 'Q':
    OnlyNumbers.add_number(u_input)
    u_input = input('Введите число: ')

print(OnlyNumbers.numbers_list)
