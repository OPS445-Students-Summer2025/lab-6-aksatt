#!/usr/bin/env python3
# Author ID: aksatt

class Student:
    # Define the name and number 
    def __init__(self, name, number):
        self.name = name
        self.number = str(number)
        self.courses = {}

    # Return student namde and number
    def displayStudent(self):
        return f"Student Name: {self.name}\nStudent Number: {self.number}"

    # Add a course and grade to the student's record
    def addGrade(self, course, grade):
        self.courses[course] = grade

    # Calculate the GPA
    def displayGPA(self):
        if not self.courses:
            return f"GPA of student {self.name} is 0.0"
        total = sum(self.courses.values())
        gpa = total / len(self.courses)
        return f"GPA of student {self.name} is {gpa}"

    # Return a list of courses that the student has passed
    # A course is considered passed if the grade is greater than 0.0
    def displayCourses(self):
        passed = []
        for course, grade in self.courses.items():
            if grade > 0.0:
                passed.append(course)
        return passed

if __name__ == '__main__':
    # Create first student and add courses and grades
    student1 = Student('John', '013454900')
    student1.addGrade('uli101', 1.0)
    student1.addGrade('ops245', 2.0)
    student1.addGrade('ops445', 3.0)

    # Create second student and add courses and grades
    student2 = Student('Jessica', 123456)
    student2.addGrade('ipc144', 4.0)
    student2.addGrade('cpp244', 3.5)
    student2.addGrade('cpp344', 0.0)
    
    # Diplay the student1 information, GPA, and courses
    print(student1.displayStudent())
    print(student1.displayGPA())
    print(student1.displayCourses())

    # Display the student2 information, GPA, and courses
    print(student2.displayStudent())
    print(student2.displayGPA())
    print(student2.displayCourses())
