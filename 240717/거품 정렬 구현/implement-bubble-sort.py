n = int(input())

arr = list(map(int, input().split()))
for i in range (n):
    for j in range (n-i-1):
        if arr[j] > arr[j+1]:
            tmp = arr[j]
            arr[j] = arr[j+1]
            arr[j+1] = tmp


for i in arr:
    print(i,end=" ")