List=[5,5,4,6,8,9,9,7,10,11,52,89,65]

def duplikaty(list):
    list.sort()
    for i in list:
        if list.count(i)>1:
            list.remove(i)
    return list
print(duplikaty(List))
