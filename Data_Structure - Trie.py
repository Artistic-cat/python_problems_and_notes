class TrieNode:
    def __init__(self):
        self.children={}
        self.end=False

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insertString(self, word):
        current=self.root
        for ch in word:
            node=current.children.get(ch)
            if node==None:
                node=TrieNode()
                current.children.update({ch:node})
            current=node
        current.end=True
    
    def searchString(self,word):
        currentNode=self.root
        for i in word:
            node=currentNode.children.get(i)
    
newTrie=Trie()