from functions_6 import open_file, wybór_stopnia, add_core

a0 = input('Wpisz tekst: ')
b0 = open_file()
a1 = a0.split(' ')


while True:
    choice0 = input("""W jaki sposób chcesz usunąć wulgaryzmy w tekście? 
        0 - usunąć cały wyraz;
        1 - pozostawić pierwszą literę;
        2 - pozostawić pierwszą i ostatnią literę;
    Wybór: """)
    if choice0 == '0' or choice0 == '1' or choice0 == '2':
        result0 = wybór_stopnia(choice0,a1,b0)
        break
    else:
        print('Podaj poprawnie wybrany wariant.')
        print("\n")

print(f'\nTekst oryginalny: \n{a0}')
print(f'\n\nTekst po wprowadzeniu wstępnej korekty: \n{result0}')


while True:
    choice = input('\nCzy chcesz poddać tekst dalszym modyfikacjom (T/N)? ')
    choice = choice.upper()
    if choice == 'T':
        add_core(result0)
        b0 = open_file()
        result0 = wybór_stopnia(choice0,a1,b0)
        print(f'\nTekst po dodatkowych modyfikacjach: \n{result0}')
    elif choice == 'N':
        print(f'\n\nOstateczna wersja tekstu:\n{result0}')
        break