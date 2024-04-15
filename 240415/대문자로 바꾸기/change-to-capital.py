arr2d= []
for i in range(5):
    arr1d = list(map(str,input().split()))
    arr2d.append(arr1d)

for i in range(5):
    for j in range(3):
        print(arr2d[i][j].upper(),end=" ")
    print(end="\n")