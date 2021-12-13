import pandas as pd

class Beautify():
	def __init__(self, mycursor):
		self.mycursor = mycursor
		self.db = pd.DataFrame(data = mycursor.fetchall(), columns = [i.name for i in mycursor.description])

	def pprint(self, *col):
		if col == ("all",) or col == ("*",) or col == tuple():
			print(self.db)
		else:
			print(pd.DataFrame(self.db[list(col)]))