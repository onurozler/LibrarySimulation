import datetime

class Time():

	# constructor
	def __init__(self,startTime):
		self.__startTime = startTime

	# Change env time to real time
	def changeToClock(self,envTime):
		newTime = self.__startTime + datetime.timedelta(days=envTime)
		return newTime.strftime("%Y/%m/%d")
