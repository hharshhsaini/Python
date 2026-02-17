def divide_con(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr)//2
    left = divide_con(arr[:mid])
    right = divide_con(arr[mid:])
    return merge(left,right)

def merge(left,right):
    combineArray = []
    #pointer for comparison
    i = 0
    j = 0 
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            combineArray.append(left[i])
            i = i + 1
        else:
            combineArray.append(right[j])
            j = j + 1
    if i < len(left):
        combineArray = [*combineArray, *left[i:]]
    elif j < len(right):
        combineArray = [*combineArray,*right[j:]]
    return combineArray
    

arr = [6,4,2,8,3,1,2,4,4]
print(divide_con(arr))