def abc(n,m):
    for i in range(max(n,m),n*m+1):
        if (i%n==0) & (i%m==0):
            print(i)
            return 

n,m = input().split()
n = int(n)
m = int(m)

abc(n,m)