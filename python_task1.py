import json
import pprint

students_data = {
    "S1001": {"name": "Ashwini", "batch": "2024", "attendance": {"total_days": 200, "present_days": 185},
              "terms": {"Term 1": {"Math": 100, "Physics": 92, "English": 81},
                        "Term 2": {"Math": 91, "Physics": 94, "English": 89}}},
    "S1002": {"name": "Rekha", "batch": "2024", "attendance": {"total_days": 200, "present_days": 167},
              "terms": {"Term 1": {"Math": 88, "Physics": 92, "English": 67},
                        "Term 2": {"Math": 91, "Physics": 84, "English": 69}}}
}
 
def updated_subject_mark(data, student_id, term_name, subject_name, new_mark):
    if student_id in data:
        student = data[student_id]
        if "terms" in student and term_name in student["terms"]:
            if subject_name in student["terms"][term_name]:
                student["terms"][term_name][subject_name] = new_mark
                print(f"{subject_name} mark is updated to {new_mark} for {student_id} in {term_name}")
            else:
                print(f"student {subject_name} is not found in {term_name}")
        else:
            print(f"{term_name} not found for student {student_id}")
    else:
        print(f"student id {student_id} not found")
updated_subject_mark(students_data, "S1001", "Term 1", "Math", 100)

def calculate_average(student_id, term_name):
    if student_id not in students_data:
        print(f" student id, {student_id} is not found")
        return
    student = students_data[student_id]
    terms = student.get("terms", {})
    total_marks = 0
    subject_count= 0
    for term_name, subject in terms.items():
        for subject, mark in subject.items():
            total_marks += mark
            subject_count += 1
    if subject_count == 0:
        print(f"no marks found for {student_id}")
    average = total_marks / subject_count
    print(f"average for total marks for {student_id} for {term_name} is {average:.2f}")
    return average
calculate_average("S1001", "Term 1")

def calculate_attendance_percentage(student_id):
    if student_id not in students_data:
        print(f"student id {student_id} not found")
        return 
    student = students_data[student_id]
    attendance = student.get("attendance")
    if not attendance:
        print("No attendance data found")
        return
    total_days = attendance.get("total_days", 0)
    present_days = attendance.get("present_days", 0)
    if total_days == 0:
        print("Total days is zero cannot calculate percentage for it")
        return
    percentage = (present_days / total_days) * 100
    print(f"attendance percentage for {student_id} is {percentage}")
calculate_attendance_percentage("S1002")

def topper_by_term(term_name):
    topper = None
    highest_avg = 0
    for student_id, student_info in students_data.items():
        term_marks = student_info["terms"].get(term_name)
        if term_marks:
            total = sum(term_marks.values())
            avg = total / len(term_marks)
            print(f"{student_info['name']}'s average in {term_name}: {avg}")
            if avg > highest_avg:
                highest_avg = avg
                topper = student_info["name"]
    print(f"topper of {term_name} is {topper} with average {highest_avg}")
topper_by_term("Term 1")

def rank_topper_by_batch(batch):
    topper_id = None
    topper_name = ""
    topper_marks = 0
    for student_id in students_data:
        student = students_data[student_id]
        if student["batch"] != batch:
            continue
        terms = student["terms"]
        total_marks = 0

        for term_name in terms:
            subjects = terms[term_name]

            for subject in subjects:
                mark = subjects[subject]
                total_marks += mark

        print(f"Student ID: {student_id}, Name: {student['name']}, Total Marks: {total_marks}")
        if total_marks > topper_marks:
            topper_id = student_id
            topper_name = student["name"]
            topper_marks = total_marks
    print(f"Topper is {topper_name} id {topper_id} with total {topper_marks}")
rank_topper_by_batch("2024")
def generate_student_report(student_id):
    student = students_data[student_id]
    if not student:
        print(f"no student found with ID {student_id}")
        return
    print(f"Student report for {student['name']} (ID: {student_id}, Batch: {student['batch']})\n")
    attendance_percent = 0
    attendance = student["attendance"]
    total = attendance["total_days"]
    present = attendance["present_days"]
    attendance_percent = (present / total) * 100
    print(f"Attendance percentage for {student['name']} is {attendance_percent}%")
   
    total_marks = 0
    sub_count  = 0
    for term_name, subjects in student["terms"].items():
        print(f"Term: {term_name}")
        for subject, marks in subjects.items():
            print(f"{subject}: {marks}")
            total_marks += marks
            sub_count += 1
        print()
    average = total_marks / sub_count if sub_count else 0
    print(f"Total marks: {total_marks}")
    print(f"Average marks: {round(average, 2)}")
generate_student_report("S1001")
def export_data_to_json(filename):
    with open(filename, "w") as file:
        json.dump(students_data, file, indent=4)
    print(f"Data exported to {filename}")
export_data_to_json("students.json")
def import_data_from_json(filename):
    global students_data
    with open(filename, "r") as file:
        students_data = json.load(file)
    print(f"Data imported from {filename}")
import_data_from_json("students.json")

