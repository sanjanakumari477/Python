Q. Find the second largest number in a list
Ans:-
def second_largest(nums):
    nums = list(set(nums))
    nums.sort()
    return nums[-2]
