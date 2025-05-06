from collections import defaultdict
class Solution:
    def groupAnagrams(self,strs):
        hashmap = defaultdict(list)
        for string in strs:
            count = [0]*26
            for i in range(len(string)):
                count[ord(string[i])-ord('a')]+=1
            hashmap[tuple(count)].append(string)
        anagram = []
        for val in hashmap.values():
            anagram.append(list(val))
        return anagram