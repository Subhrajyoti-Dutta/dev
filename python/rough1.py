T = int(input())
for t in range(T):
    if t != 0:
        print()
    D,N,K = (map(int,input().split(" ")))
    vals = [[0]*K for _ in range(D)]
    # print(vals)
    events = []
    for j in range(N):
        events.append(list(map(int,input().split(" "))))
    # events.sort()
    # print(events)
    # print(len(vals))
    for h,s,e in events:
        # print(h,s,e)
        for k in range(s-1,e):
            vals[k].append(h)
            vals[k].sort()
            vals[k].pop(0)
        # print(vals)
    for i in range(len(vals)):
        vals[i].sort()
        try:
            vals[i] = sum(vals[i][-K:])
        except:
            vals[i] = sum(vals[i])
    print("Case #",t+1,": ",sorted(vals)[-1],sep="",end="")
    del D, N, K, vals, events, h, s, e