def minimum(list_):
    Index = 0
    new_Index = 0
    min_ = list_[0]
    while Index < len(list_):
        if min_ < list_[Index]:
            min_ = min_
        else:
            min_ = list_[Index]
        Index += 1
    return min_

def selection_sort(list_):
    new_list = []
    while len(list_) > 0:
        min_ = minimum(list_)
        new_list.append(min_)
        list_.remove(min_)
    return new_list
 
my_list = [1, 7, 12, 3, -1]

print (selection_sort(my_list))


            
