arr = list(map(int,input().split()))
cnt = 0
sum_num = 0
for i in arr:
    if i==0:
        break
    else:
        sum_num+=i
        cnt+=1
print("%d %.1f"%(sum_num,float(sum_num/cnt)))