data=input()
data=list(map(int, data.split(",")))
N=data[0]
S=data[1]
A=data[2]
B=data[3]

res=[]
temp=[]

res.append(S)
temp.append(S)

while(len(temp)!=0):
    for i in temp:
        temp.pop(0)

        if(i+A<=N and i+A>0):
            if((i+A) not in res and (i+A) not in temp):
                temp.append(i+A)
                res.append(i+A)

        if(i+B<=N and i+A>0):
            if((i+B) not in res and (i+B) not in temp):
                temp.append(i+B)
                res.append(i+B)

        if(i-A<=N and i-A>0):
            if((i-A) not in res and (i-A) not in temp):
                temp.append(i-A)
                res.append(i-A)

        if(i-B<=N and i-B>0):
            if((i-B) not in res and (i-B) not in temp):
                temp.append(i-B)
                res.append(i-B)

res.sort()
print(len(res))
print(*res)