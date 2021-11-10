def len_(list):
    if list == []:
        return 0
    else:
        return 1 + len_(list[1:]) 
print(len([1,2,3,4]))
