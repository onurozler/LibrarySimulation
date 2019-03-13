import simpy

class Book():

	# constructor
	def __init__(self,env,title,amount):
		self.env = env
		self.title = title
		self.amount = amount
		self.resource = simpy.PriorityResource(env, capacity=amount)
		

    # getter & setter
	def getTitle(self):
		return self.title	
	def getAmount(self):
		return self.amount
	def getResource(self):
		return self.resource


	def setTitle(self,title):
		self.title = title
	def setAmount(self,amount):
		self.amount = amount
	def setResource(self,resource):
		self.resource = resource	