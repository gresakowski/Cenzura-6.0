# funkcja otwierająca plik z istniejącą listą RDZENI SŁOWOTWÓRCZYCH i tworząca listę na jego podstawie
def open_file():
    cores_file = open('rdzenie.txt','r')
    cores = [line.strip() for line in cores_file.readlines()]
    cores_file.close()
    return cores


# funkcja służąca do wybrania sposobu usunięcia słowa:
def wybór_stopnia(choice,a1,b):
    if choice == '0':
        result0 = cenzura0(a1,b)
    elif choice == '1':
        result0 = cenzura1(a1,b)
    elif choice == '2':
        result0 = cenzura2(a1,b)
    return result0


# cenzura0 - wykropkowanie wszystkich znaków cenzurowanego wyrazu
def cenzura0(a1, b0):
    interpunction = ['.', ',', ';', ':', '/', '?', '!', '"', "'", '(', ')', '[', ']', '{', '}', '-', '_', '#', '<', '>']
    a2 = ''
    bc = []
    for a in a1:
        for b in b0:
            if b in a.lower():
                bc.append(a)
            elif b not in a:
                continue
            continue
    for a in a1:
        if a in bc:
            if a[(len(a) - 1)] not in interpunction:
                a = '.' * len(a)
                a2 += (a + ' ')
            else:
                a = '.' * (len(a)-1) + ' ' + a[len(a)-1]
                a2 += (a + ' ')
        else:
            a2 += (a + ' ')
    return a2


# cenzura1 - wykropkowanie wszystkich znaków cenzurowanego wyrazu, z wyjątkiem pierwszego
def cenzura1(a1, b0):
    interpunction = ['.', ',', ';', ':', '/', '?', '!', '"', "'", '(', ')', '[', ']', '{', '}', '-', '_', '#', '<', '>','..','...']
    a2 = ''
    bc = []
    for a in a1:
        for b in b0:
            if b in a.lower():
                bc.append(a)
            elif b not in a:
                continue
            continue
    for a in a1:
        if a in bc:
            if a[(len(a) - 1)] not in interpunction:
                a = a[0] + '.' * (len(a) - 1)
                a2 += (a + ' ')
            else:
                a = a[0] + '.' * (len(a) - 2) + ' ' + a[(len(a) - 1)]
                a2 += (a + ' ')
        else:
            a2 += (a + ' ')
    return a2


# cenzura2 - wykropkowanie wszystkich znaków cenzurowanego wyrazu, z wyjątkiem pierwszego i ostatniego
def cenzura2(a1, b0):
    interpunction = ['.', ',', ';', ':', '/', '?', '!', '"', "'", '(', ')', '[', ']', '{', '}', '-', '_', '#', '<', '>']
    a2 = ''
    bc = []
    for a in a1:
        for b in b0:
            if b in a.lower():
                bc.append(a)
            elif b not in a:
                continue
            continue
    for a in a1:
        if a in bc:
            if a[(len(a) - 1)] not in interpunction:
                a = a[0] + '.' * (len(a) - 2) + a[(len(a) - 1)]
                a2 += (a + ' ')
            else:
                a = a[0] + '.' * (len(a) - 3) + a[(len(a) - 2)] + a[(len(a) - 1)]
                a2 += (a + ' ')
        else:
            a2 += (a + ' ')
    return a2


# funkcja wprowadzająca nowy rdzeń do spisu b0
def add_core(result0):
    a = result0.lower()
    b1 = input('Wpisz rdzeń słowa, które chcesz usunąć: ')
    if b1.lower() in a or b1.capitalize() in a or b1.upper() in a :
        b1 = b1.lower()
        b1 = (f'\n{b1}')
        cenz_file = open('rdzenie.txt', 'a')
        cenz_file.write(b1)
        cenz_file.close()
    else:
        print('Podane słowo nie występuje w tekście lub zostało już z niego usunięte')