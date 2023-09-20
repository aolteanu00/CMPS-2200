# CMPS 2200 Assignment 3
## Answers

**Name:** Alex Olteanu

Place all written answers from `assignment-03.md` here for easier grading.

**1: Searching Unsorted Lists**

- **1b.** Work and span of `isearch` implementation

        The work of 'isearch' is $O(n)$  and the span of 'isearch' is $O(n)$ 
        
- **1d.** Work and span of `rsearch` implementation

        The work of 'rsearch' is $O(n)$ and the span of 'rsearch' is $O(lg n)$
        
- **1e.** Work and span of `rsearch` using `ureduce`

        The work of 'rsearch' using 'ureduce' is $O(n)$ and the span of 'rsearch' using 'ureduce' is $O(lg n)$
        
**3: Parenthesis Matching**

- **3b.** Recurrences and Big-Oh solutions for `parens_match_iterative`

        The reccurence for 'parens_match_iterative' is $W(n) = n + 2W(n/2)$ 
        Work is O(n)
        Span is O(n)

- **3d.** Work and Span for `parens_match_scan`

        The work of 'parens_match_scan' is $O(n)$ and the span of 'parens_match_scan' is $O(lg n)$

- **3f.** Recurrences and Big-Oh solutions for `parens_match_dc_helper`

        The reccurence for 'parens_match_dc_helper' is $W(n) = 2W(n/2)$ 
        Work is O(n)
        Span is O(n)
