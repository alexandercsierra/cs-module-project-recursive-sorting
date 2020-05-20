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



    while len(start) > 0 and len(end) > 0:
        if start[0] <= end[0]:
            merged_arr.append(start[0])
            start = start[1:]
        else:
            merged_arr.append(end[0])
            end = end[1:]

    return arr + start + end


def merge_sort_in_place(arr, l, r):
    # Your code here

    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        start 
        end = arr[r:]
        print('start', start, 'end', end)
        sorted_a = merge_sort_in_place(arr, start[0], end[0])
        arr = merge_in_place(arr, start, mid, end)

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr

my_arr = [9,4,6,1,5,3]
# print(merge_sort(my_arr))
print(merge_sort_in_place(my_arr, 0, my_arr[len(my_arr)-1]))