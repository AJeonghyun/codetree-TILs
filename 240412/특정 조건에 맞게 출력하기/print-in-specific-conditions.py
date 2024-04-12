arr = list(map(int,input().split()))

for elem in arr:
    if elem==0:
        break
    elif elem%2==1:
        print(elem+3,end=" ")
    elif elem%2==0:
        print(elem//2,end=" ")