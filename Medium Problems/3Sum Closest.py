class Solution(object):

  def threeSumClosest(self, nums, target):
    """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
    nums.sort()
    closest_sum = float('inf')

    for i in range(len(nums) - 2):
      left = i + 1
      right = len(nums) - 1

      while left < right:
        current_sum = nums[i] + nums[left] + nums[right]

        # Exact match found
        if current_sum == target:
          return current_sum

        # Update closest sum if current sum is closer
        if abs(target - current_sum) < abs(target - closest_sum):
          closest_sum = current_sum

        # Adjust pointers
        if current_sum < target:
          left += 1
        else:
          right -= 1

    return closest_sum