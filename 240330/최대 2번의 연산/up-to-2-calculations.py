n = input()
n = int(n)

if n%2==0:
    n = n // 2

if n%2==1:
    n = (n+1) // 2

print(n)