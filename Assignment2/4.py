leng=['a','a','b','c','c','b','a']
unique=[]

for i in leng:
    if(i not in unique):
        unique.append(i)
print(unique)