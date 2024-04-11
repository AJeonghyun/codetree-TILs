arr = list(map(int,input().split()))
odd = 0
even = 0
for i in range(0,10,2):
    odd+=arr[i]

for i in range(1,10,2):
    even+=arr[i]


if odd>even:
    print(odd-even)
else:
    print(even-odd)