def friendshipCircle(AList):
	group = []
	visited = []
	names = list(AList.keys())
	yetToVisit = [names[0]]
	for i in names:
		if len(AList[i]) < 2:
			del AList[i]

	for i in AList.keys():
		if i not in visited:
			tempGrp = []
			# if i in yetToVisit:
			# 	tempGrp.append(i)
			# 	yetToVisit.extend(AList[i])
			tempGrp.append(i)
			tempGrp.extend(AList[i])
			yetToVisit = AList[i]
			for i in yetToVisit:
				if i not in visited:
					# print(type(yetToVisit))
					# print(type(tempGrp))
					tempGrp = tempGrp+AList[i]
					yetToVisit.extend(AList[i])
					visited.append(i)
			group.append(list(set(tempGrp)))


	return group




AList = {
	'B' : ['H','Sh','Su'],
	'H' : ['B','Sa'],
	'Sa': ['H', 'Sh'],
	'Sh': ['Sa', 'B', 'Su'],
	'Su': ['Sh', 'B']
}

print(friendshipCircle(AList))