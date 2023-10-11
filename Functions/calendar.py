events = [[1, 4], [7, 10], [8, 8], [14, 23]]
wedding = int(input())
count = 0
for L in range(len(events)):
    print(events[L][0], events[L][1])
    if events[L][0] <= wedding and wedding <= events[L][1]:
        count = count + 1
print(count)
