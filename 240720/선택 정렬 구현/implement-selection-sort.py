n = int(input())
arr = list(map(int, input().split()))


length = len(arr)

for i in range (length-1):
    minmum = i
    for k in range (i+1,length):
        if arr[k] < arr[minmum]:
            minmum = k
    tmp = arr[i]
    arr[i] = arr[minmum]
    arr[minmum] = tmp


for i in arr:
    print(i,end=" ")