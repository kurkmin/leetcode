class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Modify nums1 instead of creating a new array ! 
        i = j = 0
        ans = []
        while i < m and j < n:
            if nums1[i] < nums2[j]:
                ans.append(nums1[i])
                i += 1
            else:
                ans.append(nums2[j])
                j += 1
        while i < m:
            ans.append(nums1[i])
            i += 1
        while j < n:
            ans.append(nums2[j])
            j += 1
        print(ans)

        """
        Do not return anything, modify nums1 in-place instead.
        """
