class Student: 
    def __init__(self, sid, name, dob):
        self.sid = sid
        self.name = name
        self.dob = dob
    def __str__(self): #polymorphism
        return f"{self.sid} | {self.name} | {self.dob}"
class Course:
    def __init__(self, cid, name):
        self.cid = cid
        self.name = name
    def __str__(self):
        return f"{self.cid} | {self.name}"
class Mark:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = []
    def input_students(self):
        n = int(input("Input number of students: "))
        for _ in range(n):
            sid = input("Input student ID: ")
            name = input("Input student name: ")
            dob = input("Input DOB: ")
            self.students.append(Student(sid, name, dob))
    def input_courses(self):
        n = int(input("Input number of courses: "))
        for _ in range(n):
            cid = input("Course ID: ")
            name = input("Course name: ")
            self.courses.append(Course(cid, name))
    def input_marks(self):
        cid = input("Course ID: ")
        found = False 
        for c in self.courses:
            if c.cid == cid:
                found = True
                break
        if not found:
            print("Not found!")
            return 
        print("Enter marks: ")
        for s in self.students:
            mark = float(input(f"{s.name} ({s.sid}): "))
            self.marks.append({"sid": s.sid, "cid": cid, "mark": mark})
    def list_students(self):
        print("Student list: ")
        for s in self.students:
            print(s)
    def list_courses(self):
        print("Course list: ")
        for c in self.courses:
            print(c)
    def show_marks(self):
        cid = input("Enter course ID: ")
        print(f"\n--Marks for course {cid} --")
        found = False
        for m in self.marks:
            if m["cid"] == cid:
                student = None
                for s in self.students:
                    if s.sid == m["sid"]:
                        student = s
                        break
                if student:
                    print(f"{student.name}({student.sid}): {m['mark']}")
                    found = True
        if not found:
            print("(no marks for this course yet)")
    def menu(self):
        while True:
            print("\n===== Student Mark Management =====")
            print("1. Input students")
            print("2. Input courses")
            print("3. Input marks for a course")
            print("4. List students")
            print("5. List courses")
            print("6. Show marks for a course")
            print("0. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                self.input_students()
            elif choice == "2":
                self.input_courses()
            elif choice == "3":
                self.input_marks()
            elif choice == "4":
                self.list_students()
            elif choice == "5":
                self.list_courses()
            elif choice == "6":
                self.show_marks()
            elif choice == "0":
                break
            else:
                print("Invalid")
if __name__ == "__main__":
    Mark().menu()               
        