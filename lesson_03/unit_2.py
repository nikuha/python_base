def print_user_data(name, last_name, birth_year, city, email, phone):
    print(f'имя: {name}', f'фамилия: {last_name}', f'год рождения: {birth_year}', f'город проживания: {city}', f'email: {email}', f'телефон: {phone}', sep='\n')


print_user_data('Bob', 'Smith', 1989, 'New York', 'bob@gmail.com', '123456')