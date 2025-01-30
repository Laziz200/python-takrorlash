list=[]
print("nechta son kiritasiz?")
d=int(input())
i=0
while i!=d:
    c=int(input("son kiriting:"))
    list.append(c)
    i+=1
a=0
for i in list:
    if list.count(i)==1:
        a+=1
if a==0:
    print(-1)
else:
    print(f"1 marta takrorlangan elementlar soni: ➤➤➤ {a} ta")