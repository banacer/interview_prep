import heapq


def merge_sorted_arrays(arrays):
    h = []
    iterators = [iter(l) for l in arrays]
    for it in iterators:
        element = next(it, None)
        if element is not None:
            heapq.heappush(h,element)
    res = []
    i = 0
    while h:
        e = heapq.heappop(h)
        res.append(e)
        e = next(iterators[i], None)
        if e is not None:
            heapq.heappush(h,e)
            i+=1
        else:
            del iterators[i]
        if len(iterators) > 0:
            i = i % len(iterators)
    return res


def sort_increase_decrease_array(l):
    it = []
    start = 0
    end = 1
    increasing = True
    if l[0] >= l[1]:
        increasing = False

    for i in range(1, len(l)):
        if l[i] > l[i-1]:
            if increasing:
                end = i
            else:
                it.append((start, end, increasing))
                start = i
                increasing = True
        else:
            if not increasing:
                end = i
            else:
                it.append((start, end, increasing))
                start = i
                increasing = False
    if (start, end, increasing) not in it:
        it.append((start, end, increasing))
    h = []
    idx = [start if increasing else end for start,end,increasing in it]
    for i in range(len(idx)):
        e = l[idx[i]]
        heapq.heappush(h, e)
        if it[i][2] == True:
            idx[i]+=1
        else:
            idx[i]-=1
    res = []
    count = 0
    while h:
        e = heapq.heappop(h)
        res.append(e)
        print 'pushing',e
        e = l[idx[count]]
        heapq.heappush(h, e)
        if it[count][2] == True:
            idx[count]+=1
            if idx[count] > it[count][1]: #larger than end then we need to remove this index
                del idx[count]
                del it[count]
                count-=1
        else:
            idx[count]-=1
            if idx[count] < it[count][0]: #larger than end then we need to remove this index
                del idx[count]
                del it[count]
                count-=1
        count+=1
    return res




if __name__ == '__main__':
    #l = [[3,5,7],[0,6],[0,6,28]]
    #print merge_sorted_arrays(l)
    print sort_increase_decrease_array([57,131,493,294,221,339,418,452,442,190])
