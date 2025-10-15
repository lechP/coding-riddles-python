def merge_high_definition_intervals(intervals):
    if not intervals:
        return []

    k = 0
    intervals.sort(key=lambda x: (x[0], x[1]))
    merged = []
    left, right = intervals[0]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= right:
            right = max(right, intervals[i][1])
        else:
            merged.append([left, right])
            left, right = intervals[i]

    merged.append([left, right])
    return merged

def main():
    _input = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(merge_high_definition_intervals(_input))

if __name__ == "__main__":
    main()

