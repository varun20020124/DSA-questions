class Solution:
    def combinationSum2(self, nums, target):
        def backtrack(path,options,total):
            if total == target:
                result.append(path[:])
                return
            i = 0
            while i < len(options):
                if options[i] + total > target:
                    continue
                path.append(options[i])
                backtrack(path,options[i+1:],total + options[i])
                path.pop()
                j = i+1
                while j < len(options) and options[j] == options[i]:
                    j+=1
                i = j
        result = []
        nums.sort()
        backtrack([],nums,0)
        return result