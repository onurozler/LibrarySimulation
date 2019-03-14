import simpy
import yaml
import random
import datetime
from Student import Student
from Book import Book
from Time import Time

#Get settings data from Settings.yml
configYaml = open("Settings.yml", "r")
settingsConfig = yaml.load(configYaml)
configYaml.close()

libraryInfo = settingsConfig["library"]
bookInfo = libraryInfo["book"]
studentInfo = settingsConfig["student"]

# Student & Book list to keep datas
studentList = []
bookList = []
def setupStudents(env):
	#Setup Students
	stuLen = len(studentInfo["studentName"])
	surNamelen = len(studentInfo["studentSurname"])
	
	#Adding Students to student list with their membership by generating random name & surnames
	for i in range(stuLen):
		randomName = studentInfo["studentName"][random.randint(0, stuLen-1)] + ' ' +  studentInfo["studentSurname"][random.randint(0, surNamelen-1)]
		student = Student(env,randomName,libraryInfo["membershipOptions"][random.randint(0, 1)])
		studentList.append(student)

def setupLibrary(env):
	#Setup Library
	print('\n======= Welcome to %s. Library is open till %s =======' % (libraryInfo["name"], libraryInfo["closeHour"]))
	
	#Adding books to library's booklist
	for i in range(len(bookInfo["titles"])):
		book = Book(env,bookInfo["titles"][i],random.randint(1, 3))
		bookList.append(book)
	
	#Give Info about Books
	print('\nLibrary Books: \n\nTitle\t\t\tAmount\n==============================')
	for book in bookList:
		print('%s\t\t%s' %(book.getTitle(),book.getAmount()))
		
	print('\n=======================================================================================\n')
		

def main():
	#One second in Real World = One Env Time
	env = simpy.rt.RealtimeEnvironment(factor=1.0)
	setupLibrary(env)
	setupStudents(env)
	
	# One Env Time = 1 Day in Simulation
	now = datetime.datetime.now()
	t = Time(now.year,now.month,now.day,now.hour,now.minute,now.second)
	
	# Students come and request Books randomly. They can get books earlier depending on priority of membership.
	studentComeTime = random.randint(0,3)
	for student in studentList:
		env.process(student.requestBook(env,bookList[random.randint(0, len(bookList)-1)],studentComeTime,t))
		studentComeTime += random.randint(1,3)
	
	env.run()
	
	print('\n=========================== Library will be closed for a while, Thanks for your patience! ===========================')

if __name__ == "__main__":
    main()