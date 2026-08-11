arr=list(map(int,input().split()))
i=0
for j in range(len(arr)):
    if arr[j] % 2==0:
        arr[i]=arr[j]
        i += 1
print(arr[:i])