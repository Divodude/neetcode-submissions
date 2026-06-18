class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        from collections import defaultdict
        map=defaultdict(list)
        
        def compare(s1,s2):

            limit=min(len(s1),len(s2))
            idx=0
            while idx<limit:
                if s1[idx]!=s2[idx]:
                   
                    map[s1[idx]].append(s2[idx])
                    break
                idx+=1
        for i in range(1,len(words)):
            if words[i] in words[i-1] and len(words[i])<len(words[i-1]):
                return ""
            
            compare(words[i-1],words[i])
  
        self.order=[] 
        visit=set()
        def dfs(node,path):
            if node in visit:
                return True
            if node in path:
                return False

            
            path.add(node)
            for nei in map[node]:
                if nei not in visit:
                    if not dfs(nei,path):
                        return False
            self.order.append(node)
            visit.add(node)

            return True
        chars = set()

        for word in words:
            for ch in word:
                chars.add(ch)

        for ch in chars:
            if ch not in visit:
                if not dfs(ch,set()):
                    return ""

        return "".join(self.order[::-1])





        