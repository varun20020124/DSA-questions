class Solution:
    def subsetsWithDup(self, nums):
        def backtrack(path,options):
            result.append(path[:])
            i = 0
            while i < len(options):
                path.append(options[i])
                backtrack(path,options[i+1:])
                path.pop()
                j = i+1
                while j < len(options) and options[i] == options[j]:
                    j+=1
                i = j
        result = []
        nums.sort()
        backtrack([],nums)
        return result