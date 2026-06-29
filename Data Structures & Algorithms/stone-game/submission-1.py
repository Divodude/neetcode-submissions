class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}
        total = sum(piles)

        def rec(start, end, turn):
            if start > end:
                return 0

            if (start, end, turn) in dp:
                return dp[(start, end, turn)]

            if turn:  
                ans = max(
                    piles[start] + rec(start + 1, end, False),
                    piles[end] + rec(start, end - 1, False)
                )
            else:     
                ans = min(
                    rec(start + 1, end, True),
                    rec(start, end - 1, True)
                )

            dp[(start, end, turn)] = ans
            return ans

        alice = rec(0, len(piles) - 1, True)
        bob = total - alice

        return alice > bob