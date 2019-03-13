import simpy

class Student():
	# constructor
	def __init__(self,env,name,membership):
		self.env = env
		self.name = name
		self.membership = membership
		if(membership == -1):
			self.membershipName = 'Gold Membership'
		else:
			self.membershipName = 'Normal Membership'

    # getter & setter
	def getName(self):
		return self.name	
	def getMembership(self):
		return self.membership

	def setName(self,name):
		self.name = name
	def setMembership(self,membership):
		self.membership = membership
		
	
	# Functions
	def requestBook(self,env,book,wait):
		yield env.timeout(wait)
		resource = book.getResource()
		
		with resource.request(priority=self.membership) as req:
			print('%s requesting %s Book at %s with %s' % (self.name, book.getTitle(),env.now, self.membershipName))
			yield req
			print('%s has borrowed book at %s' % (self.name, env.now))
			yield env.timeout(3)
			print('%s gave book at %s' % (self.name, env.now))
	
	