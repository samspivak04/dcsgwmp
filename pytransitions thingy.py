# use networkx and matplotlib to model finite state machine
# create finite state machine in pytransitions
# look for weird state transitions!
from transitions import Machine
import random



# class Solution(object):
#     def containsNearbyDuplicate(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: bool
#         """
#         if (len(set(nums)) != len(nums)):
#             for i in range(len(nums)):
#                 for j in range(len(nums)):
#                     if (i != j):
#                         if (abs(i - j) <= k) and (nums[i] == nums[j]):
#                                 return (nums[i] == nums[j]) and (abs(i - j) <= k)
#         return False
#
# nums = [1, 2, 3, 1]
# k = 3
# test = Solution()
# test.containsNearbyDuplicate(nums, k)