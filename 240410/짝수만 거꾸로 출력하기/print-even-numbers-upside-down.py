n = int(input())

for i in range(n):
    arr = list(map(int, input().split()))
    if arr[i]%2==0:
        print(arr[i],end=" ")