lst = [1,2,3,4]
print(lst)
lst[0:3] = 99,55,77
print(lst)
ls = [7,8,9]
print(lst+ls)

lst2 = lst.copy() #it will copy the content of the variable
lst2 = lst #but in this scenario, it is copying the exact address with data 