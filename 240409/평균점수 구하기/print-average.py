arr = list(map(float,input().split()))

sum_num = 0
for i in range(8):
    sum_num+=arr[i]

avg = float(sum_num/8)

print("%.1f"%avg)