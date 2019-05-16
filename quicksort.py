def partion(arr,low,high):
    i= (low-1)
    pivot = arr[high]
    for j in range(low,high):
        if arr[j]<=pivot:
            i = i+1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return (i+1)
    
    
def sorting(arr,low,high):
    if low<high:
        pi = partion(arr,low,high)
        partion(arr,low,pi-1)
        partion(arr,pi+1,high)
    

arr= list(map(int,input().split()))
n=0
n1 = len(arr)-1
sorting(arr,n,n1)
for i in arr:
    print(i,end=" ")
