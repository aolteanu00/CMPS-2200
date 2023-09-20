# CMPS 2200 Assignment 6
## Answers

**Name:**_________________________
**Name:**_________________________


Place all written answers from `assignment-06.md` here for easier grading.


**1. Shortest shortest paths**

- **1b.** Work and span of `shortest_shortest_path`
    
    The work of 'shortest_shortest_path' is  $O(|E|log|E|)$  
    
    The span of 'shortest_shortest_path' is  $O(|E|log|E|)$

**3. Improving Dijkstra**

- **3a.** What is the maximum depth of a $d$-ary heap?

    The maximum depth of a $d$-ary heap is $O(logdn)$


- **3b.** What is the work done by `delete-min` and `insert` operations in a $d$-ary heap?

    The work done by 'delete_min' is  $O(log n d)$ 

    The work done of 'insert' is  $O(log n d)$


- **3c.** What is the work done by Dijkstra's algorithm using a $d$-ary heap?

    The work done by Dijkstra's algorithm using a $d$-ary heap is $O(|E| log n d)$


- **3d.** What value of $d$ yields an overall running time of $O(|E|)$?

    The number 2 yields this value

**4. Spanning trees**

- **4a.** Is a solution to MST guaranteed to be a solution to MMET?

    Yes it is, which is evidenced by the lightest edge property. 

- **4b.** Describe algorithm for next best MST.

    Start with T. Consider every |E| swap to get alternative Ts and choose the lightest. 
    
- **4c.** What is the work of your algorithm?

    $O(|E|lg|E|)$
