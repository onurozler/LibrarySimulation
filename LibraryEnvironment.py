import simpy
from Student import Student
from Book import Book

def main():
	env = simpy.Environment()
	s1 = Student(env,'onur','ctis',0)
	s2 = Student(env,'deneme','ctis',0)
	
	b1 = Book(env,'Intro','ctis',1)
	
	p1 = env.process(s1.requestBook(env,b1.getResource(),0))
	p2 = env.process(s2.requestBook(env,b1.getResource(),1))
	env.run()

if __name__ == "__main__":
    main()