import simpy
from Student import Student
from Book import Book

def main():
	env = simpy.Environment()
	StudentTest = Student(env,'onur','ctis',1)
	print(StudentTest.getName())

if __name__ == "__main__":
    main()