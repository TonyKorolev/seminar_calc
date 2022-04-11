

def get_user_info():
    print('Добавление нового пользователя.')
    user_name = input('Введите имя: ')
    user_surname = input('Введите фамилию: ')
    user_birth_date = input('Укажите дату рождения:')
    user_phone_number = input('Укажите номер телефона: ')
    print('Добавление нового пользователя совершено.')
    return [user_name, user_surname, user_birth_date, user_phone_number]

