class Warehouse:
    equipments = []

    @staticmethod
    def send_to_warehouse(new_item, amount):
        try:
            existent_record = next(record for record in Warehouse.equipments if record['item'].id == new_item.id)
            existent_record['amount'] += amount
        except StopIteration:
            Warehouse.equipments.append({'item': new_item, 'amount': amount})

    @staticmethod
    def print_equipments():
        for record in Warehouse.equipments:
            print(f"Количество: {record['amount']}, Товар: {record['item']}")
        

class Equipment:
    current_id = 1
    ids = []
    equipments = []
    name = 'Оргтехника'

    def __init__(self, model, color):
        self.model = model
        self.color = color
        while Equipment.current_id in Equipment.ids:
            Equipment.current_id += 1
        self.id = Equipment.current_id
        Equipment.ids.append(Equipment.current_id)
        Equipment.equipments.append(self)
        
    def __str__(self):
        return f'id: {self.id}: {self.name} {self.model}, цвет: {self.color}'

    @staticmethod
    def print_equipments():
        for item in Equipment.equipments:
            print(item)


class Printer(Equipment):
    name = 'Принтер'


class Scanner(Equipment):
    name = 'Сканер'


class Xerox(Equipment):
    name = 'Ксерокс'


item_1 = Printer('Samsung', 'черный')
item_2 = Printer('Epson', 'серый')
item_3 = Scanner('HP', 'белый')
item_4 = Scanner('Canon', 'черный')
item_5 = Scanner('Epson', 'белый')
item_6 = Xerox('Xerox', 'серый')

# вся оргтехника
print('Вся оргтехника: ')
Equipment.print_equipments()

print('\nДля просмотра результата нажмите Q.')
chosen_item = None
get_id_text = 'Введите id товара для отправки на склад: '
get_amount_text = 'Введите количество товаров, отправляемых на склад: '
u_input = input(get_id_text)
while u_input != 'Q':
    try:
        user_item_id = int(u_input)
        chosen_item = next(item for item in Equipment.equipments if item.id == user_item_id)
    except ValueError:
        print('Неверно введен id')
        u_input = input(get_id_text)
    except StopIteration:
        print('Товар с таким id не найден')
        u_input = input(get_id_text)
    else:
        print(f'Выбран товар: {chosen_item}')
        chosen_amount = 0
        u_input = input(get_amount_text)
        while u_input != 'Q' and not chosen_amount:
            try:
                chosen_amount = int(u_input)
                if chosen_amount < 1:
                    chosen_amount = 0
                    raise ValueError
            except ValueError:
                print('Неверно введено количесво')
                u_input = input(get_amount_text)
            else:
                Warehouse.send_to_warehouse(chosen_item, chosen_amount)
                print(f'Добавлено!')
                u_input = input(get_id_text)


# то что на складе
print('\nНа складе: ')
Warehouse.print_equipments()


