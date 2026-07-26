class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        from collections import Counter
        party={"R":"Radiant","D":"Dire"}
        counts=Counter(senate)
        from collections import deque

        n=len(senate)

        r=deque()
        q=deque()
        for i in range(n):
            if senate[i]=="R":
                r.append(i)
            else:
                q.append(i)
        while r and q:
            tr=r.popleft()
            tq=q.popleft()
            if tr<tq:
                r.append(tr+n)
            else:
                q.append(tq+n)
        if r :
            return party["R"]
        else:
            return party["D"]

