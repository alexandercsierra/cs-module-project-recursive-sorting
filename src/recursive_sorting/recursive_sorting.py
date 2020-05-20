# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    merged_arr = []

    #while there are elements in both arrays continue to execute, because once one is empty we can just assume the others are in order and can append them directly
    while len(arrA) > 0 and len(arrB) > 0:
        #compare the first elements of each array. These are guaranteed to be the lowest values, since they are already sorted. If the first element from arrA is lower or equal to the first element of arrB, append this value to our merged array. But we have to make sure we aren't accounting for it twice, so we truncate it to exclude the value we added to the merged array
        if arrA[0] <= arrB[0]:
            merged_arr.append(arrA[0])
            arrA = arrA[1:]
        #do the same (but opposite) for arrB
        else:
            merged_arr.append(arrB[0])
            arrB = arrB[1:]
    #exit the while loop when either arrA or arrB is empty. Add their contents onto the merged array. Adding an empty array will do nothing, and we can add the remaining contents of the other array because it was already sorted. This way, there doesn't need to be a conditional to check which is empty, just add both and empty array won't hurt anything.
    return merged_arr + arrA + arrB



# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    #divide array in half until there are only single elements
    if len(arr) <= 1:
        return arr
    else:
        #find middle index
        mid = len(arr)//2
        #split left and right halves along middle index
        arrA = arr[:mid]
        arrB = arr[mid:]
        #define left and right arrays after breaking down to single elements
        sorted_a = merge_sort(arrA)
        sorted_b = merge_sort(arrB)
        #pass into merge function for final sorting
        arr = merge(sorted_a, sorted_b)

    #merge them into pairs

    return arr



# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):

    #define a variable for the start of the right half for clarity
    right_start = mid + 1

    #while the left half is not empty, (l has not exceeded its end point of mid), and the right half is not empty, (r has not exceeded its end point of end), continue
    while (start <= mid and right_start <= end):

        #check if the lowest value from the left side is less than or equal to the lowest value from the right side. If yes, there is no movement to be done, the value is already in the correct position, but we need to move the start pointer to move on to the next comparison
        if arr[start] <= arr[right_start]:
            #its already in the right place, so increment start
            start +=1
        #otherwise, the lowest element in the right half is greater than the lowest element in the left half. In this case we need to move this to the position of the start element, and shift everything else over. I've done this by inserting that value where start was, and then deleting the element where it existed before (plus 1 to account for everything shifting over 1 index)
        else:
            value = arr[right_start]
            index = right_start
            arr.insert(start, value)
            del arr[index+1]
              
           
            #As of here, the start would be pointing to the newly inserted value, so it needs to be incremented by 1. The mid and right_start should stay the same, but everything has shifted 1 index, so they also need to be incremented
            start+=1
            mid+=1
            right_start+=1

    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here
    #base case is when l and r are the same element (the subarray contains one item) or the array passed in is empty (which by default is already sorted)
    if l == r or len(arr) == 0:
        return arr
    else:
        #the midpoint of the subarray should be the beginning (marked by l) and end (marked by r) divided by 2 (floor)
        mid = (l + r)//2
        #sorting left half of array, its starting point represented by l, and its ending point represented by the mid point
        merge_sort_in_place(arr, l, mid)
        #sorting right half of array, its starting point represented by one greater than the left half's ending point, mid +1, and its ending point represented by r
        merge_sort_in_place(arr, mid+1, r)
        #merging the sorted halves, here still technically a part of arr, but represented by l, mid, and r pointers
        arr = merge_in_place(arr, l, mid, r)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr

