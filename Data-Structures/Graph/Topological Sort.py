#push the elements which have indegree=0
#perform bfs algo (pop q[0] and reduce the indegree of it's adjacent nodes by 1
#check if there is any node with indegree = 0, 
#if no: move ahead and pop another element and repeat, 
#if yes, insert that node into queue )

class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, adj):
        ans = []
        indegree = [0]*V
        for i in range(V):
            for j in adj[i]:
                indegree[j] = indegree[j]+1
        q = []
        for i in range(V):
            if indegree[i]==0:
                q.append(i)
        
        while(q):
            node = q.pop(0)
            ans.append(node)
            for i in adj[node]:
                indegree[i] = indegree[i]-1
                if indegree[i]==0:
                    q.append(i)
                    
        return ans



#TC = O(N+E)
#SC = O(N)+O(N)
#QUEUE AND INDEGREE ARRAY
