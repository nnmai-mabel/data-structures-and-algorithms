# Divide the array into halves until reach the base case with array of 1 element
# Have we reached the end of any of the arrays?
#     No:
#         Compare current elements of both arrays 
#         Copy smaller element into sorted array
#         Move pointer of element containing smaller element
#     Yes:
#         Copy all remaining elements of non-empty array

def merge_sort(array):

    # Check if array has more than 1 elements to split
    if len(array) == 1:
        return
    
    # Find the middle index and split the array into 2 halves, left and right
    mid = len(array) // 2
    left = array[:mid]
    right = array[mid:]

    # Call the merge_sort recursively to continue finding a splitting each sub array
    # into smaller ones until they have 1 element in each sub array
    merge_sort(left)
    merge_sort(right)

    # Create an array to store sorted values and its current index
    # and default it to the array to be sorted to get the size, then replace with values
    merged_array = array
    m = 0

    # Create 2 indices, l and r to represent current pointer in each array
    # Compare each element in left and right array to find out the smaller one
    # and fill it to an empty array, then increment the pointer of the array that
    # has smaller values, keep going until 1 array becomes empty, paste all
    # remaining values of the other array into the merged_array
    l = 0
    r = 0

    # Exit the loop when 1 array becomes empty
    while l < len(left) and r < len(right):
        
        # Get the smaller value and copy into merged_array
        if left[l] < right[r]:
            merged_array[m] = left[l]
            l += 1
        else:
            merged_array[m] = right[r]
            r += 1

        # Increment index of the merged_array
        m += 1
    
    # If right array becomes empty, copy all values remaining from left array
    while l < len(left):
        merged_array[m] = left[l]
        l += 1
        m += 1

    # If left array becomes empty, copy all values remaining from right array
    while r < len(right):
        merged_array[m] = right[r]
        r += 1
        m += 1
    
    return merged_array

print(merge_sort([1, 9, 5, 7, 2, 8, 3, 4, 6]))
