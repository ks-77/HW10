"""
HW 10
Savchenko Kirill
"""


import re
from colorama import init
init(autoreset=True)


class Person:
    __fullname = "Unknown"
    __age = "Unknown"
    __gender = "Unknown"
    __hobby = "No hobby"

    def __init__(self, fullname, age, gender, hobby):
        self.fullname = fullname
        self.age = age
        self.gender = gender
        self.hobby = hobby

    @property
    def fullname(self):
        return self.__fullname

    @fullname.setter
    def fullname(self, fullname):
        if re.match(r'^[A-Za-z]{2,20}\s[A-Za-z]{2,20}\s[A-Za-z]{2,20}$', fullname):
            self.__fullname = fullname
        else:
            print("Incorrect fullname length!")

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if 16 <= age <= 100:
            self.__age = age
        else:
            print("Incorrect age!")

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, gender):
        if gender == "Male" or gender == "Female":
            self.__gender = gender
        else:
            print("Incorrect gender!")

    @property
    def hobby(self):
        return self.__hobby

    @hobby.setter
    def hobby(self, hobby):
        if 2 <= len(hobby) <= 1000:
            self.__hobby = hobby
        else:
            print("Incorrect hobby length!")

    def show_info(self):
        print(
            f"Name: {self.fullname}, Age: {self.age}, Gender: {self.gender}, Hobby: {self.hobby}")


class Student(Person):
    __course = "Unknown"
    __faculty = "Unknown"

    def __init__(self, fullname, age, gender, hobby, course, faculty):
        super().__init__(fullname, age, gender, hobby)
        self.course = course
        self.faculty = faculty

    @staticmethod
    def add_student(intrant):
        with open("Student_list.txt", "a") as student:
            student.write(f"Student name: {intrant.fullname}\n")
            student.write(f"Student age: {intrant.age}\n")
            student.write(f"Student gender: {intrant.gender}\n")
            student.write(f"Student hobby: {intrant.hobby}\n")
            student.write(f"Student course: {intrant.course}\n")
            student.write(f"Student faculty: {intrant.faculty}\n\n")
        if intrant.faculty == "It":
            with open("It_s_list", "a") as itlist:
                itlist.write(f"Student name: {intrant.fullname}\n")
                itlist.write(f"Student age: {intrant.age}\n")
                itlist.write(f"Student gender: {intrant.gender}\n")
                itlist.write(f"Student hobby: {intrant.hobby}\n")
                itlist.write(f"Student course: {intrant.course}\n")
                itlist.write(f"Student faculty: {intrant.faculty}\n\n")
        elif intrant.faculty == "Law":
            with open("Law_s_list", "a") as lawlist:
                lawlist.write(f"Student name: {intrant.fullname}\n")
                lawlist.write(f"Student age: {intrant.age}\n")
                lawlist.write(f"Student gender: {intrant.gender}\n")
                lawlist.write(f"Student hobby: {intrant.hobby}\n")
                lawlist.write(f"Student course: {intrant.course}\n")
                lawlist.write(f"Student faculty: {intrant.faculty}\n\n")
        elif intrant.faculty == "Medicine":
            with open("Medicine_s_list", "a") as medlist:
                medlist.write(f"Student name: {intrant.fullname}\n")
                medlist.write(f"Student age: {intrant.age}\n")
                medlist.write(f"Student gender: {intrant.gender}\n")
                medlist.write(f"Student hobby: {intrant.hobby}\n")
                medlist.write(f"Student course: {intrant.course}\n")
                medlist.write(f"Student faculty: {intrant.faculty}\n\n")
        else:
            print("Incorrect faculty!")

    @property
    def course(self):
        return self.__course

    @course.setter
    def course(self, course):
        if 1 <= course <= 6:
            self.__course = course
        else:
            print("Incorrect course!")

    @property
    def faculty(self):
        return self.__faculty

    @faculty.setter
    def faculty(self, faculty):
        if faculty in all_faculties:
            self.__faculty = faculty
        else:
            print("Incorrect faculty!")


class Teacher(Person):
    __subject_of_teaching = "Unknown"
    __education = "Unknown"

    def __init__(self, fullname, age, gender, hobby, subject_of_teaching, education):
        super().__init__(fullname, age, gender, hobby)
        self.subject_of_teaching = subject_of_teaching
        self.education = education

    def show_info(self):
        print(
            f"\nName: {self.fullname}\nAge: {self.age}\nGender: {self.gender}\nHobby: {self.hobby}\n"
            f"Subject of teaching: {self.subject_of_teaching}\nEducation: {self.education}")

    @property
    def subject_of_teaching(self):
        return self.__subject_of_teaching

    @subject_of_teaching.setter
    def subject_of_teaching(self, subject_of_teaching):
        if 2 <= len(subject_of_teaching) <= 100:
            self.__subject_of_teaching = subject_of_teaching
        else:
            print("Incorrect subject of teaching!")

    @property
    def education(self):
        return self.__education

    @education.setter
    def education(self, education):
        if 2 <= len(education) <= 100:
            self.__education = education
        else:
            print("Incorrect place of education!")


class Academy:
    name = "Ukrainian National Academy"


