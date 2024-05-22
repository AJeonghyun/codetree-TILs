n,m = input().split()
n = int(n)
m = int(m)
# 첫 번째 2차원 배열을 구현해 정수를 입력받습니다.
arr_1 = [
    [0 for _ in range(m)]
    for _ in range(n)
]


# 두 번째 2차원 배열을 구현해 정수를 입력받습니다.
arr_2 = [
    [0 for _ in range(m)]
    for _ in range(n)
]

# 2차원 배열을 구현합니다.
arr_3 = [
    [0 for _ in range(m)]
    for _ in range(n)
]

# 두 배열의 곱을 새로운 배열에 담습니다.
for i in range(n):
    for j in range(m):
        if arr_1[i][j] == arr_2[i][j]:
            arr_3[i][j] = 0
        else:
            arr_3[i][j] = 1
	
# 새로운 배열을 출력합니다.
for row in arr_3:
	for elem in row:
		print(elem, end=" ")
	print()