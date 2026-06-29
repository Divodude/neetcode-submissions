class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        dp = {}
        total = sum(piles)

        def rec(start, end):
            if (end-start+1)%2==0 :
                turn=True
            else:
                turn =False
            if start > end:
                return 0

            if (start, end) in dp:
                return dp[(start, end)]

            if turn:  
                ans = max(
                    piles[start] + rec(start + 1, end),
                    piles[end] + rec(start, end - 1)
                )
            else:     
                ans = min(
                    rec(start + 1, end),
                    rec(start, end - 1)
                )

            dp[(start, end)] = ans
            return ans

        alice = rec(0, len(piles) - 1)
        bob = total - alice

        return alice > bob