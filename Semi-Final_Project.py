from abc import ABC, abstractmethod
import json

Program_name = "Computing & Data Sciences"
students = {
    "name": ["Peter", "David", "George", "John", "Sandra", "Katherene"],
    "ID": [76859789, 76845740, 85976468, 90798597, 95357296, 37649377],
    "GPA": [4.0, 3.8, 3.7, 3.3, 3.5, 3.9],
    "CGPA": [4.0, 3.6, 1.666, 1.0, 3.5, 3.8],
    "Grades": [98, 96, 92, 75, 78, 83],
    "level": [3, 3, 3, 2, 4, 4],
}
Courses1 = {
        "Linear Algebra": 3,
        "Introduction to Computer Systems": 3,
        "Introduction to Data Sciences": 3,
        "Programming I": 3,
        "Probability and Statistics I": 3,
        "Data Structures and Algorithms": 3,
        "Discrete Structures": 3,
        "Software Engineering": 3,
        "Distributed Programming": 3,
        }
Courses2 = {
        "Regression Analysis": 3,
        "Introduction to Databases": 3,
        "Cloud Computing": 3,
        "Data Science Methodology": 3,
        "Probability and Statistics II": 3,
        "Data Science Tools and Software": 3,
        "Advanced Calculus": 3,
        "Machine Learning": 3,
        "Data Mining and Analytics": 3,
        }
Courses3 = {
        "Stochastic Processes": 3,
        "Design and Analysis of Experiments": 3,
        "Data Computation and Analysis": 3,
        "Data Science Methodology": 3,
        "Probability and Statistics II": 3,
        "Survey Methodology": 3,
        "Advanced Calculus": 3,
        "Data Visualization Tools": 3,
        "Data Mining and Analytics": 3,
        }
Courses4 = {
        "Big Data Analytics": 3,
        "Simulations": 3,
        "Social Data Analytics": 3,
        "Convex Optimization": 3,
        "Stream Processing": 3,
        "Concurrent Algorithms and Data Structures": 3,
        "Multivariate Statistical Analysis": 3,
        "Project I": 3,
        }

student_courses = {name: {} for name in students["name"]}

current_term_courses = {name: {} for name in students["name"]}

def score_to_grade(score):
    if score >= 90:
        return "A", 4.000
    elif score >= 85:
        return "A-", 3.666
    elif score >= 80:
        return "B+", 3.333
    elif score >= 75:
        return "B", 3.000
    elif score >= 70:
        return "B-", 2.666
    elif score >= 65:
        return "C+", 2.333
    elif score >= 60:
        return "C", 2.000
    elif score >= 56:
        return "C-", 1.666
    elif score >= 53:
        return "D+", 1.333
    elif score >= 50:
        return "D", 1.000
    else:
        return "F", 0.000

def academic_standing(cgpa):
    if cgpa >= 2.00:
        return "Good Standing"
    elif cgpa >= 1.666:
        return "Academic Warning"
    else:
        return "Academic Probation"

class FacultyMember(ABC):
    @abstractmethod
    def display_info(self):
        pass

class Student(FacultyMember):
    def __init__(self, name, student_id, level):
        self.__name = name
        self.__student_id = student_id
        self.__level = level

    def display_info(self):
        print("Name :", self.__name)
        print("ID   :", self.__student_id)
        print("Level:", self.__level)

    def get_name(self):
        return self.__name

    def get_id(self):
        return self.__student_id

    def get_level(self):
        return self.__level

    def set_level(self, level):
        self.__level = level

class Advisor(FacultyMember):
    def __init__(self, name):
        self.name = name

    def display_info(self):
        print("Advisor :", self.name)

student_objects = [
    Student(students["name"][i], students["ID"][i], students["level"][i])
    for i in range(len(students["name"]))
]

advisors = [Advisor("Amr Amin"), Advisor("Mahmoud Gamal")]
program_advisor = advisors[0]

def add_advisor():
    name = input("Advisor Name : ")
    if any(a.name == name for a in advisors):
        print("! Advisor Already Exists !")
        return
    advisors.append(Advisor(name))
    print("Advisor Added Successfully")

def view_advisor():
    if len(advisors) == 0:
        print('No advisors found')
        return
    for advisor in advisors:
        advisor.display_info()

def sync_student_object(index):
    """Keep the Student object's level in sync with the students dict."""
    student_objects[index].set_level(students["level"][index])

def add_student():
    try:
        name = input("Student Name : ")
        if name in students["name"]:
            print("! Student Already Exists !")
            return
        student_id = int(input("Student ID : "))
        if student_id in students["ID"]:
            print("! Student ID Already Exists !")
            return
        level = int(input("Student Level : "))
        if level < 1 or level > 4:
            print("! Level Must Be From 1 To 4 !")
            return
        students["name"].append(name)
        students["ID"].append(student_id)
        students["GPA"].append(0.0)
        students["CGPA"].append(0.0)
        students["Grades"].append(0)
        students["level"].append(level)
        student_courses[name] = {}
        current_term_courses[name] = {}
        student_objects.append(Student(name, student_id, level))
        print("Student Added Successfully")
    except ValueError:
        print("! Invalid Input !")

