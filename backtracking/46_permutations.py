class Solution:
    def permute(self,nums):
        def backtrack(path,options):
            if len(options) == 0:
                result.append(path[:])
                return 
            for i,option in enumerate(options):
                path.append(option)
                backtrack(path,options[:i]+options[i+1:])
                path.pop()
        result = []
        backtrack([],nums)
        return result