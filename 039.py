class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        self.backtracking(candidates, target,[], ans)
        return ans

    def backtracking(self, candidates, target, temp, ans):
        if target == 0:
            ans.append(temp)

        else:
            for i, values in enumerate(candidates):
                if target < 0:
                    break
                self.backtracking(candidates, target - values, temp.append(values), ans)
