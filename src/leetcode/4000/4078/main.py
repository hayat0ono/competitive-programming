class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        if n % 2 == 1:
            return False
        n /= 2
        fibonacci = [0, 1]
        while True:
            fibonacci.append(fibonacci[-2] + fibonacci[-1])
            if n == fibonacci[-1]:
                return True
            elif fibonacci[-1] > n:
                return False