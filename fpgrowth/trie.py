import numpy as np

# класс узла дерева
class TrieNode:
    def __init__(self, text='', char=''):
        self.text = text
        self.char = char
        self.count = 0
        self.children = dict()
        self.is_word = False

# класс префиксного дерева
class PrefixTree:
    def __init__(self):
        self.root = TrieNode()

    # вставка слова в дерево
    def insert(self, word):
        current = self.root
        for i, char in enumerate(word):
            if char not in current.children:
                prefix = word[0:i+1]
                current.children[char] = TrieNode(prefix, char)
            current.count += 1
            current = current.children[char]
        current.count += 1
        current.is_word = True

    # вспом. метод для tree_words
    def rec_func(self, node, words):
        if node.is_word:
            words.append(node.text)
        for letter in node.children:
            self.rec_func(node.children[letter], words)

    # возврат всех находящихся в дереве слов
    def tree_words(self):
        words = list()
        current = self.root
        self.rec_func(current, words)
        return words

    # подсчет кол-ва встреч символа в дереве
    def occur(self, char, current=None):
        if not current:
            current = self.root
        count = 0
        if current.char == char:
            count = current.count
        for letter in current.children:
            count += self.occur(char, current.children[letter])
        return count

# построение дерева на основе слов из itemset
def constructTree(itemset):
    tree = PrefixTree()
    for i in itemset:
        tree.insert(i)
    return tree

# построение условного дерева для символа char
def cond_tree(set, items, char, ml):
    res_list = []
    tree = PrefixTree()
    words = []
    for i in items:
        if char[-1] in i:
            word = ''
            for j in i:
                if j == char[-1]:
                    break
                word += j
            if word != '':
                words = np.append(words, word)
                tree.insert(word)
    for i in set:
        if tree.occur(i) >= ml:
            res_list = np.append(res_list, char+i)
            ct = cond_tree(set, words, char+i, ml)
            if len(ct) > 0:
                res_list = np.append(res_list, ct)
    return res_list
