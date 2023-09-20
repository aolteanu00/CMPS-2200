# assignment-03

# no other imports needed
from collections import defaultdict
import math


### PART 1: SEARCHING UNSORTED LISTS

# search an unordered list L for a key x using iterate
# return True or False
def isearch(L, x):
    f = lambda y, z: y or z == x
    xArg = False
    a = L
    return iterate(f, xArg, a)

def test_isearch():
    assert isearch([1, 3, 5, 4, 2, 9, 7], 2) == (2 in [1, 3, 5, 4, 2, 9, 7])
    assert isearch([1, 3, 5, 2, 9, 7], 99) == (99 in [1, 3, 5, 2, 9, 7])

def iterate(f, x, a):
    # done. do not change me.
    if len(a) == 0:
        return x
    else:
        return iterate(f, f(x, a[0]), a[1:])

# search an unordered list L for a key x using reduce
# return True or False
def rsearch(L, x):
    pass

def test_rsearch():
    assert rsearch([1, 3, 5, 4, 2, 9, 7], 2) == (2 in [1, 3, 5, 4, 2, 9, 7])
    assert rsearch([1, 3, 5, 2, 9, 7], 99) == (99 in [1, 3, 5, 2, 9, 7])

def reduce(f, id_, a):
    print(a)
    # done. do not change me.
    if len(a) == 0:
        return id_
    elif len(a) == 1:
        return a[0]
    else:
        # can call these in parallel
        res = f(reduce(f, id_, a[:len(a)//2]),
                 reduce(f, id_, a[len(a)//2:]))
        return res

def ureduce(f, id_, a):
    if len(a) == 0:
        return id_
    elif len(a) == 1:
        return a[0]
    else:
        # can call these in parallel
        return f(ureduce(f, id_, a[:len(a)//3]),
                 ureduce(f, id_, a[len(a)//3:]))


### PART 2: DOCUMENT INDEXING

def run_map_reduce(map_f, reduce_f, docs):
    # done. do not change me.
    """    
    The main map reduce logic.
    
    Params:
      map_f......the mapping function
      reduce_f...the reduce function
      docs.......list of input records
    """
    # 1. call map_f on each element of docs and flatten the results
    # e.g., [('i', 1), ('am', 1), ('sam', 1), ('i', 1), ('am', 1), ('sam', 1), ('is', 1), ('ham', 1)]
    pairs = flatten(list(map(map_f, docs)))
    # 2. group all pairs by by their key
    # e.g., [('am', [1, 1]), ('ham', [1]), ('i', [1, 1]), ('is', [1]), ('sam', [1, 1])]
    groups = collect(pairs)
    # 3. reduce each group to the final answer
    # e.g., [('am', 2), ('ham', 1), ('i', 2), ('is', 1), ('sam', 2)]
    return [reduce_f(g) for g in groups]

def doc_index_map(doc_tuple):
    """
    Params:
      doc_tuple....a tuple (docstring, docid)
    Returns:
      a list of tuples of form (word, docid), where token is a whitespace delimited element of this string.

    Note that the returned list can contain duplicates.
    E.g.
    >>> doc_index_map('document one is cool is it', 0)
    [('document', 0), ('one', 0), ('is', 0), ('cool', 0), ('is', 0), ('it', 1)]    
    """
    ### done. do not change me.
    doc, docid = doc_tuple[0], doc_tuple[1]
    return [(token, docid) for token in doc.split()]

def dedup(a, b):
    """
    Return a concatenation of two lists without any duplicates.
    Assume that input lists a and b already sorted and deduplicated.
    This should be done in _constant_ time (ignoring any time to create or concatenate lists).
    e.g.
    >>> dedup([1,2,3], [3,4,5])
    [1,2,3,4,5]
    """
    result = list(a+b)
    result = set(result)
    result = sorted(result)
    return result

def doc_index_reduce(group):
    """
    Fix this function to instead call the reduce and dedup functions
    to return the _unique_ list of document ids that this word appears in.
    
    Params:
      group...a tuple of the form (word, list_of_docids), indicating the docids containing this word, with duplicates.
    Returns:
      tuple of form (word, list_of_docids), where duplicate docids have been removed.
      
    >>> doc_index_reduce(['is', [0,0,1,2]])
    ('is', [0,1,2])
    """
    f = dedup
    id_ = []
    a = map(dir_helper, group[1])
    a = list(a)
    result = reduce(f, id_, a)
    return (group[0], result)
    
def test_dedup():
    assert dedup([1,2,3], [3,4,5]) == [1,2,3,4,5]
    
def test_doc_index_reduce():
    assert doc_index_reduce(['is', [0,0,1,2]]) == ('is', [0,1,2])

def test_index():
    res = run_map_reduce(doc_index_map, doc_index_reduce,
               [('document one is cool is it', 0),
                ('document two is also cool', 1),
                ('document three is kinda neat', 2)
               ])    
    assert res == [('also', [1]),
                   ('cool', [0, 1]),
                   ('document', [0, 1, 2]),
                   ('is', [0, 1, 2]),
                   ('it', [0]),
                   ('kinda', [2]),
                   ('neat', [2]),
                   ('one', [0]),
                   ('three', [2]),
                   ('two', [1])]
    
def collect(pairs):
    """
    Implements the collect function (see text Vol II Ch2)
    >>> collect([('i', 1), ('am', 1), ('sam', 1), ('i', 1)])
    [('am', [1]), ('i', [1, 1]), ('sam', [1])]    
    """
    ### done
    result = defaultdict(list)
    for pair in sorted(pairs):
        result[pair[0]].append(pair[1])
    return list(result.items())

def plus(x, y):
    # done. do not change me.
    return x + y
    
def flatten(sequences):
    # done. do not change me.
    return iterate(plus, [], sequences)

def dir_helper(input):
    return [input]


### PART 3: PARENTHESES MATCHING

#### Iterative solution
def parens_match_iterative(mylist):
    """
    Implement the iterative solution to the parens matching problem.
    This function should call `iterate` using the `parens_update` function.
    
    Params:
      mylist...a list of strings
    Returns
      True if the parenthesis are matched, False otherwise
      
    e.g.,
    >>>parens_match_iterative(['(', 'a', ')'])
    True
    >>>parens_match_iterative(['('])
    False
    """
    f = parens_update
    x = 0
    a = mylist

    return iterate(f, x, a) == 0

def parens_update(current_output, next_input):
    """
    This function will be passed to the `iterate` function to 
    solve the balanced parenthesis problem.
    
    Like all functions used by iterate, it takes in:
    current_output....the cumulative output thus far (e.g., the running sum when doing addition)
    next_input........the next value in the input
    
    Returns:
      the updated value of `current_output`
    """
    if next_input == ')':
        return current_output - 1

    if next_input == '(':
         return current_output + 1

    else:
        return current_output

def test_parens_match_iterative():
    assert parens_match_iterative(['(', ')']) == True
    assert parens_match_iterative(['(']) == False
    assert parens_match_iterative([')']) == False


#### Scan solution

def parens_match_scan(mylist):
    """
    Implement a solution to the parens matching problem using `scan`.
    This function should make one call each to `scan`, `map`, and `reduce`
    
    Params:
      mylist...a list of strings
    Returns
      True if the parenthesis are matched, False otherwise
      
    e.g.,
    >>>parens_match_scan(['(', 'a', ')'])
    True
    >>>parens_match_scan(['('])
    False
    
    """
    f = sum 
    id_ = 0
    a = map(paren_map, mylist)
    a = list(a)

    f2 = test 
    id_2 = 0
    a2 = scan(f, id_, a)
 
    if a2[1] == 0:
        return (reduce(f2, id_2, a2) == 0)
    else:
        return False

def scan(f, id_, a):
    """
    This is a horribly inefficient implementation of scan
    only to understand what it does.
    We saw a more efficient version in class. You can assume
    the more efficient version is used for analyzing work/span.
    """
    return (
            [reduce(f, id_, a[:i+1]) for i in range(len(a))],
             reduce(f, id_, a)
           )

def paren_map(x):
    """
    Returns 1 if input is '(', -1 if ')', 0 otherwise.
    This will be used by your `parens_match_scan` function.
    
    Params:
       x....an element of the input to the parens match problem (e.g., '(' or 'a')
       
    >>>paren_map('(')
    1
    >>>paren_map(')')
    -1
    >>>paren_map('a')
    0
    """
    if x == '(':
        return 1
    elif x == ')':
        return -1
    else:
        return 0

def min_f(x,y):
    """
    Returns the min of x and y. Useful for `parens_match_scan`.
    """
    if x < y:
        return x
    return y

def test_parens_match_scan():
    assert parens_match_scan(['(', ')']) == True
    assert parens_match_scan(['(']) == False
    assert parens_match_scan([')']) == False

#### Divide and conquer solution

def parens_match_dc(mylist):
    """
    Calls parens_match_dc_helper. If the result is (0,0),
    that means there are no unmatched parentheses, so the input is valid.
    
    Returns:
      True if parens_match_dc_helper returns (0,0); otherwise False
    """
    # done.
    n_unmatched_left, n_unmatched_right = parens_match_dc_helper(mylist)
    return n_unmatched_left==0 and n_unmatched_right==0

def parens_match_dc_helper(mylist):
    """
    Recursive, divide and conquer solution to the parens match problem.
    
    Returns:
      tuple (R, L), where R is the number of unmatched right parentheses, and
      L is the number of unmatched left parentheses. This output is used by 
      parens_match_dc to return the final True or False value
    """

def test_parens_match_dc():
    assert parens_match_dc(['(', ')']) == True
    assert parens_match_dc(['(']) == False
    assert parens_match_dc([')']) == False

def sum(val1, val2):
    result = val1 + val2
    return result

def test(val1, val2):
    if (val1 == -1) or (val2 == 1):
        return 1
    else:
        return 0 