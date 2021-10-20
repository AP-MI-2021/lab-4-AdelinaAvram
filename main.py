def citireLista():
    '''
    citeste de la tastatura o lista de nr intregi
    :return: lista citita
    '''
    givenString = input ("Dati lista, cu elemente separate prin virgula: ")
    numbersAsString = givenString.split(",")
    l = []
    for x in numbersAsString:
        l.append(int(x))
    return l

def nr_elem_pare (l):
    '''
    determina nr de elemente pare dintr-o lista
    :param l: lista de nr intregi
    :return: nr de elemente pare dintr-o lista
    '''
    cnt = 0
    for x in l:
        if x%2==0:
            cnt = cnt + 1
    return cnt

def test_nr_elem_pare():
    assert nr_elem_pare ([12, 3, 5, 18, 20]) == 3
    assert nr_elem_pare ([0, -4, -3, 12, 15]) == 3

def printMenu():
    print ("1. Citirea a 2 liste de nr intregi")
    print ("2. Verifica daca cele 2 liste citite au acelasi numar de elemente pare")

def main():
    test_nr_elem_pare()
    l1 = []
    l2 = []
    while True:
        printMenu()
        optiune = input ("Dati optiunea: ")
        if optiune == "1":
            n = input ("Apasati 1 daca cititi prima lista si 2 daca o cititi pe a doua: ")
            n = int(n)
            if n==1:
                l1 = citireLista()
            elif n==2:
                l2 = citireLista()
        elif optiune == "2":
            if nr_elem_pare (l1) == nr_elem_pare (l2):
                print ("DA")
            else:
                print ("NU")

main()
