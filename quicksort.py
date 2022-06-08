import random

def ran_partition(arr, low, high):
    pivot = random.randint(low,high)
    arr[pivot], arr[low] = arr[low], arr[pivot]
    return partition(arr, low, high)

def partition(arr, low, high):
    x = arr[low]
    i = low

    for j in range(low+1, high + 1):
        if arr[j] < x:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[low], arr[i] = arr[i], arr[low]
    return i

def ran_quicksort(arr, low, high):
    if low < high:
        p = ran_partition(arr, low, high)
        ran_quicksort(arr, low, p - 1)
        ran_quicksort(arr, p+1, high)

if __name__ == "__main__":
    arr = [2, 5, 6, 1, 4, 4, 6, 2, 4, 7, 8]
    ran_quicksort(arr, 0, len(arr)-1)
    print(arr)