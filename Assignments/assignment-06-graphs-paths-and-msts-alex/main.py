from collections import deque
from heapq import heappush, heappop 



def shortest_shortest_path(graph, source):
    """
    Params: 
      graph.....a graph represented as a dict where each key is a vertex
                and the value is a set of (vertex, weight) tuples (as in the test case)
      source....the source node
      
    Returns:
      a dict where each key is a vertex and the value is a tuple of
      (shortest path weight, shortest path number of edges). See test case for example.
    """
    def push():
      return heappush(q, (0, source, 0))
    
    def push2(): 
      return heappush(q, arg)

    q = []
    push()
    d = {}
    while len(q) != 0:
        a, u, e = heappop(q)
        if u not in d:
            d[u] = (a, e)
            for v, w in graph[u]:
                g = e + 1
                arg = (a + w, v, g)   
                push2()
    return d
    
def test_shortest_shortest_path():

    graph = {
                's': {('a', 1), ('c', 4)},
                'a': {('b', 2)}, # 'a': {'b'},
                'b': {('c', 1), ('d', 4)}, 
                'c': {('d', 3)},
                'd': {},
                'e': {('d', 0)}
            }
    result = shortest_shortest_path(graph, 's')
    # result has both the weight and number of edges in the shortest shortest path
    assert result['s'] == (0,0)
    assert result['a'] == (1,1)
    assert result['b'] == (3,2)
    assert result['c'] == (4,1)
    assert result['d'] == (7,2)
    
    
def bfs_path(graph, source):
    """
    Returns:
      a dict where each key is a vertex and the value is the parent of 
      that vertex in the shortest path tree.
    """
    def body(): 
      u = q.popleft()
      for v in graph[u]:
          if v not in d:
              #print(q)
              q.append(v)
              #print(v)
              d[v] = u
      #print(graph)

    q = deque()
    q.append(source)

    d = {}
    d[source] = None

    while len(q) != 0:
        body()
    return d

def get_sample_graph():
     return {'s': {'a', 'b'},
            'a': {'b'},
            'b': {'c'},
            'c': {'a', 'd'},
            'd': {}
            }

def test_bfs_path():
    graph = get_sample_graph()
    parents = bfs_path(graph, 's')
    assert parents['a'] == 's'
    assert parents['b'] == 's'    
    assert parents['c'] == 'b'
    assert parents['d'] == 'c'
    
def get_path(parents, destination):
    """
    Returns:
      The shortest path from the source node to this destination node 
      (excluding the destination node itself). See test_get_path for an example.
    """
    p = []

    while destination != None:

        p.append(destination)
        #print(p)
        destination = parents[destination]
        for i in p:
          #print(p)
          #print(i)
          pass
        
    print(parents)
    print(p)
    print(p[1:])
    return ''.join(reversed(p[1:]))

def test_get_path():
    graph = get_sample_graph()
    parents = bfs_path(graph, 's')
    assert get_path(parents, 'd') == 'sbc'
