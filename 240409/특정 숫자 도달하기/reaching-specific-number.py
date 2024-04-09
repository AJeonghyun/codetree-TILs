arr = list(map(int,input().split()))

sum_num = 0
a = 0
for i in arr:
    if i<250:
        sum_num+=i
        a+=1
    else:
        break

avg=float(sum_num/a)

print("%d %.1f"%(sum_num,avg))