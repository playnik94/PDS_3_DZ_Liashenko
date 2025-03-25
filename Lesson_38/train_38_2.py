#
# def solution(nums: list[int], target: int) -> list[int]:
#
#     for i in range(len(nums)):
#         for j in range(len(nums)):
#
#             if i != j and nums[i] + nums[j] == target:
#
#                 return [i, j]


def solution(nums: list[int], target: int) -> list[int]:

    db = {}

    for i, n in enumerate(nums):
        db[n] = i

    for i, n in enumerate(nums):
        pair = target - n

        if pair in db and db[pair] != i:
            return [i, db[pair]]


print(solution([2, 15, 11, 7], 9))