with open('unit_2.txt') as f:
    i = 0
    for line in f:
        i += 1
        print(f"Количество слов в {i}-й строке: {len(line.split(' '))}")
    print(f'Количество строк: {i}')
