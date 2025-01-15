#Question2: Create a "School" class in Python. This class should have the following features and functionality:

#Features:
#"name"
#"foundation_year"
#"students"
#"teachers"

#Methods:
#add_new_student(self, student_name, class): A method used to add a new student to the school. It takes the student's name and class and adds it to the "students" list.
#add_new_teacher(self, teacher_name, branch): A method used to add a new teacher to the school. It takes the teacher's name and major and adds it to the "teachers" dictionary.
#view_student_list(self): A method used to display the list of students enrolled in the school. List student names and classes.
#view_teacher_list(self): A method used to display the list of teachers working in the school. List teacher names and majors.

class School():
    
    def __init__(self, name, foundation_year, students, teachers):
        self.name=name
        self.foundation_year=foundation_year
        self.students=students
        self.teachers=teachers

    def add_new_student(self,student_name,student_class):
        new_student = {"name": student_name, "class": student_class}
        self.students.append(new_student)
        print(f"New student {student_name} added to class {student_class}.")

    def add_new_teacher(self,teacher_name,branch):
        self.teachers[teacher_name] = branch
        print(f"New teacher {teacher_name} (Branch: {branch}) added.")


    def view_student_list(self):
        if not self.students:
            print("No students enrolled in the school yet.")
            return
        print("List of students:")
        for student in self.students:
            print(f"Name: {student['name']}, Class: {student['class']}")

    def view_teacher_list(self):
        if not self.teachers:
            print("No teachers working in the school yet.")
            return
        print("List of teachers:")
        for name, branch in self.teachers.items():
            print(f"Name: {name}, Branch: {branch}")


school = School("Anadolu Ogretmen Lisesi", 2000, [], {})

school.add_new_student("Melike Demiray", "9-B")
school.add_new_student("Elif Sahin"," 9-A")

school.add_new_teacher("Nilufer Aydogan", "Edebiyat")
school.add_new_teacher("Turan Sariemir", "Matematik")

school.view_student_list()
school.view_teacher_list()





    


