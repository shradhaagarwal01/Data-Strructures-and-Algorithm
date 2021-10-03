#Given an undirected graph with V vertices and E edges, check whether it contains any cycle or not. 



class Solution:
    
    #Function to detect cycle in an undirected graph.
	def cycle(self,node,parent,vis,adj):
        vis[node] = True
        for i in adj[node]:
            if not vis[i]:
                if self.cycle(i,node,vis,adj):
                    return True
            elif i!=parent:
                return True
        return False
    
    def isCycle(self, V, adj):
        vis = [False]*V
        for i in range(V):
            if not vis[i]:
                if self.cycle(i,-1,vis,adj):
                    return True
        return False
