# Choose pivot (last element or random)
# All element less than pivot should be on the left of pivot
# Others should be on the right of pivot
# Use 2 indices, i and j (i goes left -> right, j goes right -> left)
# i looks for element > pivot
# j looks for element < pivot
# If find an element at index i that is > pivot, and item at index i is
# < item at index j, swap with element at index j
# When j at left of i, swap pivot with element at index i
# Up til now got everything left of pivot smaller than pivot
# everything right of pivot bigger than pivot
# Call quicksort of subarray to the left and right (not including pivot)
# of the pivot

def quick_sort(array, low, high):
    if low < high:
        partition_pos = partition(array, low, high)
        quick_sort(array, low, partition_pos - 1)
        quick_sort(array, partition_pos + 1, high)
    return array

def partition(array, low, high):
    i = low
    j = high - 1
    pivot = array[high]

    while i < j:
        while i < high and array[i] < pivot:
            i += 1
        while j > low and array[j] >= pivot:
            j -= 1
        
        if i < j:
            temp = array[i]
            array[i] = array[j]
            array[j] = temp
    
    if array[i] > pivot:
        temp2 = array[i]
        array[i] = array[high]
        array[high] = temp2

    return i

array = [1, 9, 5, 7, 2, 8, 3, 4, 6]
print(quick_sort(array, 0, len(array) - 1))

array2 = [11, 19, 15, 17, 12, 18, 13, 14, 16]
print(quick_sort(array2, 0, len(array2) - 1))