def load_student():
    while True:
        name = input("Load (or type 'cancel' to go back) : ")
        if name.lower() == "cancel":
            return None
        if name not in students["name"]:
            print("! Invalid Student Name ! , Please Try Again .")
            continue
        index = students["name"].index(name)
        try:
            student_id = int(input("Enter Student ID : "))
            if students["ID"][index] == student_id:
                print("Student Information Loaded")
                return index
            else:
                raise ValueError
        except ValueError:
            print("! Invalid ID ! , Please Try Again .")

def enroll_course(index):
    name = students["name"][index]
    level = students['level'][index]
    print("\nAvailable Courses:")

    if level == 1:
        courses_dict = Courses1
    elif level == 2:
        courses_dict = Courses2
    elif level == 3:
        courses_dict = Courses3
    elif level == 4:
        courses_dict = Courses4
    else:
        print("! Invalid Level !")
        return

    course_list = list(courses_dict.keys())

    for i in range(len(course_list)):
        print(i + 1, ".", course_list[i], "-", courses_dict[course_list[i]], "Credits")

    try:
        choice = int(input("Choose Course : "))
        if choice < 1 or choice > len(course_list):
            print("! Invalid Course !")
            return
        course = course_list[choice - 1]
        if course in student_courses[name]:
            print("! Student Is Already Enrolled In This Course !")
            return
        score = float(input("Enter Score (0-100) : "))
        if score < 0 or score > 100:
            print("! Score Must Be Between 0 And 100 !")
            return
        letter, points = score_to_grade(score)
        course_record = {
            "score": score,
            "letter": letter,
            "points": points,
            "credits": courses_dict[course],
        }
        student_courses[name][course] = course_record
        current_term_courses[name][course] = course_record
        students["Grades"][index] = score
        print("Course Added Successfully")
        print("Letter Grade :", letter)
        print("Grade Points :", points)
    except ValueError:
        print("! Invalid Input !")

def calculate_gpa_from_courses(courses):
    if len(courses) == 0:
        return 0.0
    total_points = 0
    total_credits = 0
    for course in courses:
        points = courses[course]["points"]
        credits = courses[course]["credits"]
        total_points += points * credits
        total_credits += credits
    if total_credits == 0:
        return 0.0
    return total_points / total_credits

def update_gpa(index):
    name = students["name"][index]
    gpa = calculate_gpa_from_courses(current_term_courses.get(name, {}))
    students["GPA"][index] = round(gpa, 3)
    return gpa

def update_cgpa(index):
    name = students["name"][index]
    cgpa = calculate_gpa_from_courses(student_courses.get(name, {}))
    students["CGPA"][index] = round(cgpa, 3)
    return cgpa

def start_new_term(index):
    name = students["name"][index]
    current_term_courses[name] = {}
    print("New Term Started. GPA Will Now Reflect Only New Courses.")

def check_student_status(index):
    name = students["name"][index]
    gpa = update_gpa(index)
    cgpa = update_cgpa(index)
    print("\n========== STUDENT STATUS ==========")
    student_objects[index].display_info()
    print("GPA :", students["GPA"][index])
    print("CGPA :", students["CGPA"][index])
    print("Standing :", academic_standing(cgpa))
    print("====================================")

def show_students_in_course():
    print("\n========== STUDENTS ==========")
    for name in students["name"]:
        print("\nName :", name)
        if len(student_courses.get(name, {})) == 0:
            print("No Courses Enrolled")
        else:
            for course in student_courses[name]:
                print("-", course)
    print("==============================")

def update_student_status(index):
    name = students["name"][index]
    print("\n1. Update Grade")
    print("2. Update Level")
    print("3. Back")
    choice = input("Choose : ")
    if choice == "1":
        if len(student_courses[name]) == 0:
            print("! Student Has No Courses !")
            return
        print("\nCourses:")
        course_list = list(student_courses[name].keys())
        for i in range(len(course_list)):
            print(i + 1, ".", course_list[i])
        try:
            course_choice = int(input("Choose Course : "))
            if course_choice < 1 or course_choice > len(course_list):
                print("! Invalid Course !")
                return
            course = course_list[course_choice - 1]
            new_score = float(input("Updated Grade : "))
            if new_score < 0 or new_score > 100:
                print("! Grade Must Be From 0 To 100 !")
                return
            letter, points = score_to_grade(new_score)
            student_courses[name][course]["score"] = new_score
            student_courses[name][course]["letter"] = letter
            student_courses[name][course]["points"] = points
            if course in current_term_courses.get(name, {}):
                current_term_courses[name][course]["score"] = new_score
                current_term_courses[name][course]["letter"] = letter
                current_term_courses[name][course]["points"] = points
            students["Grades"][index] = new_score
            update_gpa(index)
            update_cgpa(index)
            print("Student Updated Successfully")
        except ValueError:
            print("! Invalid Input !")
    elif choice == "2":
        try:
            new_level = int(input("Updated Level : "))
            if new_level < 1 or new_level > 4:
                print("! Level Must Be From 1 To 4 !")
                return
            students["level"][index] = new_level
            sync_student_object(index)
            print("Student Updated Successfully")
        except ValueError:
            print("! Invalid Level !")
    elif choice == "3":
        return
    else:
        print("Invalid Option")

