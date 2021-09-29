n = int(input())

for _ in range(n):
    N = int(input())
    arr = map(int,input().split(" "))
    flag = 'yes'
    i = 0
    while i < N - i -1:
        if arr[i] <= arr[i-1] or arr[i] != arr[N-i-1]:
            flag
        pass
    print(max(map(lambda x : a%x, range(1,b+1))))