def bubble_sort(array):
    swapped = True
    while swapped:
         swapped = False
         for i in range(len(array)-1):
             if array[i] > array[i+1]:
                 array[i], array[i+1] = array[i+1], array[i]   
                 swapped = True

def selection_sort(array):
    for i in range(len(array)):
        minimum_index = i 
        minimum = array[i]
        for x in range(i, len(array)):
            if array[x] < minimum:
                minimum = array[x]
                minimum_index = x
        array.pop(minimum_index)
        array.insert(i, minimum)



    
    
arr = [1,4,5,2,3,6]
selection_sort(arr)
print(arr)