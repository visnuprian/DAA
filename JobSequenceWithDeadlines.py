def printJobScheduling(arr, t):
 
    n = len(arr)

    for i in range(n):
        for j in range(n - 1 - i):
            if arr[j][2] < arr[j + 1][2]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
 
    result = [False] * t

    job = ['nil'] * t
 
    for i in range(len(arr)):

        for j in range(min(t - 1, arr[i][1] - 1), -1, -1):
 
            if result[j] is False:
                result[j] = True
                job[j] = arr[i][0]
                break
 
    print(job)
 
if __name__ == '__main__':
    arr = [['j1', 5, 85],  
              ['j2', 4, 25],
              ['j3', 3, 16],
              ['j4', 3, 40],
              ['j5', 4, 55],
              ['j6', 5, 19],
              ['j7', 2, 92],
              ['j8', 3, 80],
              ['j9', 7, 15]]
 
    print("Following is maximum profit sequence of jobs")
 
    printJobScheduling(arr, 7)