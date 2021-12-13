def binarySearchIndexAndComparisons(L,k,count = 0):
    if L == []:
        return False,count+1
    mid = len(L)//2
    if L[mid] == k:
        return (True,count+1)
    elif L[mid] < k:
        return binarySearchIndexAndComparisons(L[mid+1:],k,count+1)
    else:
        return binarySearchIndexAndComparisons(L[:mid-1],k,count+1)