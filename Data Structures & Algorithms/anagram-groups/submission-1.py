class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict

        count = defaultdict(list)

        for word in strs:
            sortedWord = ''.join(sorted(word))
            count[sortedWord].append(word)
        return list(count.values())