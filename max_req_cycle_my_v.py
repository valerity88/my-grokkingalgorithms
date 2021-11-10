def big(list_):
    a = list_[0]
    for i in list_[1:]:
        if i > a:
            a = i
    return a
print(big([3,7,12,1,8,36,4]))
        
