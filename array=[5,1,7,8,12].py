def insertion_sort(array):
    for i in range(1, len(array)):
        posicion= array[i]
        j=i-1
        
        while j>=0 and posicion < array[j]:
            array[j+1]=array[j]
            j -=1
        array[j+1]=posicion
    return array

list=[5,1,8,9,2]
print(list)
list_ordenada = insertion_sort(list)
print(list_ordenada)