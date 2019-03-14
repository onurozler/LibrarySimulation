

class Time():

	# constructor
	def __init__(self,year,month,day,hour,minute,second):
		self.__year = year
		self.__month = month
		self.__day = day
		self.__hour = hour
		self.__minute = minute
		self.__second = second

	# Change env time to real time
	def changeToClock(self,envTime):
	
		year = self.__year
		month = self.__month
		day = self.__day
		hour = self.__hour
		minute = self.__minute
		second = self.__second
		
		day +=int((envTime + minute)%60)

		if month == 4 or month == 6 or month == 9 or month == 11:
			month += int(day / 31)
			day = ((day - 1) % 30) + 1
		elif month == 2:
			if (year % 4 == 0):
				month += int(day / 30)
				day = ((day - 1) % 29) + 1
			else:
				month += int(day / 29)
				day = ((day - 1) % 28) + 1
		else:
			month += int(day / 32)
			day = ((day - 1) % 31) + 1

		year += int(month / 13)
		month = ((month - 1) % 12) + 1

		newTime = "%s/%s/%s"%(
		year, str(month).rjust(2, "0"), str(day).rjust(2, "0"))
		return newTime
