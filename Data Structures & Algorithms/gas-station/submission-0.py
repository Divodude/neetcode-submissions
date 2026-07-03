class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        def reach_check(start):
            gs = 0
            i = start
            cnt = 0

            while cnt < n:
                gs += gas[i]
                if gs < cost[i]:
                    return False
                gs -= cost[i]
                i = (i + 1) % n
                cnt += 1

            return True
        for i in range( len(gas)):
            if reach_check(i):
                return i
        return -1

                

