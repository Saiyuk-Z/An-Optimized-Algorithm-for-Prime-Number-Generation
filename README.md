## Optimized Prime Number Generation Algorithm

An optimized prime-number generation algorithm designed to reduce unnecessary computation while maintaining the same asymptotic complexity as conventional sieve-based approaches.
The algorithm uses an odd-only search space, begins composite marking at i², limits the outer loop to √n, and uses a compact byte-based representation for composite-number marking.

#Overview

The algorithm generates all prime numbers up to a given upper limit n.
Its optimization strategy is based on three principles:
 • Even numbers greater than 2 are     immediately treated as composite.
• Only odd candidates need to be examined after handling 2.
• Composite marking begins at i², avoiding work that has already been performed by smaller factors.

These optimizations reduce unnecessary iterations and memory overhead while preserving the underlying sieve complexity.

#Algorithm

For an upper limit n:
 •Handle the even numbers separately.
•Consider only odd candidate factors starting from 3.
•Continue the factor search only up to √n.
•Ignore candidates that have already been identified as composite.
•For every remaining candidate, mark its multiples beginning at i².
•After the marking process is complete, the remaining unmarked odd numbers are prime.

Starting at i² is important because all smaller multiples of i have already been handled by smaller factors.

#Complexity

Time Complexity
O(n log log n)

The asymptotic complexity remains in the same class as the standard sieve approach. The optimizations primarily reduce the constant factors rather than changing the Big-O complexity.

Space Complexity
O(n)

The implementation uses a compact byte-based structure for tracking composite numbers, requiring approximately one byte per number up to n.

#Performance

The algorithm is designed to reduce practical computation through:
•An odd-only candidate space
•A √n termination bound for the outer loop
•Composite marking beginning at i²
•Compact composite-state storage
•Reduced redundant marking operations

These optimizations can produce substantially lower execution time in practical benchmarks while maintaining O(n log log n) time complexity.
 -Benchmark results should be reported     separately with the exact hardware,  implementation, input size, number of runs, and measurement method used.

#Correctness

The algorithm relies on the fundamental property that every composite number ≤ n has at least one factor ≤ √n.

Therefore, once all eligible factors up to √n have been processed, every remaining unmarked candidate is prime.

#Project Structure
.
├── odd_number_sieve.py
└── README.md

The complete implementation, including the optional step-by-step verbose output, is contained in odd_number_sieve.py.

#Demonstration

For an upper limit such as 50, the program can display the marking process and then produce the resulting prime numbers.
The verbose mode is useful for examining the algorithm's behavior and verifying which values are marked as composite during each stage.
