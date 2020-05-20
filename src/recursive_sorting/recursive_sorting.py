# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    merged_arr = []


    while len(arrA) > 0 and len(arrB) > 0:
        if arrA[0] <= arrB[0]:
            merged_arr.append(arrA[0])
            arrA = arrA[1:]
        else:
            merged_arr.append(arrB[0])
            arrB = arrB[1:]

    return merged_arr + arrA + arrB



# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort(arr):
    # Your code here
    #divide array in half until there are only single elements
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        arrA = arr[:mid]
        arrB = arr[mid:]
        sorted_a = merge_sort(arrA)
        sorted_b = merge_sort(arrB)
        arr = merge(sorted_a, sorted_b)

    #merge them into pairs

    return arr


# def merge_sort(arr):
#     # $%$Start
#     if len(arr) > 1:
#         left = merge_sort(arr[0: len(arr) // 2])
#         right = merge_sort(arr[len(arr) // 2:])
#         arr = merge(left, right)   # merge() defined later
#     # $%$End

#     return arr


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):

    right_start = mid + 1

    if(arr[mid] <= arr[right_start]):
        return arr

    while (start <= mid and right_start <= end):
        print('start', start, 'mid', mid, 'end', end)
        if arr[start] <= arr[right_start]:
            #its already in the right place, so increment l/start
            start +=1
        else:
            value = arr[right_start]
            index = right_start
            # arr.insert(index, value)

            while (index != start): 
                arr[index] = arr[index - 1]; 
                index -= 1; 
              
            arr[start] = value; 

            start+=1
            mid+=1
            right_start+=1

    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here

    if l == r:
        return arr
    else:
        mid = (l + r)//2
        #sorting left half of array
        merge_sort_in_place(arr, l, mid)
        #sorting right half of array
        merge_sort_in_place(arr, mid+1, r)
        arr = merge_in_place(arr, l, mid, r)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr

my_arr = [9,4,6,1,5,3]
# print(merge_sort(my_arr))
print(merge_sort_in_place(my_arr, 0, my_arr[len(my_arr)-1]))