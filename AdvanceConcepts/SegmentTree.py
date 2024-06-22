arr = [1, 0, 3, 2, 4, 2, 1]
query = [[1, 3], [3, 6], [2, 5]]

# Initialize the segment tree array
segTree = [0] * (4 * len(arr))

def buildSegmentTree(index, low, high, arr, segTree):
    if low == high:
        segTree[index] = arr[low]
        return 

    mid = (low + high) // 2
    
    buildSegmentTree(2 * index + 1, low, mid, arr, segTree)
    buildSegmentTree(2 * index + 2, mid + 1, high, arr, segTree)
    
    segTree[index] = min(segTree[2 * index + 1], segTree[2 * index + 2])

# Build the segment tree
buildSegmentTree(0, 0, len(arr) - 1, arr, segTree)
print(segTree)