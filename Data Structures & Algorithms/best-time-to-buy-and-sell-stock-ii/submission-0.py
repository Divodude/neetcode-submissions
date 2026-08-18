class Solution:
    def maxProfit(self, price: List[int]) -> int:
        n = len(price)
        dp = {}

        def rec(i, buyed):
            if i == n:
                return 0

            if (i, buyed) in dp:
                return dp[(i, buyed)]


            if buyed is not None:
                psell = rec(i + 1, None) + (price[i] - buyed)
                pskip = rec(i + 1, buyed)

                dp[(i, buyed)] = max(psell, pskip)

            else:
                pbuy = rec(i + 1, price[i])
                pskip = rec(i + 1, None)

                dp[(i, buyed)] = max(pbuy, pskip)

            return dp[(i, buyed)]

        return rec(0, None)