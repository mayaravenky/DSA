def next_perm(arr):
    n = len(arr)
    i = n - 1
    ind = -1
    for i in range(n-2,-1,-1):
        if arr[i]<arr[i+1]:
            ind = i
            break
    print(ind)
    if ind == -1:
        arr.reverse()
        return arr
    for i in range(n-1,ind,-1):
        print(i,ind)
        if arr[i]>arr[ind]:
            arr[i],arr[ind] = arr[ind],arr[i]
            break
    arr[ind+1:] = reversed(arr[ind+1:])
    return arr

# Example usage:
#arr = [1, 2, 3]
#print(next_perm(arr))  # Output: [1, 3, 2]
arr = [1, 3, 2]
print(next_perm(arr))  # Output: [2, 1, 3]

