n = int(input())
arr = list(map(int, input().split()))

def insertion_sort():
  size = len(arr)
  for i in range(1,size):
    j = i - 1 
    key = arr[i]
    while (j >= 0 and arr[j] > key):
      arr[j + 1] = arr[j]
      j = j-1
    arr[j + 1] = key
  return arr

insertion_sort()

for i in arr:
  print(i,end=" ")