class Faculty:
    __name = "Not specified"

    def __init__(self, name, dean, subjects, bachelor, master):
        self.name = name
        self.dean = dean
        self.subjects = subjects
        self.bachelor = bachelor
        self.master = master

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if 1 <= len(name) <= 100:
            self.__name = name
        else:
            print("Incorrect faculty name!")

    def showinfo(self):
        print(f"\nFaculty name: {self.name}\nDean: {self.dean}\nSubjects: {self.subjects}\nYears of studying:"
              f"\n\tBachelor's degree: {self.bachelor} years\n\tMaster's degree: {self.master} years")


class Subjects:
    __name = "Not specified"

    def __init__(self, name, teacher):
        self.__name = name
        self.teacher = teacher

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if name in subjects_it or subjects_law or subjects_medicine:
            self.__name = name
        else:
            print("Incorrect subject name!")

    def showinfo(self):
        print(f"Subjects name: {", ".join(self.name)}\nTeacher: {self.teacher}\n")


subjects_it = ["Computer science", "Programming", "Design", "WebDev", "Math"]
subjects_law = ["Law", "Politics", "History", "Constitutional law", "Administrative law"]
subjects_medicine = ["Medicine", "Pharmacy", "Dentistry", "Anatomy", "Chemistry"]

it_fac_inf = Faculty(name="It", dean="Gontar Tomara Ivanovna", subjects=subjects_it, bachelor=4, master=1)
law_fac_inf = Faculty(name="Law", dean="Ivanov Igor Dmitrievich", subjects=subjects_law, bachelor=4, master=1.5)
med_fac_inf = Faculty(name="Medicine", dean="Gorenko Adam Rahitenko", subjects=subjects_medicine, bachelor=5, master=2)
all_faculties = it_fac_inf, law_fac_inf, med_fac_inf


Tamara = Teacher(fullname="Gontar Tomara Ivanovna", age=35, gender="Female", hobby="singing",
                 subject_of_teaching=subjects_it, education="ONPU")
Igor = Teacher(fullname="Ivanov Igor Dmitrievich", age=37, gender="Male", hobby="sport shooting",
               subject_of_teaching=subjects_law, education="ONLA")
Adam = Teacher(fullname="Gorenko Adam Rahitenko", age=48, gender="Male", hobby="research",
               subject_of_teaching=subjects_medicine, education="ONMEDU")
all_teachers = Tamara, Igor, Adam


it_sub_inf = Subjects(name=subjects_it, teacher=Tamara.fullname)
law_sub_inf = Subjects(name=subjects_law, teacher=Igor.fullname)
med_sub_inf = Subjects(name=subjects_medicine, teacher=Adam.fullname)
all_subjects = it_sub_inf, law_sub_inf, med_sub_inf


def academy_structure():
    print(f"\nWelcome to the {Academy.name}!\n\nYou can:\n1. Add new student\n2. Get information about students\n"
          f"3. Get information about teachers\n4. Get information about faculties\n5. Get information about subjects")
    try:
        choice = int(input("Enter your choice (1-5): "))

        if choice == 1:
            intrant = Student(fullname=input("Enter student's fullname: "),
                              age=int(input("Enter student's age: ")),
                              gender=input("Enter student's gender: "),
                              hobby=input("Enter student's hobby: "),
                              course=int(input("Enter student's course: ")),
                              faculty=input("Enter student's faculty: "))
            intrant.add_student(intrant)
            print('\033[32;1m'"Student added to the list")
        elif choice == 2:
            print("\nStudents of which faculty you want to see?\n1. All students\n2. It\n3. Law\n4. Medicine")
            choice = int(input("\nEnter your choice (1-4): "))
            if choice == 1:
                with open("Student_list.txt", "r") as student:
                    print(student.read())
            elif choice == 2:
                with open("It_s_list.txt", "r") as itlist:
                    print(itlist.read())
            elif choice == 3:
                with open("Law_s_list.txt", "r") as lawlist:
                    print(lawlist.read())
            elif choice == 4:
                with open("Medicine_s_list.txt", "r") as medlist:
                    print(medlist.read())
            else:
                print('\033[31;1m'"\nIncorrect choice!\nYou can choose 1-4 only")
        elif choice == 3:
            for teacher in all_teachers:
                teacher.show_info()
        elif choice == 4:
            print("\nInformation of which faculty you want to see?\n1. All faculties\n2. It\n3. Law\n4. Medicine")
            choice = int(input("\nEnter your choice (1-4): "))
            if choice == 1:
                for faculty in all_faculties:
                    faculty.showinfo()
            elif choice == 2:
                it_fac_inf.showinfo()
            elif choice == 3:
                law_fac_inf.showinfo()
            elif choice == 4:
                med_fac_inf.showinfo()
            else:
                print('\033[31;1m'"\nIncorrect choice!\nYou can choose 1-4 only")
        elif choice == 5:
            print("Info about subjects of which faculty you want to see?\n1. All subjects\n2. It\n3. Law\n4. Medicine")
            choice = int(input("\nEnter your choice (1-4): "))
            if choice == 1:
                for subject in all_subjects:
                    subject.showinfo()
            elif choice == 2:
                it_sub_inf.showinfo()
            elif choice == 3:
                law_sub_inf.showinfo()
            elif choice == 4:
                med_sub_inf.showinfo()
            else:
                print('\033[31;1m'"\nIncorrect choice!\nYou can choose 1-4 only")
        else:
            print('\033[31;1m'"\nIncorrect choice!\nYou can choose 1-5 only")
    except Exception as e:
        print('\033[31;1m'f"Error: {e}")


academy_structure()
