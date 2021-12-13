class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None
class doubly_linked_list:
  def __init__(self):
    self.head = None
    self.last = None

  def insert_end(self, data):
    if self.last is None:
      self.last = Node(data)
      self.head = self.last
    else:
      self.last.next = Node(data)
      self.last.next.prev = self.last
      self.last = self.last.next

  def delete_end(self):
    if self.last is self.head:
      self.last = None
      self.head = None
    else:
      self.last = self.last.prev
      self.last.next = None

  def traverse(self):
    temp = self.head
    while temp != None:
      if temp.next != None:
        print(temp.data, end=',')
      else:
        print(temp.data)
      temp = temp.next
        
  def traverse_rev(self):
    temp = self.last
    while temp != None:
      if temp.prev != None:
        print(temp.data, end=',')
      else:
        print(temp.data)
      temp = temp.prev

ins = eval(input())
delt = int(input())
A = doubly_linked_list()
for i in ins:
  A.insert_end(i)
for j in range(delt):
  A.delete_end()
A.traverse()
A.traverse_rev() 