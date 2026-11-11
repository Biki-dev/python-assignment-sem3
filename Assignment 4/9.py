def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1
    mid = (low+high)//2
    
    if arr[mid] == target:
        return mid
    elif target < arr[mid]:
        return binary_search_recursive(arr, target, low, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, high)

arr = [1,2,3,4,5,6,7,8]
target1 = 5
target2 = 9
print(binary_search_recursive(arr, target1, 0, len(arr) - 1)) # 4
print(binary_search_recursive(arr, target2, 0, len(arr) - 1)) # -1