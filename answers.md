# CMPS 2200 Assignment 3
## Answers

**Name:** Emily Aymond


Place all written answers from `assignment-03.md` here for easier grading.

1a. Find the largest 2^k so that 2^k <= N. Then, subtract 2^k from N and keep subtracting 2^k until N <= 1. 


1b. This algorithm is optimal because k is at its largest possible value every time. We know this because the largest value one of our coins could have is always less than or equal to N, so there are no smaller coins to replace it without using more coins.


1c. Work: O(log n)

Span: O(log n)


2a. Consider D = {1, 3, 4} and N = 6. The greedy algorithm would choose 4 first, which would leave 2, forcing two ones to be used. This totals three coins. However, the most efficient way to do this would be to use two threes, using only two coins.


2b. This is an optimal substructure because it relies on solving smaller problems to take on larger ones


2c. In the top-down method, we have to take into account all of the substructures, so this makes the work and span O(n).