class Solution:
    def sieve_of_eratosthenes(self, n):
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

    def maxPrimes(self, n: int, s: int) -> list[int]:
        primes = self.sieve_of_eratosthenes(n)
        ans = []
        val = 0
        for i in range(len(primes)):
            val += primes[i]
            if val <= s:
                ans.append(primes[i])
            else:
                break
        return ans