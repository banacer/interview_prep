import heapq
import collections
def compute_optimum_task_assignment(l, N):
    l.sort(reverse=True)
    h = [0 for _ in range(N)]
    for i in l:
        e = heapq.heappop(h)
        heapq.heappush(h,e+i)
    return max(h)

def schedule_minimize_time(l):
    l.sort()
    count = 0
    sum = 0
    for i in l:
        sum+=count
        count+=i

    return sum
def interval_covering_problem(l):
    Interval = collections.namedtuple('interval', ('left','right'))
    intervals = []
    for i in l:
        intervals.append(Interval(i[0],i[1]))
    intervals.sort(key=lambda x: x.right)
    res = []
    for i in intervals:
        if not res or (res and res[-1] < i.left):
            res.append(i.right)
    return res

def find_majority(l):
    candidate = None
    count = 0
    for c in l:
        if not candidate or count == 0:
            candidate = c
            count = 1
        if candidate == c:
            count+=1
        else:
            count-=1
            if count == 0:
                candidate = c
                count = 1
    return candidate
def find_gasup(gallons, cities):
    total_distance = sum(cities)
    total_gallons = sum(gallons)
    mpg = total_distance/total_distance
    for i in range(len(cities)):
        if cities[i]/gallons[i] == mpg or cities[i-1]/gallons[i] == mpg:
            return i
    return -1

def max_trapped_water(l):
    i = 0;
    j = len(l)-1
    max_area = 0

    while i < j:
        area = min(l[i],l[j])*(j-i)
        if area > max_area:
            max_area = area
        if l[i] > l[j]:
            j-=1
        else:
            i+=1
if __name__ == '__main__':
    assert compute_optimum_task_assignment([5,2,1,6,4,4],3) == 8
    assert schedule_minimize_time([2,5,1,3]) == 10
    assert interval_covering_problem([[1,2], [2,3],[3,4], [2,3],[2,3],[3,4],[4,5]]) == [2,4]
    assert find_majority(list('bacaabaaca')) == 'a'
    assert max_trapped_water([1,2,1,3,4,4,5,6,2,1,3,2,1,2,4]) == 48