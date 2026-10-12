class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Hashmap and Prefix Sum
        zero, one = 0, 0
        diff_idx = {}
        res = 0
       
        try:
            for i, n in enumerate(nums):
                if n == 0:
                    zero += 1
                if n == 1:
                    one += 1
                if one - zero not in diff_idx:
                    diff_idx[one - zero] = i
                if one == zero:
                    res = one + zero
                else:
                    idx = diff_idx[one - zero]
                    res = max(res, i-idx)
            return res
        except Exception as e:
            print(e)
