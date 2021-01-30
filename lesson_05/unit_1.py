print('введите строки для файла, для завершения нажмите q')
user_str = ''
user_data = []
while user_str != 'q':
    user_str = input('')
    user_data.append(f"{user_str}\n")

with open('user_1.txt', 'w') as f:
    f.writelines(user_data)
