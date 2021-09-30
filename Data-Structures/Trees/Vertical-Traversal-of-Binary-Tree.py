#Given a Binary Tree, find the vertical traversal of it starting from the leftmost level to the rightmost level.
#If there are multiple nodes passing through a vertical line, then they should be printed as they appear in level order traversal of the tree.

class Solution:
    
    #Function to find the vertical order traversal of Binary Tree.
    def verticalOrder(self, root): 
        ar = []
        queue = [(root, -1)]

        while queue:
            cur = queue.pop(0)
            ar.append((cur[-1] + 1, cur[0].data))
    
            if cur[0].left: 
                queue.append((cur[0].left, cur[-1] - 1))
            if cur[0].right: 
                queue.append((cur[0].right, cur[-1] + 1))
        
        mn, mx = min([i[0] for i in ar]), max([i[0] for i in ar])
        br = {i: [] for i in range(mn, mx+1)}
        
        for i in ar:
            br[i[0]].append(i[1])
        
        ans = []
        for i in range(mn, mx+1):
            ans += br[i]
        
        return ans
