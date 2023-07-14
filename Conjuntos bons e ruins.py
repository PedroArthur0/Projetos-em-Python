class TrieNode:
    def _init_(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def _init_(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
            if current.is_end_of_word:
                return False  # A palavra é um prefixo de outra palavra
        current.is_end_of_word = True
        # Verifica se a palavra é um prefixo de outra palavra
        return len(current.children) == 0


def is_set_good(words):
    trie = Trie()
    for word in words:
        if not trie.insert(word):
            return False
    return True


while True:
    n = int(input())
    if n == 0:
        break
        words = []
        for _ in range(n):
            word = input()
            words.append(word)
        if is_set_good(words):
            print("Conjunto Bom")
        else:
            print("Conjunto Ruim")
