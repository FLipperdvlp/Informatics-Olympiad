import sys
sys.setrecursionlimit(1 << 25)
input = sys.stdin.readline

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

def insert(root, word):
    node = root
    for ch in word:
        if ch not in node.children:
            node.children[ch] = TrieNode()
        node = node.children[ch]
    node.is_end = True

def dfs(node, path):
    for ch in sorted(node.children):
        path.append(ch)
        dfs(node.children[ch], path)
        path.append('B')
    if node.is_end:
        path.append('E')

n = int(input())
words = [input().strip() for _ in range(n)]

root = TrieNode()
for word in words:
    insert(root, word)

result = []
dfs(root, result)

print(len(result))
print(''.join(result))
