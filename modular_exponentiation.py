#!/usr/bin/python3.10
def mod_exp(base, exponent, modulus):
    """Right-to-left method for modular exponentiation. Of the form `base`^`exponent` mod `modulus`"""

    if modulus == 1: return 0

    base = base % modulus
    result = 1
    while exponent > 0:
        if exponent % 2 == 1: result = (result * base) % modulus
        base = (base * base) % modulus
        exponent //= 2

    return result


if __name__ == "__main__":
    print(mod_exp(132905, 21341, 1213))
