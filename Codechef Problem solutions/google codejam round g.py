for t in range(int(input())):
	n = int(input())
	a = []
	cnt = 0
	a = list(map(int,input().split()[:n]))
	for i in range(0,n):
		for j in range(i+1,n):
			for k in range(j+1,n):
				if a[i] == a[j] * a[k] or a[j] == a[i] * a[k] or a[k] == a[j] * a[i]:
					cnt+=1


	print("Case #{}: {}".format(t+1, cnt))
