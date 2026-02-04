lista_disordinata = [67,9,4,2,6,8,3,5,6,7,8,888,6,453,1]
def insertion_sort(lista):
    for k in range(1,len(lista)):
        elem = lista[k]
        j = k-1
        while j >= 0 and elem < lista[j]:
            lista[j+1] = lista[j]
            j -=1
        lista[j+1] = elem
    return lista

def bubble_sort(lista):
    n = len(lista)
    j = 0
    ordinato = False
    while j < n-1 and not ordinato:
        ordinato = True
        i = n-1
        while j < i:
            if lista[i] < lista[i-1]:
                lista[i], lista[i-1] = lista[i-1], lista[i]
                ordinato = False
            i -=1
        j +=1
    return lista


def binary_search(lista,target):
    inf = 0
    sup = len(lista)-1
    mid = (sup + inf) // 2
    i = 0
    while inf <= sup:
        i +=1
        if target == lista[mid]:
            return mid,i
        elif target < lista[mid]:
            sup = mid -1
        else:
            inf = mid +1
        mid = (sup + inf) // 2
    return -1




def main():
    print(insertion_sort(lista_disordinata))
    lista_ordinata = bubble_sort(lista_disordinata)
    print(lista_ordinata)
    target = int(input('inserisci un numero da ricercare: '))
    print(binary_search(lista_ordinata,target))
if __name__ == '__main__':
    main()