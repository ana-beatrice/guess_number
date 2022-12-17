import random
import os

numar_de_ghicit = random.randint(1, 100)
os.system('clear')

while True:
    user_input = input('introdu numarul ghicit: ')

    if user_input == 'Done':
        break

    if user_input.isdigit():
        numar = int(user_input)
    else:
        print('numar invalid! mai incearca.')
        continue

    if numar_de_ghicit == numar:
        print()
        print('**************************')
        print(f'ai ghicit numarul! {numar_de_ghicit}')
        print('**************************')
        print()

        user_input = input('mai vrei sa joci o data? ')

        if user_input.lower() == 'da':
            numar_de_ghicit = random.randint(1, 100)
            os.system('clear')
            continue
        else:
            break
    elif numar_de_ghicit < numar:
        print('numarul este MAI MIC!')
    elif numar_de_ghicit > numar:
        print('numarul este MAI MARE!')
