a="""def KNN(class1,class2,x_new):\n
  dist1 = np.sum((np.transpose(x_new)-class1)**2,axis=1)  \n
  dist2 = np.sum((np.transpose(x_new)-class2)**2,axis=1)\n
  dist1 = np.append([dist1],np.ones((1,5)),axis=0)\n
  dist2 = np.append([dist2],2*np.ones((1,5)),axis=0)\n
  dist  = np.concatenate((dist1, dist2), axis=1)\n
  ii = np.argsort(dist[0])\n
  dist = dist[:,ii]\n
  if np.sum(dist[1][0:3])<=4:\n
    return 1\n
  else:\n
    return 2\n
\n
# validate space\n
#ensure the student code runs without an error\n
try:\n
  knn(class1,class2,x_new)\n
except Exception as e:\n
  print(e)\n
  exit()\n
\n"""
a.split("\n\n")
print("\n".join(a.split("\n\n")))