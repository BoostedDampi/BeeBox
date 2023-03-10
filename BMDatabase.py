import pymongo


class BeeBase:

	def __init__(self, ip_name):
		print("Init BeeBase...")
		self.dbclient = pymongo.MongoClient("mongodb://localhost:27017/")
		self.dblist = self.dbclient.list_database_names()
		if ip_name not in self.dblist:
			print(f"No database with name {ip_name} found, creating new one...")
		self.data = self.dbclient[ip_name]['weight']

	def addEntry(self, date, time, weight):
		entry = {
			"date": date,
			"time": time,
			"weight": weight
		}
		self.data.insert_one(entry)
		print("Item added")

	def printContent(self):
		print("-"*10)
		for a in self.data.find():
			print(a)
		print("-"*10)

	def printBases(self):
			print("-"*10)
			for a in self.dbclient.list_database_names():
				print(a)
			print("-"*10)



if __name__ == "__main__":
	lol = BeeBase("19216811")
	lol.printBases()
	lol.addEntry("2022-3-10", "12:11" ,19.9)
	lol.printBases()
	lol.printContent()
	print("finished")