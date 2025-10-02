# Example 1: Given an array of positive integers nums and an integer k, 
# find the length of the longest subarray whose sum is less than or equal to k. 
# This is the problem we have been talking about above. We will now formally solve it.

def find_length(nums, k):
    left = curr = answer = 0 
    for right in range(len(nums)): 
        curr += nums[right]
        if curr > k: 
            curr -= nums[left]
            left += 1
        answer = max(answer, right - left + 1)
    return answer
        

# Test cases 
nums = [3, 1, 2, 7, 4, 2, 1, 1, 5] 
k = 8 

print(find_length(nums, k))
