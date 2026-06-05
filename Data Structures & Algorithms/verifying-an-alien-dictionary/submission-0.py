class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        dic = {}
        for i, ch in enumerate(order):
            dic[ch] = i

        def lexo(word1, word2):

            for j in range(min(len(word1), len(word2))):

                if word1[j] != word2[j]:

                    return dic[word1[j]] < dic[word2[j]]

            return len(word1) <= len(word2)

        n = len(words)

        for i in range(1, n):

            if not lexo(words[i - 1], words[i]):
                return False

        return True