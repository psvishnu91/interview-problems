from typing import List

class Solution:

    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        start_cur = 0
        k = k%n
        if (k%n == 0):
            return
        tmp = None
        cur = 0
        next = (cur+ (k%n) + n)%n
        cnt = 1
        while (cnt <= n):
            tmp = nums[next]
            nums[next] = nums[cur]
            cur = next
            if (cur == start_cur):
                start_cur = cur
                cur = (cur+1)%n
                start_cur = cur
            next = (cur + (k%n) + n)%n
            cnt += 1


if __name__ == "__main__":
    a = [1,2,3,4]
    k = 2
    Solution().rotate(nums=a,k=k)
    print(a)