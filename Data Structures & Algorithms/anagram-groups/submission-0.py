class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        seen = defaultdict(list)

        for item in range(len(strs)):
            sortedWord = ''.join(sorted(strs[item]))
            seen[sortedWord].append(strs[item])
        
        return list(seen.values())
            

        