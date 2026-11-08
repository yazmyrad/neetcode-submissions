class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
            
        graph = defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i]+"*"+word[i+1:]
                graph[pattern].append(word)

        q = deque([beginWord])
        visited = set([beginWord])
        count = 1
        while q:
            for j in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return count
                for i in range(len(word)):
                    pattern = word[:i]+"*"+word[i+1:]
                    for nei in graph[pattern]:
                        if nei not in visited:
                            visited.add(nei)
                            q.append(nei)
            count += 1
        return 0