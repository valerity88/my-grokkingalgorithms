def max(list_):
    if len(list_) == 2:
        return list_[0] if list_[0] > list_[1] else list_[1]
    return list_[0] if list_[0] > max(list_[1:]) else max(list_[1:])
    
print(max([3,7,12,1,8,36,4]))
        
