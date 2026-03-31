class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > 0 and len(nums2) > 0:
            if nums1[0] <= nums2[0]:
                a = nums1
                b = nums2
            else:
                a = nums2
                b = nums1
        elif len(nums1) == 0 and len(nums2) > 0:
            if len(nums2)%2 == 0:
                return ((nums2[len(nums2)//2] + nums2[(len(nums2)-1)//2])/2)
            else:
                return nums2[len(nums2)//2]
        elif len(nums2) == 0 and len(nums1) > 0:
            if len(nums1)%2 == 0:
                return ((nums1[len(nums1)//2] + nums1[(len(nums1)-1)//2])/2)
            else:
                return nums1[len(nums1)//2]

        while b[0] < a[len(a)-1]:
            target =  b[0]
            l, r = 0, len(a) - 1

            while l <= r:
                mid = (l+r)//2
            
                if a[mid] <= target <= a[mid+1]:
                    a.insert(mid+1, target)
                    b.pop(0)
                    break
                
                elif a[mid] < target:
                    l = mid + 1
                
                else:
                    r = mid - 1
            
            if len(b) <= 0: break
        
        a+=b

        if len(a)%2 == 0:
            return ((a[len(a)//2] + a[(len(a)-1)//2])/2)
        else:
            return a[len(a)//2]
        