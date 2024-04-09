arr = list(map(int,input().split()))
cnt = 0
sum_num = 0
for i in arr:
    if i==0:
        break
    elif i%2==0:
        sum_num+=i
        cnt+=1

print(f"{cnt} {sum_num}")