class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        answer = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in answer:
                return [i, answer[diff]]
            answer[v] = i
        return 0