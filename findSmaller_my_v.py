def choice(list_):
    Index = 0
    min_ = list_[0]
    while Index < len(list_):
        if min_ < list_[Index]:
            min_ = min_
        else:
            min_ = list_[Index]
        Index += 1
    return min_
my_list = [1, 7, 12, 3, -1, 2]
print (choice(my_list))


            
