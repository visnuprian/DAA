print("Enter the size of the array")
n=int(input())
print("Enter the elements one after another")
arr=[]
for i in range(n):
    arr.append(int(input()))    
print("Array after sorting is  ")
for i in range(len(arr)):	
	min_idx = i
	for j in range(i+1, len(arr)):
		if arr[min_idx] > arr[j]:
			min_idx = j	
	arr[i], arr[min_idx] = arr[min_idx], arr[i]
print(arr)
print("Enter the Key value")
k=int(input())
def binarysearch(arr, l, r, x):  
    if r >= l:
        mid = l + (r - l) // 2        
        if arr[mid] == x:   
            return mid
        elif arr[mid] > x:
            return binarysearch(arr, l, mid-1, x)
        else:
            return binarysearch(arr, mid + 1, r, x)
    else:
        return -1
result = binarysearch(arr, 0, len(arr)-1, k) 
if result != -1:
    print("Element is present at index % d" % result)
else:
    print("Element is not present in array")