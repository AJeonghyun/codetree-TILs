arr_2d = []

for _ in range(4):
    arr_1d = list(map(int,input().split()))
    arr_2d.append(arr_1d)
    sum_num =sum(arr_1d)
    print(sum_num)