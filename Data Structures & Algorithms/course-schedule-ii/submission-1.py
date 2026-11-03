class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = defaultdict(int)
        graph = defaultdict(list)
        for course in prerequisites:
            graph[course[0]].append(course[1])
        
        for node in range(numCourses):
            if node not in graph:
                graph[node] = []

        has_cycle = False
        order = []
        def dfs(node):
            nonlocal has_cycle
            if visited[node] == 1:
                has_cycle = True
                return
            if visited[node] == 2:
                return
            visited[node] = 1
            
            for nei in graph[node]:
                if not has_cycle:
                    dfs(nei)
            
            if has_cycle: return
            order.append(node)
            visited[node] = 2

        for node in range(numCourses):
            dfs(node)
        #order.reverse()
        return order if not has_cycle else []