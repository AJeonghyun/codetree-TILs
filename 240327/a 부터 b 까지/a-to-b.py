arr = input().split()

a = int(arr[0])
b = int(arr[1])


while a<=b:
    if(a%2==0):
        print(a,end=" ")
        a+=3
    else:
        print(a,end=" ")
        a*=2