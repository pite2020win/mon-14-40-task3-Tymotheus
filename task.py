# Class diary
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
#
# Please, use your imagination and create more functionalities.
# Your project should be able to handle entire school(s?).
# If you have enough courage and time, try storing (reading/writing)
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface (might be text-like).
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#
#When you are done upload this code to your github repository. 
#
#Delete these comments before commit!
#Good luck.
class Student:
  def __init__(self, name, grades):
    self.name = name
    self.grades = grades
  
  def get_average(self):
    return sum(self.grades) / len(self.grades)

  def __str__(self):
    return self.name

class Class:
  def __init__(self, name, students):
    self.name = name
    self.students = students

  def class_average(self):
    if len(self.students) == 0:
      print("No students in a class")
    else:
      return map(lambda stud: stud.get_average(), self.students )
  
  def print_students(self):
      for i in range(len(self.students)):
        print("{}. {}".format(i+1,self.students[i]))


class School:
  classes = []
  def __init__(self, name, classes=[]):
    self.name = name
    self.classes = [classes]
  
  def total_average(self):
    sum_of_averages = 0
    number_of_students = 0
    for c in self.classes:
      for student in c.students:
        sum_of_averages += student.get_average()
        number_of_students +=1
    return sum_of_averages/number_of_students
        

def main():
  print("That's a class diary")
  students = []
  students.append(Student("Johnny Mnemonic", [4.0, 5.0, 4.5]))
  students.append(Student("Paul Atreides", [5.0, 5.0, 5.0]))
  students.append(Student("Samuel L. Jackson", [4.0, 4.0, 4.5]))
  class1 = Class("1A", students)
  class1.print_students()
  school1 = School(["Monster High"], class1)
  print("Shool average: {}".format(school1.total_average()))


#if __name__ == "main":
#with above line code was not running
main()
