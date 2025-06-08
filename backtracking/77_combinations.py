class Solution:
    def combine(self, n, k):
        def backtrack(path,options):
            if len(path)==k:
                result.append(path[:])
                return
            for i, option in enumerate(options):
                path.append(option)
                backtrack(path,options[i+1:])
                path.pop()
        result = []
        nums = [i for i in range(1,n+1)]
        backtrack([], nums)
        return result