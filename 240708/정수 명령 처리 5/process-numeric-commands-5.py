a = int(input())
arr = []

for i in range(a):
    command = input().split()
    
    if command[0] == 'push_back':
        arr.append(int(command[1]))
    elif command[0] == 'pop_back':
        arr.pop()
    elif command[0] == 'get':
        e = int(command[1])
        if 1 <= e <= len(arr):
            print(arr[e - 1])
        else:
            print("Index out of range")
    elif command[0] == 'size':
        print(len(arr))