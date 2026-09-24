from collections import defaultdict
import sys
input = sys.stdin.readline

class TrieNode:
    def __init__(self):
        self.children = {}
        self.era_count = defaultdict(int)

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, code, era):
        node = self.root
        for ch in code:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            node.era_count[era] += 1
    
    def query(self, prefix, era):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return 0
            node = node.children[ch]
        return node.era_count.get(era, 0)

def solve():
    Q = int(input())
    trie = Trie()
    for _ in range(Q):
        parts = input().split()
        if parts[0] == "ADD":
            code, era = parts[1], int(parts[2])
            trie.add(code, era)
        else:  # QUERY
            prefix, era = parts[1], int(parts[2])
            print(trie.query(prefix, era))

if __name__ == "__main__":
    solve()
