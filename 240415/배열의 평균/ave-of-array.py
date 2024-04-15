arr2d= []
for i in range(2):
    arr1d = list(map(int,input().split()))
    arr2d.append(arr1d)

sum_1,sum_2,sum_3,sum_4,sum_5,sum_6,sum_all = 0,0,0,0,0,0,0
for j in range(4):
    sum_1 += arr2d[0][j]
    sum_2 += arr2d[1][j]
for i in range(2):
    sum_3 += arr2d[i][0]
    sum_4 += arr2d[i][1]
    sum_5 += arr2d[i][2]
    sum_6 += arr2d[i][3]
for i in range(2):
    for j in range(4):
        sum_all += arr2d[i][j]

print("%.1f %.1f"%(sum_1/4,sum_2/4))

print("%.1f %.1f %.1f %.1f"%(sum_3/2,sum_4/2,sum_5/2,sum_6/2))

print("%.1f"%(sum_all/8))