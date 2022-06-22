#!/usr/bin/python3.10
import sys
from time import perf_counter

from miller_rabbin_primality_test import primality_test


def disprove_conjecture(n) -> tuple[int, int, int] | bool:
    """
    Goldbach's weak conjecture: Every odd number N > 7 is a sum of three odd primes.
    'Odd' as it is not including 2.
    Note that as n increases, more tests are performed on the possible solution space, which increases the likelihood of
    incorrectly declaring a composite number is a prime. This increases the overall chance of returning an invalid
    triple. This is only of concern if accuracy is paramount, over efficiency. One could, scale the number of witnesses
    with n.

    Time complexity: average case is based on (unproven) invariant that there is always a triple with a 3, resting on
    Goldbach's strong (binary) conjecture.
        - Best case: O(nlog^3(n))
        - Worst case: O(n^2 * log^3(n))
    :return If false, GWC has been disproved. If a triplet, then we haven't been able to disprove GWC.
    """

    if n <= 7 or n % 2 == 0:
        raise Exception("{} does not satisfy the precondition for Goldbach's weak conjecture".format(n))

    for i in range(3, n - 5, 2):
        if not primality_test(i).value: continue
        for j in range(i, n - 2, 2):
            if primality_test(j).value and primality_test(n - j - i).value:
                return i, j, n - j - i

    return False  # Goldbach's weak conjecture violated


def disprove_conjecture_cli() -> None:
    """Command line version of Goldbach's weak conjecture disprover"""
    number = int(sys.argv[1])
    triplet = disprove_conjecture(number)
    with open("output_threeprime.txt", "w") as output_file:
        output_file.write("{} {} {}".format(*triplet))


if __name__ == "__main__":
    t_start = perf_counter()
    print(disprove_conjecture(66178434513578438715761814543874653487436543874654311541561516487543434873))
    print("Time Elapsed: ", perf_counter() - t_start)
    # disprove_conjecture_cli()
