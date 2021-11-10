def sum(arr):
    x = 0
    if len(arr) == 0:
        return 0
    else:
        return arr[x] + sum(arr[x+1:]) 
print(sum([1,2,3,4]))
