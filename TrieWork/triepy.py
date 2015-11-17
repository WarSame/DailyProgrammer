# Trie work
# Graeme Cliffe


class Node:
    # Node - element in the trie
    # May have children nodes. May be a leaf.
    # Must be on the path to some leaf
    def __init__(self, word):
        self.word = word
        self.children = {}
        self.leaf = False

    def set_child(self, char, child_node):
        self.children[char] = child_node

    def get_child(self, char):
        if char in self.children:
            return self.children[char]

    def __str__(self):
        node_string = self.word
        if not self.children.keys():
            return node_string
        node_string += "\nConnected to:"
        for char in self.children.keys():
            node_string += char + "\t"
        return node_string


class Trie:
    def __init__(self, words):
        # Given a list of words insert all words into trie
        self.start_node = Node("")
        for word in words:
            self.insert_word(word)

    def print_children(self, stub):
        # Given a stub of a word, print all words from it
        curr_node = self.start_node
        for char in stub:
            pass

    def insert_word(self, word):
        # Given a word, insert it into the trie
        curr_node = self.start_node
        for char in word:
            # Loop through entire word
            prev_node = curr_node
            child = prev_node.get_child(char)
            if child:
                # If you find a child, move to it
                curr_node = child
            else:
                # If not, make one
                curr_node = Node(prev_node.word)
                prev_node.set_child(char, curr_node)
        # Make the last character in the word a leaf
        curr_node.leaf = True

    def is_leaf(self, word):
        # Given a word, find if it is a leaf(full word)
        curr_node = self.start_node
        for char in word:
            child = curr_node.get_child(char)
            if child:
                # If the next letter is in the trie, move on to it
                curr_node = child
            else:
                # Otherwise the word is not in the trie
                return False, ""
        # Return whether the end node is a leaf or not
        return curr_node.leaf, str(curr_node)

    def is_in_trie(self, word):
        # Given a word, find if it is in the trie
        curr_node = self.start_node
        for char in word:
            child = curr_node.get_child(char)
            if child:
                # If child in trie, search from it
                curr_node = child
            else:
                return False
        return True


def main():
    f = open("../enable1.txt","r")
    words=[]
    for line in f.readlines():
        words.append(line.strip("\n"))
    tr = Trie(words)
    result = tr.is_in_trie("a")
    print result


main()
