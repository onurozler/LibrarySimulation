import simpy
import os
import yaml
import random
import datetime
from itertools import cycle
from Student import Student
from Book import Book
from Time import Time

#Get settings data from Settings.yml
configYamlPath = os.path.join(os.path.dirname(__file__),"Settings.yml")
with open(configYamlPath, "r") as configYaml:
	settingsConfig = yaml.load(configYaml)

libraryInfo = settingsConfig["library"]
bookInfo = libraryInfo["book"]
studentInfo = settingsConfig["student"]

# Student & Book list to keep datas
studentList = []
bookList = []
def setupStudents(env):
	#Setup Students
	names = studentInfo["studentName"]
	surnames = studentInfo["studentSurname"]
	
	#Pairing name&surname lists and randomizing the pairs
	randomNames = list(zip(names, cycle(surnames))) if len(names) > len(surnames) else list(zip(cycle(names), surnames))
	random.shuffle(randomNames)
	
	#Adding Students to student list with their membership
	for randomName in randomNames:
		student = Student(env," ".join(randomName),libraryInfo["membershipOptions"][random.randint(0, 1)])
		studentList.append(student)

def setupLibrary(env):
	#Setup Library
	print('\n======= Welcome to %s. Library is open till %s =======' % (libraryInfo["name"], libraryInfo["closeHour"]))
	
	#Adding books to library's booklist
	for title in bookInfo["titles"]:
		book = Book(env,title,random.randint(1, 3))
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
	t = Time(datetime.datetime.now())
	
	# Students come and request Books randomly. They can get books earlier depending on priority of membership.
	studentComeTime = 0
	for student in studentList:
		env.process(student.requestBook(env,random.choice(bookList),studentComeTime,t))
		studentComeTime += random.randint(1,3)
	
	env.run()
	
	print('\n=========================== Library will be closed for a while, Thanks for your patience! ===========================')

if __name__ == "__main__":
    main()
