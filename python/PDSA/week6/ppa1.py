class MaxHeap():
	def __init__(self,arr,k):
		self.heapArr = arr[:k]
		self.k = k
		self.heapSort()

	def swap(self,a,b):
		self.heapArr[a], self.heapArr[b] = self.heapArr[b], self.heapArr[a]

	def heapify(self,i):
		biggest = i
		if (2*i+1) < self.k and self.heapArr[biggest] < self.heapArr[2*i+1]:
			biggest = 2*i+1
		if (2*i+2) < self.k and self.heapArr[biggest] < self.heapArr[2*i+2]:
			biggest = 2*i+2
		if biggest != i:
			self.swap(i,biggest)
			self.heapify(biggest)
		
	def heapSort(self):
		for i in range(self.k//2,-1,-1):
			self.heapify(i)

	def swapMaxVal(self, ele):
		if ele < self.heapArr[0]:
			self.heapArr[0] = ele
			self.heapify(0)

	def printHeap(self):
		i=0
		l = 0
		while i < self.k:
			print(self.heapArr[i],end=' ')
			if 2**(l+1) - 2 == i:
				print()
				l+=1
			i+=1


arr = [70, 68, 25, 41, 15, 1, 25, 18, 14, 57, 64, 12, 54, 38, 88, 1, 60, 38, 27, 29, 80, 92, 17, 17, 15]
k=10
heap = MaxHeap(arr,k)
for i in range(k,len(arr)):
	heap.swapMaxVal(arr[i])
heap.printHeap()