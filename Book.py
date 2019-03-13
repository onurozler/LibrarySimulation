import simpy

class Book():

	# constructor
	def __init__(self,env,title,subject,amount,resource):
		self.env = env
		self.title = title
		self.subject = subject
		self.amount = amount
		resource = simpy.PriorityResource(env, capacity=amount)
		

    # getter & setter
	def getTitle(self):
		return self.title
	def getSubject(self):
		return self.subject		
	def getAmount(self):
		return self.amount
	def getResource(self):
		return self.resource


	def setTitle(self,title):
		self.title = title
	def setSubject(self,subject):
		self.subject = subject	
	def setAmount(self,amount):
		self.amount = amount
	def setResource(self,resource):
		self.resource = resource	