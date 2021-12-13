def findAllPaths(vertices, glist, source, destination, path = list()):
	vertices.remove(source)
	res = []
	path.append(source)
	for i in glist[source]:
		if i == destination:
			res.append(path+[i])
		elif i in vertices:
			res.extend(findAllPaths(vertices.copy(), glist, i, destination, path = path.copy()))
	return res
	
	
#Vertices are expected to be labelled as single letter or single digit 

#Sort and arrange the result for uniformity
def ArrangeResult(result):
  res = []
  for item in result:
    s = ""
    for i in item:
      s += str(i)    
    res.append(s)
  res.sort() 
  return res

v= ['1', '2', '3', '4', '5', '6', '7']
Alist = {
	'1': ['3', '4'], 
	'2': ['3'], 
	'3': ['6'], 
	'4': ['6', '7'], 
	'5': ['4', '6'], 
	'6': ['2'], 
	'7': ['5']
	}
source = '1'
dest ='2'
print(ArrangeResult(findAllPaths(v, Alist, source, dest)))