import simpy
import yaml
import random
import datetime
from Student import Student
from Book import Book
from Time import Time

configYaml = open("Settings.yml", "r")
settingsConfig = yaml.load(configYaml)
configYaml.close()

libraryInfo = settingsConfig["library"]
bookInfo = libraryInfo["book"]
studentInfo = settingsConfig["student"]

studentList = []
bookList = []
def setupStudents(env):
	stuLen = len(studentInfo["studentName"])
	surNamelen = len(studentInfo["studentSurname"])
	for i in range(stuLen*2):
		randomName = studentInfo["studentName"][random.randint(0, stuLen-1)] + ' ' +  studentInfo["studentSurname"][random.randint(0, surNamelen-1)]
		student = Student(env,randomName,libraryInfo["membershipOptions"][random.randint(0, 1)])
		studentList.append(student)

def setupLibrary(env):
	print('Welcome to %s. Library is open till %s.' % (libraryInfo["name"], libraryInfo["closeHour"]))
	
	#Adding books to library's booklist
	for i in range(len(bookInfo["titles"])):
		book = Book(env,bookInfo["titles"][i],i+1)
		bookList.append(book)
		
	print('\nLibrary Books: \nTitle\t\t\tAmount\n==============================')
	for book in bookList:
		print('%s\t\t%s' %(book.getTitle(),book.getAmount()))
		
	print('=======================================================================================')
		

def main():
	env = simpy.Environment()
	setupLibrary(env)
	setupStudents(env)
	
	now = datetime.datetime.now()
	t = Time(now.year,now.month,now.day,now.hour,now.minute,now.second)
	
	
	for student in studentList:
		env.process(student.requestBook(env,bookList[random.randint(0, len(bookList)-1)],0,t))
	
	env.run()

if __name__ == "__main__":
    main()