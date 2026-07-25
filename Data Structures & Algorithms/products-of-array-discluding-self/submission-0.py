class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre = [1]
        for n in nums[:-1]:
            pre.append(pre[-1]*n)
        post = [1]
        for i in range(len(nums)-1, 0, -1):
            post.append(post[-1]*nums[i])
        post = post[::-1]
        return [pre[i]*post[i] for i in range(len(pre))]