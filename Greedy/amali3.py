Coins=[10,5,1]
m=int(input())

#O(n)
def Coin(n):
    idx=0
    res=0
    while(n!=0):
        if(Coins[idx]<=n):
            n-=Coins[idx]
            res+=1
        else:
            idx+=1
    return res

#O(1)
def Coin2(n):
    money=0

    money+=(n//10)
    n=(n%10)

    money+=(n//5)
    n=(n%5)
    money+=(n//1)

    return money

print(Coin2(m))