def abc(n,m):
    for i in range(1,n+1):
        if(n%i==0) & (m%i==0):
            max = i
    print(max)

n,m =input().split()
n = int(n)
m = int(m)

abc(n,m)