class Animal:
	def __init__(self, L, ear):
		self.Legs = L
		self.ear = ear
	def walk(self):
		print("Animal walks with", self.Legs, "legs")
	def ears(self):
		print("Animal hears with", self.ear, "ears")
class Bird(Animal):
	def __init__(self, L, W):
		super.__init__(self, L, 2)
		self.Wings = W
	def fly(self):
		print("Bird flies")

A = Animal(6, 2)
B = Bird(5, 2)

A.walk()
A.ears()
B.walk()
B.ears()
B.fly()