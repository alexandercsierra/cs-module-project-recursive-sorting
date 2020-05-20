# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    merged_arr = []

    # Your code here
    # print('a', arrA, 'b', arrB)
    # sorted_a = merge_sort(arrA)
    # sorted_b = merge_sort(arrB)
    # print('sorted_a', sorted_a, 'sorted_b', sorted_b)


    while len(arrA) > 0 and len(arrB) > 0:
        if arrA[0] <= arrB[0]:
            merged_arr.append(arrA[0])
            arrA = arrA[1:]
        else:
            merged_arr.append(arrB[0])
            arrB = arrB[1:]

    return merged_arr + arrA + arrB

    # j=0
    # for i in range(0,len(merged_arr),2):
    #     print('i', i)
    #     if j < len(sorted_a) and j < len(sorted_b):
    #         if sorted_a[j] > sorted_b[j]:
    #             merged_arr[i] = sorted_b[j]
    #             merged_arr[i+1] = sorted_a[j]
    #             j+=1
    #         else:
    #             merged_arr[j] = sorted_a[j]
    #             merged_arr[j+1] = sorted_b[j]
    #             j+=1
    #     else:
    #         merged_arr += sorted_b[len(sorted_a):]

    # print('merged', merged_arr)

    # last = 0 
    # for i in range(len(sorted_a)):
    #     for j in range(len(sorted_b)):
    #         if sorted_a[i] > sorted_b[j]:
    #             merged_arr[j] = sorted_b[j]
    #             last = j
    #         else:
    #             merged_arr[i] = sorted_a[i]
    #     merged_arr[last+1] = sorted_a[i]

    # a=0
    # b=0
    # for i in range(len(merged_arr)):
    #     while a < len(sorted_a) and b < len(sorted_b):
    #         if sorted_a[a] >= sorted_b[b]:
    #             merged_arr[i] = sorted_b[b]
    #             b+=1
    #         else:
    #             merged_arr[i] = sorted_a[a]
    #             a+=1

    # if a > len(sorted_a):
    #     merged_arr + sorted_a[:a]
    # if b > len(sorted_b):
    #     merged_arr + sorted_b[:b]





    # return merged_arr


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


# implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # Your code here


    return arr


def merge_sort_in_place(arr, l, r):
    # Your code here


    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):
    # Your code here

    return arr

my_arr = [9,4,6,1,5,3]
print(merge_sort(my_arr))