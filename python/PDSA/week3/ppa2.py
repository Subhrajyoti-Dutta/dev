class Hashing:
  def __init__(self,c1,c2,m):
    self.hashtable = []
    for i in range(m):
      self.hashtable.append(None)     
    self.c1 = c1
    self.c2 = c2
    self.m = m
  def store_data(self,data):
    h = lambda k, i: ((k%self.m) + self.c1*i + self.c2*i**2)%self.m
    flag = False
    for i in range(self.m):
      if self.hashtable[h(data,i)] is None:
        self.hashtable[h(data,i)] = data
        flag = True
        break
    else:
      if flag is False:
        print('Hash table is full')
  def display_hashtable(self):
    return (self.hashtable)
c1 = int(input())
c2 = int(input())
m = int(input())
data=eval(input())
A = Hashing(c1,c2,m)
for i in data:
  A.store_data(i)
print(A.display_hashtable())