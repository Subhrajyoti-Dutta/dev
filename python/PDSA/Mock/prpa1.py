def maxValueSelection(items, c):
	total_value = 0
	for i in sorted(items, key=lambda x:items[x][1]/items[x][0],reverse=True):
		print(i, items[i])


maxValueSelection({1:(10,60), 2:(20,100), 3:(30,120)}, 50)