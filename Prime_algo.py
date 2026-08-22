import math


def odd_number_sieve(n, verbose=True):
    """
    Odd-skipping Sieve of Eratosthenes.

    Differences from the naive version:
      - Outer loop only visits odd numbers (evens handled in one shot).
      - Marking starts at i*i instead of 2*i (smaller multiples of i are
        already marked by smaller primes, so starting earlier is redundant).
      - Outer loop stops at sqrt(n) (anything past that can't mark anything
        new -- any composite <= n has a factor <= sqrt(n)).
      - Uses a bytearray instead of a set for marking (array indexing beats
        hashing).
    """
    if n < 2:
        return []

    # is_composite[i] == 1 means i is known composite. Index directly by
    # number (0 and 1 unused/ignored).
    is_composite = bytearray(n + 1)

    # Multiples of 2 (the only even prime) in one pass.
    for m in range(4, n + 1, 2):
        is_composite[m] = 1
    if verbose:
        print(f"2  -> marked {list(range(4, n + 1, 2))}")

    limit = int(math.isqrt(n))

    # Only need to sieve with odd i up to sqrt(n); beyond that, no i has
    # multiples <= n that haven't already been marked by a smaller prime.
    for i in range(3, limit + 1, 2):
        if is_composite[i]:
            if verbose:
                print(f"{i}  -> skipped (already marked composite)")
            continue
        start = i * i
        marked = list(range(start, n + 1, i))
        for m in marked:
            is_composite[m] = 1
        if verbose:
            print(f"{i}  -> marked {marked}")

    if verbose:
        print("=" * 40)

    composite_odds = [i for i in range(3, n + 1, 2) if is_composite[i]]
    prime_odds = [i for i in range(3, n + 1, 2) if not is_composite[i]]

    if verbose:
        print("Composite odd numbers:", composite_odds)
        print("Prime odd numbers:", prime_odds)

    return prime_odds


if __name__ == "__main__":
    n = int(input("Enter the nth term (upper limit): "))
    odd_number_sieve(n)
    