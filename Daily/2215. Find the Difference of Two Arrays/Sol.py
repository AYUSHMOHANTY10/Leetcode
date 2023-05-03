'''class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1, nums2 = set(nums1), set(nums2)
        return(nums1.difference(nums2), nums2.difference(nums1))'''
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        res=[]
        a=[]
        a=set(nums1) - set(nums2)
        b=[]
        b=set(nums2) - set(nums1)
        res.append(a)
        res.append(b)
        return res
