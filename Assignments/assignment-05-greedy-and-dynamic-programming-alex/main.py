import math, queue
from collections import Counter

####### Problem 1 #######

class TreeNode(object):
    # we assume data is a tuple (frequency, character)
    def __init__(self, left=None, right=None, data=None):
        self.left = left
        self.right = right
        self.data = data
    def __lt__(self, other):
        return(self.data < other.data)
    def children(self):
        return((self.left, self.right))
    
def get_frequencies(fname):
    f=open(fname, 'r')
    C = Counter()
    for l in f.readlines():
        C.update(Counter(l))
    return C

# given a dictionary f mapping characters to frequencies, 
# create a prefix code tree using Huffman's algorithm
def make_huffman_tree(f):
    p = queue.PriorityQueue()
    # construct heap from frequencies, the initial items should be
    # the leaves of the final tree
    for c in f.keys():
        p.put(TreeNode(None,None,(f[c], c)))

    # greedily remove the two nodes x and y with lowest frequency,
    # create a new node z with x and y as children,
    # insert z into the priority queue (using an empty character "")
    while (p.qsize() > 1):
        nodeX = p.get()
        nodeY = p.get()
        val1 = nodeX.data[0]
        val2 = nodeY.data[0]
        arg3 = val1 + val2
        arg4 = ""
        z = TreeNode(nodeX, nodeY, (arg3, arg4))
        p.put(z)
        
    # return root of the tree
    return p.get()

# Perform a traversal on the prefix code tree to collect all encodings.
# Recursively call get_code, appending 0 or 1 to prefix as appropriate
# depending on if the call is to the left or right child.
# When a leaf is found, update the code dict object to map from
# the value in the leaf to the encoding specified by prefix.
# Return the code object.
def get_code(node, prefix="", code={}):
    if (node.left == None and node.right == None):
        code[node.data[1]] = prefix
    else:
        get_code(node.left, prefix + "0", code)
        get_code(node.right, prefix + "1", code)
    return code

# Given an alphabet and frequencies, compute the cost of a fixed length encoding.
# You'll have to consider the total number of unique elements in f to 
# determine the number of bits needed to represent each character.
def fixed_length_cost(f):
    return(math.ceil(math.log(len(f), 2)) * sum(f.values()))

# given a Huffman encoding and character frequencies, compute cost of a Huffman encoding
def huffman_cost(C, f):
    cost = 0
    for c in f.keys():
        cost += f[c] * len(C[c])
    return cost

def test_huffman_simple():
    """ example from class """
    f = Counter(["A", "A", "A", "A", "A", "A", "A", "A", "A", "B", "C", "D"])
    T = make_huffman_tree(f)
    C = get_code(T)
    assert huffman_cost(C, f) == 17

def analyze_files():
    for fname in ['alice29.txt', 'asyoulik.txt', 'f1.txt', 'fields.c', 'grammar.lsp']:
        f = get_frequencies(fname)
        print("Fixed-length cost:  %d" % fixed_length_cost(f))
        T = make_huffman_tree(f)
        C = get_code(T)
        print("Huffman cost:  %d" % huffman_cost(C, f))


####### Problem 4 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('relevant', 'elephant')]
alignments = [('book', 'back'), ('kookaburra', 'kookybird-'), ('relev-ant','-elephant')]

def MED(S, T):
    # TODO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T)))


def fast_MED(S, T, MED_cache={}):
    key = len(S), len(T)

    if key in MED_cache:
        return MED_cache[key]

    if (len(S) == 0):
        return len(T)
    if (len(T) == 0):
        return len(S)
    if (S[-1] == T[-1]):
        return fast_MED(S[:-1], T[:-1])
        
    MED_cache[key] = 1 + min(fast_MED(S[:-1], T[:-1]), fast_MED(S[:-1], T), fast_MED(S, T[:-1]))
    return MED_cache[key]

def fast_align_MED(S, T, MED_cache={}):
    if (len(S) == 0):
        return ("-" * len(T), T)
    if (len(T) == 0):
        return (S, "-" * len(S))
    if (S[-1] == T[-1]):
        return fast_align_MED(S[:-1], T[:-1])
    else:
        return 1 + min(fast_align_MED(S[:-1], T[:-1]), fast_align_MED(S[:-1], T), fast_align_MED(S, T[:-1]))

def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)
                                 
def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])