def show_transcript(index):
    name = students["name"][index]
    gpa = update_gpa(index)
    cgpa = update_cgpa(index)
    print("\n")
    print("==========================================")
    print("        STUDENT ACADEMIC TRANSCRIPT")
    print("==========================================")
    print("Program :", Program_name)
    student_objects[index].display_info()
    print("------------------------------------------")
    if len(student_courses[name]) == 0:
        print("No Courses Enrolled")
    else:
        for course in student_courses[name]:
            information = student_courses[name][course]
            print("Course :", course)
            print("Credits :", information["credits"])
            print("Score :", information["score"])
            print("Letter :", information["letter"])
            print("Grade Points :", information["points"])
            print("------------------------------------------")
    print("GPA :", round(gpa, 3))
    print("CGPA :", round(cgpa, 3))
    print("Standing :", academic_standing(cgpa))
    print("==========================================")

def save_data():
    data = {
        "students": students,
        "student_courses": student_courses,
        "current_term_courses": current_term_courses,
    }
    try:
        with open("students_data.json", "w") as file:
            json.dump(data, file, indent=4)
        print("Data Saved Successfully")
    except Exception:
        print("! Error While Saving Data !")

def load_data():
    global students
    global student_courses
    global current_term_courses
    global student_objects
    try:
        with open("students_data.json", "r") as file:
            data = json.load(file)
        students = data["students"]
        student_courses = data["student_courses"]
        current_term_courses = data.get("current_term_courses", {})
        student_objects = [
            Student(students["name"][i], students["ID"][i], students["level"][i])
            for i in range(len(students["name"]))
        ]
        print("Data Loaded Successfully")
    except FileNotFoundError:
        print("No Saved Data Found. Starting With Default Data.")
    except Exception:
        print("! Error While Loading Data !")

if __name__ == "__main__":
    load_data()
    while True:
        print("\n==========================================")
        print("   ", Program_name)
        print("      STUDENT ACADEMIC RECORD SYSTEM")
        print("==========================================")
        print("1. Add Student")
        print("2. Load Student")
        print("3. Enroll In Course & Enter Grade")
        print("4. View Transcript")
        print("5. Check Student Status")
        print("6. Show Students In Course")
        print("7. Update Student Status")
        print("8. Start New Term")
        print("9. View Advisor")
        print("10. Save")
        print("11. Add Advisor")
        print("12. Exit Program")
        choose = input("Choose : ")
        if choose == "1":
            add_student()
        elif choose == "2":
            index = load_student()
            if index is None:
                continue
            while True:
                print("\nStudent :", students["name"][index])
                print("1. Enroll In Course & Enter Grade")
                print("2. View Transcript")
                print("3. Check Student Status")
                print("4. Show Students In Course")
                print("5. Update Student Status")
                print("6. Start New Term")
                print("7. Exit Student Information")
                student_choice = input("Choose : ")
                if student_choice == "1":
                    enroll_course(index)
                elif student_choice == "2":
                    show_transcript(index)
                elif student_choice == "3":
                    check_student_status(index)
                elif student_choice == "4":
                    show_students_in_course()
                elif student_choice == "5":
                    update_student_status(index)
                elif student_choice == "6":
                    start_new_term(index)
                elif student_choice == "7":
                    print("Student Information Closed")
                    break
                else:
                    print("Invalid Option , Please Try Again !")
        elif choose == "3":
            index = load_student()
            if index is not None:
                enroll_course(index)
        elif choose == "4":
            index = load_student()
            if index is not None:
                show_transcript(index)
        elif choose == "5":
            index = load_student()
            if index is not None:
                check_student_status(index)
        elif choose == "6":
            show_students_in_course()
        elif choose == "7":
            index = load_student()
            if index is not None:
                update_student_status(index)
        elif choose == "8":
            index = load_student()
            if index is not None:
                start_new_term(index)
        elif choose == "9":
            view_advisor()
        elif choose == "10":
            save_data()
        elif choose == "11":
           add_advisor()
        elif choose == "12":
            exit_text = input("Exit Program? (Y/N) : ")
            if exit_text.upper() == "Y":
                save_data()
                print("Program Closed")
                break
            elif exit_text.upper() == "N":
                continue
            else:
                print("Invalid Answer , Please Look At The Options And Try Again !")
        else:
            print("Invalid Option , Please Look At The Options And Try Again !")