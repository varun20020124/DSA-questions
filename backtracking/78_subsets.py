class Solution:
    def subsets(self, nums):
        result = []
        def backtrack(path, options):
            result.append(path[:])
            for i,option in enumerate(options):
                path.append(option)
                backtrack(path,options[i+1:])
                path.pop()
        backtrack([],nums)
        return result