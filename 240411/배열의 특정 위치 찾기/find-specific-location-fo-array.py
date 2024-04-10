arr = list(map(int,input().split()))
summ = 0
avg = 0
cnt = 0
for i in range(1,10,2):
    summ+=int(arr[i])

for i in range(2,10,3):
    avg+=int(arr[i])
    cnt+=1
print("%d %.1f"%(summ,avg/cnt))