import json
import os
sample_data = {
    "S1001": {
        "name": "Ashwini",
        "batch": "2024",
        "attendance": {
            "total_days": 200,
            "present_days": 185
        },
        "terms": {
            "Term 1": {
                "Math": 100,
                "Physics": 92,
                "English": 81
            },
            "Term 2": {
                "Math": 91,
                "Physics": 94,
                "English": 89
            }
        }
    },
    "S1002": {
        "name": "Rekha",
        "batch": "2024",
        "attendance": {
            "total_days": 200,
            "present_days": 167
        },
        "terms": {
            "Term 1": {
                "Math": 88,
                "Physics": 92,
                "English": 67
            },
            "Term 2": {
                "Math": 91,
                "Physics": 84,
                "English": 69
            }
        }
    }
}
students_data = {}

def import_data_from_json(filename):
    global students_data
    with open(filename, "r") as file:
        students_data = json.load(file)
    

def register_student(student_id, name, batch):
    if student_id in students_data:
        print(f"Student ID {student_id} already exists")
        return 
    students_data[student_id] = {
        "name": name,
        "batch": batch,
        "attendance": {
            "total_days": 0,
            "present_days": 0
        },
        "terms": {}
    }
    print(f"Student {name} ({student_id}) updated successfully.")

def add_term_result(student_id, term_name, subject_marks_dict):
    if student_id not in students_data:
        print(f"Student ID {student_id} not found")
        return
    student = students_data[student_id]
    if "terms" not in student:
        student["terms"] = {}
    if term_name not in student["terms"]:
        student["terms"][term_name] = {}
    student["terms"][term_name].update(subject_marks_dict)
    
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
        print(f"student ID {student_id} not found")
        return
    student = students_data[student_id]
    attendance = student.get("attendance")
    if not attendance:
        print(f"No attendance data for {student['name']}")
        return 
    total_days = attendance.get("total_days", 0)
    present_days = attendance.get("present_days", 0)
    if total_days == 0:
        print(f"Invalid total days for {student['name']}")
        return
    percentage = (present_days / total_days) * 100
    print(f"{student['name']} - Attendance: {round(percentage, 1)}%")
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

def export_data_to_json(filename):
    with open(filename, "w") as file:
        json.dump(students_data, file, indent=4)
def delete_subject_mark(student_id, term_name, subject_name):
    if student_id not in students_data:
        print(f"Student ID {student_id} not found.")
        return
    if term_name not in students_data[student_id]["terms"]:
        print(f"Term '{term_name}' not found for student {student_id}.")
        return
    if subject_name not in students_data[student_id]["terms"][term_name]:
        print(f"Subject '{subject_name}' not found in {term_name}.")
        return
    
    del students_data[student_id]["terms"][term_name][subject_name]
    print(f"Deleted subject '{subject_name}' from {term_name} for student {student_id}.")

def students_progress_report():
    for student_id, student_info in students_data.items():
        name = student_info["name"]
        term = student_info["terms"]
        for term_name, subjects in term.items():
            status = "Pass"
            for subject, mark in subjects.items():
                if mark < 40:
                    status = "Fail"
                    break
            print(f"{student_id} - {name} in {term_name} : {status}")

   

if __name__ == "__main__":
    filename = "students.json"
    if not os.path.exists(filename):
        students_data = sample_data
        export_data_to_json(filename)
    else:
        import_data_from_json(filename)

    
    students_progress_report()
    
    generate_student_report("S1003")
    
    rank_topper_by_batch("2024")
