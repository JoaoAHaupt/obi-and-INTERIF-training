n = int(input())
arr = [1, 1, 1]
for i in range(n):
    if i > 2:
        arr.append(arr[i-3] + arr[i-2])


print(arr[len(arr)-1])
