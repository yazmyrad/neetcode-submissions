class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges)))
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]] 
                x = parent[x]
            return x

        for u, v in edges:
            ru, rv = find(u-1), find(v-1)
            if ru == rv:          
                return [u, v]
            parent[ru] = rv     
        
