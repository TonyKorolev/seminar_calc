import datetime as dt

def html_logger(*args):
    time_stamp = dt.datetime.now()
    data = ""
    for i in range(len(args)):
        data += f'{args[i]}'
        if i == len(args) - 2: data += '='
    
    
    with open('log.html', 'a') as file:
        file.write(f'Time: {time_stamp} Calc_action: {str(data)}\n')

