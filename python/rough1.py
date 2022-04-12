def tuplesort(L,ind):
	L_ = [i for i in L]
	L_.sort(key=lambda arr : arr[ind])
	return L_

a = ((0,2,2),(1,3,7),(2,5,6),(3,1,5),(4,10,1))

# print(tuplesort(a,2))

def vol(arr):
	# print(arr)
	return 3.14 * (arr[1]/2)**2 * arr[2]

def tallTower(L):
	L_ = list(L)
	L_.sort(key=lambda arr : arr[1],reverse=True)
	pre = L_[0]
	print(L_)
	# print([vol(i) for i in L_])
	i=1
	while i < len(L_):
		print(i)
		print(L_)
		print([vol(i) for i in L_])
		if (vol(L_[i]) >= vol(pre)/2):
			print("if")
			L_.pop(i)
		elif(L_[i][1] > pre[1]):
			print("elif")
			L_.pop(i)
		else:
			print("else")
			pre = L_[i]
			i += 1
	height = 0
	print(L_)
	print([vol(i) for i in L_])
	for i in L_:
		height+=i[2]
	return height

print(tallTower(a))
