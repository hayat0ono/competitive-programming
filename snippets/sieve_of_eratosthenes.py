# Return all primes up to and including n.
def sieve_of_eratosthenes(n):
    if n < 2:
        return []

    prime_flags = [True] * (n + 1)

    prime_flags[0] = prime_flags[1] = False

    for i in range(2, int(n**0.5) + 1):
        if prime_flags[i]:
            for j in range(i*i, n+1, i):
                prime_flags[j] = False

    primes = [i for i in range(2, n+1) if prime_flags[i]]

    return primes
