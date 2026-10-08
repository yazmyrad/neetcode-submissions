class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = Counter(tasks)
        tasks = [(freq, task) for task, freq in counts.items()]
        heapq.heapify_max(tasks)
        time = 0
        ans = ''
        q = deque()
        while tasks or q:
            if tasks:
                freq, task = heapq.heappop_max(tasks)
                ans += task
                if freq - 1 > 0:
                    q.append((freq-1, task, time+n))
               
            if q and time == q[0][2]:
                freq, task, t = q.popleft()
                heapq.heappush_max(tasks, (freq, task))
            
            if q and time != q[0][2] and tasks == []: ans += '*'
            time += 1
            
        #print(ans)
        return len(ans)
