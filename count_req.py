def count(list):
    if list == []:
        return 0
    return 1 + count(list[1:]) 
print(len([1,2,3,4]))
