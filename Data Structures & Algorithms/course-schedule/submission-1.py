class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = defaultdict(int)
        graph = defaultdict(list)
        for course in prerequisites:
            graph[course[0]].append(course[1])
        #print(graph)
        has_cycle = False
        def dfs(node):
            nonlocal has_cycle
            if visited[node] == 1:
                has_cycle = True
                return
            if visited[node] == 2:
                return
            visited[node] = 1
            for nei in graph[node]:
                dfs(nei)
            
            if has_cycle: return
            visited[node] = 2

        for node in range(numCourses):
            if node not in visited:
                visited[node] = 0
                dfs(node)
        return not has_cycle