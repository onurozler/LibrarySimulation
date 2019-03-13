import simpy
import yaml
import random
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
	for i in range(studentInfo["studentSize"]):
		randomName = studentInfo["studentName"][random.randint(0, 9)] + ' ' +  studentInfo["studentSurname"][random.randint(0, 9)]
		student = Student(env,randomName,libraryInfo["membershipOptions"][random.randint(0, 1)])
		studentList.append(student)

def setupLibrary(env):
	print('Welcome to %s. Library is open till %s.' % (libraryInfo["name"], libraryInfo["closeHour"]))
	
	#Adding books to library's booklist
	for i in range(bookInfo["bookSize"]):
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
	
	print(studentList[0].getMembership())
	
	for student in studentList:
		env.process(student.requestBook(env,bookList[random.randint(0, 9)],0))
	
	env.run()

if __name__ == "__main__":
    main()