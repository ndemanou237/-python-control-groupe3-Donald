
def square(n):
    return n*n

def parity(nbre):
    if(nbre % 2 == 0):
        print(f'le nombre {nbre} est pair')
    else:
        print(f'le nombre {nbre} est impair')   

def mylist(liste):
    for listed in liste:
        print(listed)