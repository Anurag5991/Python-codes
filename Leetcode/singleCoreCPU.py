import heapq
def getOrder(tasks):
    for i, t in enumerate(tasks):
        t.append(i)
    
    res, minHeap = [], []
    i, time = 0, tasks[0][0]

    while minHeap or i < len(tasks):
        while i < len(tasks) and time >= tasks[i][0]:
            heapq.heappush(minHeap, [tasks[i][1], tasks[i][2]])
            i += 1

        if not minHeap:
            time = tasks[i][0]
        else:
            proctime, index = heapq.heappop(minHeap)
            time += proctime
            res.append(index)
    return res

print(getOrder([[1,2],[2,4],[3,5],[4,1]]))