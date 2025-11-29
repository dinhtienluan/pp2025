students = []
courses = []
marks = []
def numstudents():
    count = int(input("Input number of students: "))
    for _ in range(count):
        studentinfo()
def studentinfo():
    sid = input("Input student ID: ")
    sname = input("Input student name: ")
    dob = input("Input date of birth: ")
    students.append({"id": sid, "name": sname, "dob": dob})

def numcourses():
    count1 = int(input("Input number of courses: "))
    for _ in range(count1):
        courseinfo()
def courseinfo():
    cid = input("Course ID: ")
    name = input("Course name: ")
    courses.append({"id": cid, "name": name})

def marksforcourse():
    courseid = input("Course ID: ")
    course = None
    for c in courses:
        if c["id"] == courseid:
            course = c
            break
    if not course:
        print("Not found!")
        return
    print("Enter marks: ")
    for s in students:
        m = float(input(f"{s['name']} ({s['id']}): "))
        marks.append({"studentid": s["id"], "course_id": courseid, "mark": m})


def listcourses():
    print("Course List: ")
    for c in courses:
        print(f"{c['id']} | {c['name']}")
def liststudents():
    print("Student List: ")
    for s in students:
        print(f"{s['id']} | {s['name']} | {s['dob']}")
def studentmarks():
    courseid = input("Enter course ID: ")
    print(f"\n-- Marks for course {courseid} --")
    for m in marks:
        if m["course_id"] == courseid:
            student = None
            for s in students:
                if s["id"] == m["student_id"]:
                    student = s
                    break 
            print(f"{student['name']} ({student['id']}): {m['mark']}")

def menu():
    while True:
        print("\n===== Student Mark Management =====")
        print("1. Input number of students & student info")
        print("2. Input number of courses & course info")
        print("3. Select course & input marks")
        print("4. List students")
        print("5. List courses")
        print("6. Show student marks for a course")
        print("0. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            numstudents()
        elif choice == "2":
            numcourses()
        elif choice == "3":
            marksforcourse()
        elif choice == "4":
            liststudents()
        elif choice == "5":
            listcourses()
        elif choice == "6":
            studentmarks()
        elif choice == "0":
            print("Exiting program...")
            break
        else:
            print("Invalid option. Try again.")
menu()


