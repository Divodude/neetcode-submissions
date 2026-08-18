class Solution:
    def maxProfit(self, price: List[int]) -> int:
        n = len(price)
        dp = {}

        def rec(i, buyed, sold):
            if i == n:
                return 0

            if (i, buyed, sold) in dp:
                return dp[(i, buyed, sold)]

            if sold:
                return 0

            if buyed is not None:
                psell = rec(i + 1, None, 1) + (price[i] - buyed)
                pskip = rec(i + 1, buyed, 0)

                dp[(i, buyed, sold)] = max(psell, pskip)

            else:
                pbuy = rec(i + 1, price[i], 0)
                pskip = rec(i + 1, None, 0)

                dp[(i, buyed, sold)] = max(pbuy, pskip)

            return dp[(i, buyed, sold)]

        return rec(0, None, 0)