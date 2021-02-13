class Date:
    @classmethod
    def split_date(cls, date):
        try:
            d, m, y = [int(x) for x in date.split('-')]
        except:
            return {'error': 'Дата неверного формата!'}
        return {'d': d, 'm': m, 'y': y}

    @staticmethod
    def check_date(date):
        split_date = Date.split_date(date)
        if 'error' in split_date:
            return split_date
        if not 1 <= split_date['m'] <= 12:
            return {'error': 'Неверный месяц'}
        # можно еще расширить проверку на 30 или 31 день в месяце
        # 28/29 для февраля + проверка високосного года
        if not 1 <= split_date['d'] <= 31:
            return {'error': 'Неверное число'}
        return {'success': f'Дата {date} верная'}



date_1 = Date()
print(date_1.split_date('01-05-2020'))

print(Date.check_date('24-01-2020'))

print(Date.check_date('32-02-2020'))

print(Date.check_date('07-22-2020'))
