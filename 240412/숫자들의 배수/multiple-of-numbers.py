n = int(input())

arr = []
cnt = 0
for i in range(1,100):
    arr.append(n*i)

for elem in arr:
    print(elem,end=" ")
    if elem%5==0:
        cnt+=1
    if cnt==2:
        break