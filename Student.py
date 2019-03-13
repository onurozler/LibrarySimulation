import simpy

class Student():
	# constructor
	def __init__(self,env,name,membership):
		self.__env = env
		self.__name = name
		self.__membership = membership
		if(self.__membership == -1):
			self.__membershipName = 'Gold Membership'
		else:
			self.__membershipName = 'Normal Membership'

    # getter & setter
	def getName(self):
		return self.__name	
	def getMembership(self):
		return self.__membership

	def setName(self,name):
		self.__name = name
	def setMembership(self,membership):
		self.__membership = membership
		
	
	# Functions
	def requestBook(self,env,book,wait,time):
		yield env.timeout(wait)
		resource = book.getResource()
		
		with resource.request(priority=self.__membership) as req:
			print('%s requesting %s Book at %s with %s' % (self.__name, book.getTitle(),env.now, self.__membershipName))
			yield req
			print('%s has borrowed book at %s' % (self.__name, time.changeToClock(env.now)))
			yield env.timeout(3)
			print('%s gave book at %s' % (self.__name, env.now))
	
	