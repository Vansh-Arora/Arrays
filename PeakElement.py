def isPeak(arr,i):
    # if i == 0 and arr[i] > arr[i+1]
    # if i== n-1 and arr[i]>arr[i-1]
    # if arr[i]>= arr[i+1] and arr[i-1]
    if(i==0 or arr[i-1]<= arr[i]) and (i== len(arr)-1 or arr[i+1] <= arr[i]):
        return 1
    else:
        return 0
def peakHelper(arr,lo,hi):
    mid = (lo+hi)//2
    if isPeak(arr,mid):
        return mid
    if mid>0 and  arr[mid-1]>arr[mid]:
        return peakHelper(arr,lo,mid-1)
    return peakHelper(arr,mid+1,hi)
        
        
def peakElement(arr, n):
    # Code here'
    if n == 1:
        return 0
    return peakHelper(arr,0,n-1)

print(peakElement([1,2],2))