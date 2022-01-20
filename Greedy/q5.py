n=input()
n=list(map(int, n.split()))
k=int(n[1])

result=[]

for i in range(n[0]):   
    data=input()
    data=list(map(int, data.split()))
    result.append(data)

result.sort(reverse=False)

def answer(r):

    time=result[0][1]-1
    for j in range(len(result)):
        time+=1
        for b in range(k):
            if(time<=result[0][1]):
                result.pop(0)

            
            if(len(result)==0):
                return "YES"

            if(time>result[0][1]):
                return "NO"




    
    

print(answer(result))