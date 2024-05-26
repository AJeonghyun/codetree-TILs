def abc(n):
    num = 0
    for i in range(1,n+1):
        num+=i
    return (int(num/10))


n = input()
n = int(n)
print(abc(n))