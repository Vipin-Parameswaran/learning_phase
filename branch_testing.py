# Product of Array except self

"""Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 """

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        len_nums = len(nums)
        leftprd_list = [0]* len_nums
        leftprd_list[0] = 1
        for i in range(1, len_nums):
            leftprd_list[i] = leftprd_list[i-1]*nums[i-1]
        result_list = [0]*len_nums
        mult_num = 1
        for j in reversed(range(len_nums)):
            result_list[j] = leftprd_list[j]*mult_num
            mult_num *= nums[j]
        return result_list
  
