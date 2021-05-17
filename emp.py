class emp:
	def __init__(self):
		self.name=""
		self.add=""
		self.age=0
		self.phn=0
		self.email=""
	def read(self):
		self.name=input("enter name:")
		self.add=input("enter adrs:")
		self.age=int(input("enter age:"))
		self.phn=int(input("enter phn:"))
		self.email=input("enter email:")
	def print(self):
		print("name:",self.name)
		print("adrs:",self.add)
		print("age:",self.age)
		print("phn:",self.phn)
		print("email:",self.email)
	def edit(self):
		x=input("enter the name to be edit")
		y=int(input("enter the new phn no:"))
		if(x==self.name):
			self.phn=y
		print("name:",self.name)
		print("chaged phn no:",self.phn)
class tempemp(emp):
	def __init__(self):
		super().__init__()
		self.empid=0
		self.sal=0
		self.comm=0
	def read(self):
		super().read()
		self.empid=int(input("enter the empid:"))
		self.sal=int(input("enter the salary:"))
		self.comm=int(input("enter the comm:"))
	def print(self):
		super().print()
		print("empid:",self.empid)
		print("salary:",self.sal)
		print("commission:",self.comm)
class prmntemp(emp):
	def __init__(self):
		super().__init__()
		self.wrkhrs=0
		self.lvsal=0
	def read(self):
		super().read()
		self.wrkhrs=int(input("enter working hrs:"))
		self.lvsal=int(input("enter leav salary:"))
	def print(self):
		super().print()
		print("wrkhrs:",self.wrkhrs)
		print("lvsal:",self.lvsal)
o=tempemp()
o.read()
o.print()
o.edit()