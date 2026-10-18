def merge_intervals(intervals):
    intervals = sorted(intervals)
    merged = [intervals[0]]
    for i in range(1, len(intervals)):
        start = intervals[i][0]
        end = intervals[i][1]
        if start <= merged[-1][1]:
            merged[-1][1] = max(end, merged[-1][1])
        else:
            merged.append([start, end])
    return merged

class Solution:
    def minSelection(self, availableIntervals: List[List[int]], targetIntervals: List[List[int]]) -> int:
        merged_targetIntervals = merge_intervals(targetIntervals)
        availableIntervals = sorted(availableIntervals)

        if not merged_targetIntervals:
            return 0
        i = 0
        ans = 0
        covered = float("-inf")

        for left, right in merged_targetIntervals:
            while covered < right or covered < left:
                now = max(left, covered)
                best_end = covered
                while i < len(availableIntervals) and availableIntervals[i][0] <= now:
                    best_end = max(best_end, availableIntervals[i][1])
                    i += 1
                if best_end <= covered or best_end < left:
                    return -1
                covered = best_end
                ans += 1

        return ans
