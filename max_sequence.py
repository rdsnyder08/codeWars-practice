"""
Maximum Subarray Sum

The maximum sum subarray problem consists in finding the maximum sum of a contiguous subsequence in an array or list of integers:

Status: solved
"""

def max_sequence(arr):
    if len(arr)==0:
        return 0
    max_ending_here = max_so_far = arr[0]

    for num in arr[1:]:
        max_ending_here = max(num, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    if max_so_far < 0:
        return 0
