arr_2d= []

for i in range(4):
    arr = list(map(int,input().split()))
    arr_2d.append(arr)


for i in range(0,4):
    sum_num = 0
    for j in range(0,4):
        sum_num+=arr_2d[i][j]
    print(sum_num)