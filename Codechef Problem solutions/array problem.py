for _ in  range(int(input())):
	n = int(input())
	a = list(map(int,input().split()))
	j = sum(a)
	for x in range(n):
		print(j-a[x],end=" ")
	print()
