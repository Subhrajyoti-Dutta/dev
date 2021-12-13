import psycopg2 as sql

with sql.connect(user = 'postgres', host = "localhost", port = "5432", password = '', database = "flis") as mydb:
	mycursor = mydb.cursor()
	mycursor.execute("SELECT * FROM teams")
	help(mycursor)