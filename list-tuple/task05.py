list=[1,2,3,4,5,6,7,8,9,10]
new_list=[]
new_list1=[]
for i in list:
    if i % 2 == 1:
        new_list.append(i)
    else:
        new_list1.append(i)
new_list1.sort(reverse=True)
b=tuple(new_list)
a=tuple(new_list1)
c=(a,b)
print(c)