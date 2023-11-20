import random
import os
import threading

def get_input():
    try:
        global answer
        answer = float(input('Respuesta: '))
        return answer # Este return no es necesario.
    except ValueError:
        pass
if __name__ == '__main__':
    signs = {'suma':'+', 'resta':'-', 'multipicación':'*', 'división':'/'}
    count = 0

    os.system('cls') 
    print('¡¡¡A CALCULAR!!!')

    while True:
        difficult = int(count/5)
        x = random.randint(0, 10*(difficult+1)-1)
        if difficult % 2:   y = random.randint(0, 10*(difficult)-1)
        else:               y = random.randint(0, 10*(difficult+1)-1)

        sign = random.choice(list(signs.keys()))
        if sign == 'resta' and x < y:
            x, y = y, x
        elif sign == 'división' and y == 0:
            y = 1
        
        print(f'¿Cuánto es {x} {signs[sign]} {y}?')
        thread = threading.Thread(target=get_input)
        thread.start()
        thread.join(3)
        if thread.is_alive():
            print('Te has pasado de tiempo.')
            print(f'La respuesta es {round(eval(f"{x}{signs[sign]}{y}"), 2)}.')
            print(f'Has acertado {count} veces.')
            break

        if answer == round(eval(f'{x}{signs[sign]}{y}'), 2):
            os.system('cls') # Windows, para linux usar 'clear'. Para Mac OS mejor no usar. 
            print(f'¡Correcto!')
            count += 1
        else:
            print(f'Incorrecto. La respuesta es {round(eval(f"{x}{signs[sign]}{y}"), 2)}.')
            print(f'Has acertado {count} veces.')
            break