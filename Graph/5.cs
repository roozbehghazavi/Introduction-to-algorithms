using System;
using System.Collections.Generic;
 
class GFG
{
    static int N = 12, ans;
     
    static List<List<int>> tree = new List<List<int>>();
     
    static int dfs(int []visit, int node)
    {
        int num = 0, temp = 0;
        visit[node] = 1;
        for (int i = 0; i < tree[node].Count; i++)
        {
            if (visit[tree[node][i]] == 0)
            {
                temp = dfs(visit, tree[node][i]);
                if(temp % 2 != 0)
                    num += temp;
                else
                    ans++;
            }
        }
        return num + 1;
    }
     

    static int minEdge(int n)
    {
        int []visit = new int[n + 2];
        ans = 0;
     
        dfs(visit, 1);
     
        return ans;
    }
     
    public static void Main(String []args)
    {
        int n = Convert.ToInt32(Console.ReadLine());

        for(int i = 0; i < n + 2;i++)
        tree.Add(new List<int>());
        
        for(int j=0;j<n-1;j++)
        {
            string s = Console.ReadLine();
            string[] values = s.Split(' ');
            int a = int.Parse(values[0]);
            int b = int.Parse(values[1]);
            tree[a].Add(b);
            tree[b].Add(a);
        }
        
        if(n%2!=0)
        {
            Console.WriteLine(-1);
            System.Environment.Exit(0);  
        }

        Console.WriteLine(minEdge(n));
    }
}