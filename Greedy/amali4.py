#append()=push
#pop()=pop
stack = []
temp3=[]
inp=int(input())
x=0
y=0

for i in range(inp):    
    data=input()
    data=list(map(int, data.split()))
    stack.append(data)

for i in range(len(stack)):
    a1=stack[i][0]
    b1=stack[i][1]
    a2=stack[i][2]
    b2=stack[i][3]

    if(a1+b1>=a2+b2):

        temp1=[]
        temp1.append(a1)
        temp1.append(b1)

        temp2=[]
        temp2.append(a2)
        temp2.append(b2)

        temp3.append(temp1)
        temp3.append(temp2)
        
    elif(a1>b2):
        x+=a1 
        y+=b2

    elif(b1>a2):
        x+=a2
        y+=b1

temp3.sort(key=sum,reverse=True)
for j in range(len(temp3)):
    if(j%2==0):
        x+=temp3[j][0]
    else:
        y+=temp3[j][1]

print(x-y)


 
