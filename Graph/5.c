#include<stdio.h>
int w[101][101] = {0}, v[101] = {0};
int n,m,ans=0;

int dfs(int x){
    v[x] = 1;
    int son = 0;
    for(int i=0; i<101;i++) 
        if(w[x][i] && !v[i]) son += dfs(i);
    if(son % 2) { ans++; return 0;}
    return -1;
}

int main() {
    scanf("%d", &n);
    m=n-1;
    
    for(int i=0,a,b; i<m;i++){
        scanf("%d%d", &a,&b);
        w[a][b] = w[b][a] = 1;
    }
    dfs(1);
    printf("%d\n", ans-1);  
    return 0;
}