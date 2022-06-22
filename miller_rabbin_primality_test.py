#!/usr/bin/python3.10
from random import randint

from GoldbachsWeakConjecture.modular_exponentiation import mod_exp
from GoldbachsWeakConjecture.prime_enum import Primality

globals().update(Primality.__members__)  # puts Primality in the namespace of this file

is_even = lambda n: (n % 2) == 0


def primality_test(n: int, witnesses: int = 15) -> Primality:
    """
    Probabilistic Miller-Rabin test
    The algorithm declares a composite number incorrectly prime with a probability of at most
    1/4^`witnesses`. Both the Fermat's little theorem and the sequence test contribute equally to this
    probability.
    :param n: Number of choice to be primality tested
    :param witnesses: Sets tolerance of falsely concluding a prime.
    Time complexity: O(`witnesses` * log^3(n))
    :return: Enum of corresponding primality
    """
    if n == 2: return PROBABLY_PRIME
    if is_even(n) or n == 1: return COMPOSITE

    s = 0
    t = n - 1

    while is_even(t):
        # Factoring n - 1 in the form of (where t is odd): (2^s) * t
        s += 1
        t //= 2

    # run `witnesses`-times random tests
    for rand_witness in (randint(2, n - 1) for _ in range(witnesses)):



        # Design note: Expensive mod_exp op only done once at the start of the sequence test as subsequent sequence
        # elements rely upon the fact that: ( x^(2^(i-1)) * x^(2^(i-1)) ) mod z = ( x^(2^i) ) mod z
        previous_sequence = mod_exp(rand_witness, t, n)
        for i in range(1, s + 1):
            current_sequence = (previous_sequence * previous_sequence) % n
            if 1 != previous_sequence != n - 1 and current_sequence == 1:  # sequence test
                return COMPOSITE
            previous_sequence = current_sequence

        if previous_sequence != 1: return COMPOSITE  # Fermat's little theorem (2^(n-1) mod n)

    return PROBABLY_PRIME


if __name__ == '__main__':
    print(primality_test(1152271, 30))
