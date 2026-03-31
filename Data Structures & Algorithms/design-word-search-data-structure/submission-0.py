class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.is_end = True

    def search(self, word: str) -> bool:
        
        def dfs(node, index):
            for i in range(index, len(word)):
                c = word[i]

                if c == ".":
                    for n in node.children.values():
                        if dfs(n,i+1):
                            return True
                    return False
                else:
                    if c not in node.children:
                        return False
                    node = node.children[c]
            
            return node.is_end
        
        return dfs(self.root, 0)
    





class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
