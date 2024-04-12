n = int(input())

arr= [1,n]

for i in range(3,100):
    arr.append(arr[-1]+arr[-2])

    

for elem in arr:
    print(elem,end=" ")
    if elem > 100:
        break