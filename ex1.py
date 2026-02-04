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

def main():
   lista_ordinata =  insertion_sort(lista_disordinata)
   print(lista_ordinata)

if __name__ == '__main__':
    main()