def solution(numbers, target):
    idx = 0 
    curr = 0

    def dfs(nums, target, curr, idx):
        if idx == len(nums):
            if curr == target:
                return 1
            else:
                return 0

        return dfs(nums, target, curr + nums[idx], idx + 1) \
                + dfs(nums, target, curr - nums[idx], idx + 1)

    answer = dfs(numbers, target, idx, curr)
    return answer