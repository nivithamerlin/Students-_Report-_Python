import json

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

def calculate_average(student_id, term_name):
    student = students_data.get(student_id)
    if not student:
        print(f"Student {student_id} not found")
        return None
    term = student["terms"].get(term_name)
    if not term:
        print(f"{term_name} not found for {student_id}")
        return None
    total = sum(term.values())
    count = len(term)
    return round(total / count, 2)

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
    return round(percentage, 1)

def generate_student_report(student_id):
    student = students_data.get(student_id)
    if not student:
        print(f"No student found with ID {student_id}")
        return

    name = student["name"]
    batch = student["batch"]
    attendance_pct = calculate_attendance_percentage(student_id)

    print(f"\nStudent Report: {name} ({student_id})")
    print(f"Batch: {batch}")
    print(f"Attendance: {attendance_pct}%")

    overall_total = 0
    overall_subjects = 0
    term_averages = {}

    for term_name, subjects in student["terms"].items():
        term_total = sum(subjects.values())
        term_count = len(subjects)
        term_avg = term_total / term_count
        term_averages[term_name] = round(term_avg, 2)

        overall_total += term_total
        overall_subjects += term_count

    for term, avg in term_averages.items():
        print(f"{term} Average: {avg}")

    overall_avg = round(overall_total / overall_subjects, 2)
    print(f"Overall Average: {overall_avg}")

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

def import_data_from_json(filename):
    global students_data
    with open(filename, "r") as file:
        students_data = json.load(file)
    print(f"Data imported from {filename}")
generate_student_report("S1001")
topper_by_term("Term 2")

