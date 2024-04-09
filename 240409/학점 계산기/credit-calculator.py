n = int(input())

arr = list(map(float,input().split()))
sum_num = 0
for i in range(n):
    sum_num+=arr[i]

avg = float(sum_num/n)

print("%.1f"%avg)
if avg >= 4.0:
    print('Perfect')
elif avg >= 3.0:
    print('Good')
else:
    print('Poor')