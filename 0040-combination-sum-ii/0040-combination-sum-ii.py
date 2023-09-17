class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        def backtrack(combination, index, target):
            if target == 0:
                res.append(combination.copy())
                return
            if target <= 0:
                return
                
            prev = -1
            for i in range(index, len(candidates)):
                if candidates[i] == prev:
                    continue
                combination.append(candidates[i])
                backtrack(combination, i+1, target-candidates[i])
                combination.pop()
                prev = candidates[i]

        backtrack([], 0, target)
        return res
        