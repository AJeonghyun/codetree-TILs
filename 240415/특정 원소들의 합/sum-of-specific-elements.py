arr_2d = [
	list(map(int, input().split()))
	for _ in range(4)
]
sum_num = 0
for i in range(4):
    for j in range(i+1):
        sum_num+=arr_2d[i][j]

print(sum_num)