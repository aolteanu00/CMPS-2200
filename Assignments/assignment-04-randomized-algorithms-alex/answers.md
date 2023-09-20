# CMPS 2200 Assignment 4
## Answers

**Name:**_________________________
**Name:**_________________________

Place all written answers from `assignment-04.md` here for easier grading.

**1 Quicksort probabilities**

- **1a.** What is the probability that Quicksort does $\Omega({n^2})$
  comparisons?  

  The probability that Quicksort performs $\Omega({n^2})$ comparisons is $(lnn)/n$

- **1b.** What is the probability that Quicksort does $10^c n \lg n$
comparisons, for a given $c>0$? What does this say about the
deviation of the actual work from the expected work for Quicksort?

    Let c' be the constant in the asymptotic runtime of Quicksort. Using Markov’s inequality we get that this probability is at most 
    c'/10^c. This means that it is extremely unlikely that Quicksort deviates very far from the expected runtime.

**2 From "Maybe" to "Definitely"**

- **2a.** Give an algorithm to improve the guaranteed success probability and state its work.

  Run A K times, and then check for correct output. If all runs fail return that the program failed. 

- **2b.** Show how to convert $\mathcal{A}$ into an
  algorithm that always produces the correct result, but has an
  expected runtime that depends on $w(n)$ and a success probability
  $\epsilon$.

  We run A until is succeeds. If A terminates, it has succeeded. The expected runtime is O(t(n)/epsilon)

**3 Determinism versus Randomization in Quicksort**

- **3b.** Compare running times using `compare-qsort` between variants of
Quicksort and the provided implementation of selection sort (`ssort`).

- **3c.** Compare the fastest of your sorting implementations to the Python sorting function `sorted`, conducting the tests in 3b above. 
