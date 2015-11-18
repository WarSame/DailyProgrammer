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

    def get_children(self):
        for i in self.children:
            print i
'''
    def __str__(self):
        node_string = self.word
        if not self.children.keys():
            return node_string
        node_string += "\nConnected to:"
        for char in self.children.keys():
            node_string += char + "\t"
        return node_string
'''

class Trie:
    def __init__(self, words):
        # Given a list of words insert all words into trie
        self.start_node = Node("")
        for word in words:
            self.insert_word(word)

    def print_children(self, stub):
        # Given a stub of a word, print all words following from it
        curr_node = self.start_node
        for char in stub:
            child = curr_node.get_child(char)
            if child:
                # If our node has a child, move to it and continue
                curr_node = child
            else:
                # If not, the stub is not in the trie
                return ""
        # We now have our stub node and can find all
        # Its descendants, and return those
        leaves = self.get_children_leaves(curr_node)
        for i in range(0,len(leaves)):
            leaves[i] = stub + leaves[i]
        return leaves

    def get_children_leaves(self, curr_node):
        leaves = []
        for child in curr_node.children.keys():
            print "Child is "+child
            child_node = curr_node.children[child]

            # Add children leaves to our leaves collection
            # Get the leaves of our children
            leaves = self.get_children_leaves(child_node)
            # Append the current letter in front of all child leaves
            for i in range(0,len(leaves)):
                leaves[i] = child + leaves[i]

            if child_node.leaf:
                leaves.append(child)
        # Return leaves up
        return leaves

    def insert_word(self, word):
        # Given a word, insert it into the trie
        curr_node = self.start_node
        for char in word:
            # Loop through entire word
            child = curr_node.get_child(char)
            if child:
                # If you find a child, move to it
                curr_node = child
            else:
                # If not, make one
                new_node = Node(curr_node.word)
                curr_node.set_child(char, new_node)
                #And move to that new one
                curr_node = new_node
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
                return False
        # Return whether the end node is a leaf or not
        return curr_node.leaf

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
    '''
    f = open("../enable1.txt","r")
    words=[]
    for line in f.readlines():
        words.append(line.strip("\n"))
    tr = Trie(words)
    '''
    tr = Trie(["this","theory","that"])
    result = tr.print_children("th")
    print result



main()
