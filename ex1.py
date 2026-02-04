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
def main():
    print(insertion_sort(lista_disordinata))
    print(bubble_sort(lista_disordinata))

if __name__ == '__main__':
    main()