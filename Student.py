import simpy

class Student():

	# constructor
	def __init__(self,env,name,department,membership):
		self.env = env
		self.name = name
		self.department = department
		self.membership = membership

    # getter & setter
	def getName(self):
		return self.name
	def getDepartment(self):
		return self.department		
	def getMembership(self):
		return self.membership

	def setName(self,name):
		self.name = name
	def setDepartment(self,department):
		self.department = department	
	def setMembership(self,membership):
		self.membership = membership
		
	
	# Functions
	def requestBook(self,env,resource,wait):
		yield env.timeout(wait)
		with resource.request(priority=self.membership) as req:
			print('%s requesting book at %s with Membership = %s' % (self.name, env.now, self.membership))
			yield req
			print('%s has borrowed book at %s' % (self.name, env.now))
			yield env.timeout(3)
			print('%s gave book at %s' % (self.name, env.now))
	
	