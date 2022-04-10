from datetime import datetime as dt

def html_logger(*args):
    time = dt.now().strftime('%H:%M:%S')
    data = ""
    for i in range(len(args)):
        data += f'{args[i]}'
        if i == len(args) - 2: data += '='
    
    
    with open('seminar_calc//log.html', 'a') as file:
        file.write(f'Time: {time} Calc_action: {str(data)}\n')

