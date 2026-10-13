class Solution:
    def checkDivisibility(self, n: int) -> bool:
        res = []
        t = n
        while t > 0:
            res.append(t % 10)
            t //= 10
        sums = sum(res)
        sums_product = 1
        for i in res:
            sums_product *= i
        total = sums + sums_product
        return n % total == 0
