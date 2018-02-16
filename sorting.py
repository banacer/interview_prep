
def quicksort(arr, low, high):
    i = (low - 1)  # index of smaller element
    pivot = arr[high]  # pivot

    for j in range(low, high):

        # If current element is smaller than or
        # equal to pivot
        if arr[j] <= pivot:
            # increment index of smaller element
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            print 'swap',
        print arr
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return (i + 1)
def find_smallest_nonconstructible_value(nums):
    cumsum = []
    cum = 0
    for n in nums:
        cum+=n
        cumsum.append(cum)
    for i in range(1,len(cumsum)):
        if cumsum[i] -cumsum[i-1] > 1:
            return cumsum[i-1]+1
    return -1


if __name__ == '__main__':
    #l = [8,1,4,6,7,5]
    #quicksort(l,0,len(l)-1)
    #print l
    print find_smallest_nonconstructible_value([1,1,1,1,1,5,10,25])
