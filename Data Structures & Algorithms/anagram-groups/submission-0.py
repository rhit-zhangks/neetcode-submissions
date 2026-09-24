class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sublists = {}
        for s in strs:
            freq = [0] * 26
            for l in s:
                freq[ord(l) - 97] += 1
            freq = tuple(freq)
            if freq in sublists.keys():
                sublists[freq].append(s)
            else:
                sublists[freq] = [s]
        return list(sublists.values())