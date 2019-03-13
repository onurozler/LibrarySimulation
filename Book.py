import simpy

class Book():

	# constructor
	def __init__(self,env,title,amount):
		self.__env = env
		self.__title = title
		self.__amount = amount
		self.__resource = simpy.PriorityResource(env, capacity=amount)
		

    # getter & setter
	def getTitle(self):
		return self.__title	
	def getAmount(self):
		return self.__amount
	def getResource(self):
		return self.__resource


	def setTitle(self,title):
		self.__title = title
	def setAmount(self,amount):
		self.__amount = amount
	def setResource(self,resource):
		self.__resource = resource	