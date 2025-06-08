class Solution:
    def combinationSum(self, nums, target):
        def backtrack(path,options,total):
            if total == target:
                result.append(path[:])
                return 
            for i, option in enumerate(options):
                if total + option > target:
                    continue
                path.append(option)
                backtrack(path,options[i:],total + option)
                path.pop()
        result = []
        backtrack([],nums,0)
        return result