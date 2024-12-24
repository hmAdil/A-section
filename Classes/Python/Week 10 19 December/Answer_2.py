# def find_combinations(nums,target):
#     def backtrack(remaining, combo, start):
#         if remaining == 0:
#             result.append(list(combo))
#             return
#         elif remaining < 0:
#             return
#         for i in range(start, len(nums)):
#             combo.append(nums[i])
#             backtrack(remaining - nums[i], combo, i)
#             combo.pop()
#     nums = sorted(nums)
#     result = []
#     backtrack(target, [], 0)
#     return result
# nums_str = input()
# nums_lst=nums_str.split(" ")
# nums=[]
# for i in nums_lst:
#     nums.append(int(i))
# target = int(input())
# print(find_combinations(nums, target))

#or

# def find_combos(nums, goal):
#     def diff_combos(remaining, start, combi, result):
#         if remaining == 0:
#             result.append(list(combi))
#             return

#         for i in range(start, len(nums)):
#             if nums[i] > remaining:  
#                 continue

#             combi.append(nums[i])

#             diff_combos(remaining - nums[i], i, combi, result)  

#             combi.pop()
#     nums.sort()
#     result = []
#     diff_combos(goal, 0, [], result)
#     return result

# nums =list(map(int, input().split())) #[2, 3, 6, 7]
# goal = int(input())
# print(find_combos(nums, goal))