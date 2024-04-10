n = int(input())
cnt = 0
index = []
arr = list(map(int, input().split()))

for i in range(n):
    if arr[i]%2==0:
        index.append(arr[i])
        cnt+=1


for j in range(cnt-1,-1,-1):
    print(index[j],end=" ")