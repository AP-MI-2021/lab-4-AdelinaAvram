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

def intersectie (l1, l2):
    '''
    afiseaza lista obtinuta prin intersectia a doua liste
    :param l1: lista de nr intregi
    :param l2: lista de nr intregi
    :return: lista obtinuta prin intersectia celor doua liste
    '''
    l = []
    for x in l1:
        if l2.count(x)>=1:
            l.append(x)
    return l

def test_intersectie ():
    assert intersectie ([12, 22, 36, 424], [22, 23, 36, 55, 424]) == [22, 36, 424]
    assert intersectie ([11, 13, 7, 9], [20, 21, 33, 7, 9]) == [7, 9]
    assert intersectie ([1, 2], [3, 4]) == []

def palindrom(n):
    '''
    verifica daca nr n este palindrom
    :param n: nr intreg
    :return: True, daca n este palindrom si False, in caz contrar
    '''
    s = str(n)
    oglindit = s[::-1]
    if s==oglindit:
        return True
    return False

def test_palindrom ():
    assert palindrom (2332) is True
    assert palindrom (15351) is True
    assert palindrom (56) is False
    assert palindrom (3335) is False
    assert palindrom (1) is True

def lista_palindroame (l1, l2):
    '''
    Determina lista palindroamelor obtinute prin concatenarea elementelor de pe aceleasi pozitii in cele doua liste l1 si l2
    :param l1: lista de nr intregi
    :param l2: lista de nr intregi
    :return: lista palindroamelor obtinute prin concatenarea elementelor de pe aceleasi pozitii in cele doua liste l1 si l2
    '''
    if len(l1)<=len(l2):
        L = len (l1)
    else:
        L = len(l2)
    l = []
    for i in range (L):
        s1 = str(l1[i])
        s2 = str(l2[i])
        s = s1 + s2
        s = int(s)
        if palindrom(s):
            l.append(s)
    return l

def test_lista_palindroame ():
    assert lista_palindroame ([12, 22, 36, 11], [21, 23, 63, 55, 424]) == [1221, 3663]

def inlocuire_cu_oglindit (l, div):
    '''
    determina lista obtinuta prin inlocuirea elementelor divizibile cu elementele listei div cu oglinditul lor
    :param l: lista de nr intregi
    :param div: lista de nr intregi
    :return: lista obtinuta prin inlocuirea elementelor divizibile cu elementele listei div cu oglinditul lor
    '''
    for i in range (len(l)):
        x = l[i]
        ok = 1
        for j in range (len(div)):
            if x%div[j]!=0:
                ok = 0
        if ok == 1:
            oglindit = (str(x))[::-1]
            x = oglindit
            x = int(x)
            l[i] = x
    return l

def test_inlocuire_cu_oglindit ():
    assert inlocuire_cu_oglindit ([12, 22, 36, 363], [1, 2, 3, 4]) == [21, 22, 63, 363]
    assert inlocuire_cu_oglindit ([22, 23, 36, 55, 363], [1, 2, 3, 4]) == [22, 23, 63, 55, 363]

def printMenu():
    print ("1. Citirea a 2 liste de nr intregi")
    print ("2. Verifica daca cele 2 liste citite au acelasi numar de elemente pare")
    print ("3. Determina intersectia celor doua liste")
    print ("4. Determina lista palindroamelor obtinute prin concatenarea elementelor de pe aceleasi pozitii in cele doua liste ")
    print ("5. Afiseaza listele l1 si l2 in care elementele divizibile cu toate elementele din lista l3 sunt inlocuite cu oglinditul lor")
    print ("x. Iesire")

def main():
    test_nr_elem_pare()
    test_intersectie()
    test_palindrom()
    test_lista_palindroame()
    test_inlocuire_cu_oglindit()
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
        elif optiune == "3":
            print (intersectie(l1, l2))
        elif optiune == "4":
            print (lista_palindroame(l1, l2))
        elif optiune == "5":
            l3 = citireLista()
            l1 = inlocuire_cu_oglindit (l1, l3)
            l2 = inlocuire_cu_oglindit (l2, l3)
            print (l1)
            print (l2)
        elif optiune == "x":
            break
        else:
            print ("Optiune gresita. Reincercati!")
            
main()
