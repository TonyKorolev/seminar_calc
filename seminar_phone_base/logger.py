# Модуль логирования данных

def log_xml(data):
    with open('seminar_phone_base\\log.xml', 'a') as file:
        res = str(data)
        file.write(f'{res}\n')


    


