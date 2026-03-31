class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        
        wordList.append(beginWord)
        adj = {word:[] for word in wordList}

        def is_connected(w1, w2):
            count = 0
            for i in range(len(w1)):
                if w1[i] != w2[i]:
                    count +=1
            
            return True if count == 1 else False
        
        for i in range(len(wordList)):
            for j in range(i+1, len(wordList)):
                if is_connected(wordList[i], wordList[j]):
                    adj[wordList[i]].append(wordList[j])
                    adj[wordList[j]].append(wordList[i])
        
        steps = 1
        q = deque()
        visit = set()
        visit.add(beginWord)

        for nei in adj[beginWord]:
            q.append(nei)

        while q:
            steps += 1
            for i in range(len(q)):
                word = q.popleft()
                if word == endWord:
                    return steps
                
                visit.add(word)
                
                for nei in adj[word]:
                    if nei not in visit:
                        q.append(nei)
        
        return 0













