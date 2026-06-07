from collections import deque

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)

        if "0000" in deadends:
            return -1

        que = deque([(["0", "0", "0", "0"], 0)])
        visit = {"0000"}

        while que:
            coord, count = que.popleft()

            if ''.join(coord) == target:
                return count

            for i in range(4):
                digit = int(coord[i])

                nxt = coord.copy()
                nxt[i] = str((digit + 1) % 10)
                state = ''.join(nxt)

                if state not in visit and state not in deadends:
                    visit.add(state)
                    que.append((nxt, count + 1))

                nxt = coord.copy()
                nxt[i] = str((digit - 1) % 10)
                state = ''.join(nxt)

                if state not in visit and state not in deadends:
                    visit.add(state)
                    que.append((nxt, count + 1))

        return -1