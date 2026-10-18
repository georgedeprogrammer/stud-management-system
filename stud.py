import csv
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
file_name = os.path.join(script_dir, "students.csv")
student_list = {}
def save_data():
    headers = [
        "ADM", "Full_Name", "Programme",
        "Math", "Eng", "Subject Marks",
        "Average", "Grade"
    ]

    try:
        with open(
            file_name,
            mode="w",
            newline="",
            encoding="utf-8"
        ) as file:
            writer = csv.DictWriter(
                file,
                fieldnames=headers
            )
            writer.writeheader()

            for admission_number, details in student_list.items():
                writer.writerow({
                    "ADM": admission_number,
                    "Full_Name": (
                        f"{details.get('First Name', '')} "
                        f"{details.get('Last Name', '')}"
                    ).strip(),
                    "Programme": details.get("Programme", ""),
                    "Math": details.get("Math", ""),
                    "Eng": details.get("Eng", ""),
                    "Subject Marks": details.get("Subject Marks", ""),
                    "Average": details.get("Average", ""),
                    "Grade": details.get("Grade", "")
                })

        print("Student records saved successfully.")

    except OSError as e:
        print(f"Error saving student records: {e}")

def load_data():
    students = {}
    if os.path.exists(file_name):
        try:
            with open(file_name, mode="r", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    name_parts = row.get("Full_Name", "").split(maxsplit=1)
                    students[row["ADM"]] = {
                        "First Name": name_parts[0] if name_parts else "",
                        "Last Name": name_parts[1] if len(name_parts) > 1 else "",
                        "Programme": row.get("Programme", ""),
                        "Subject Marks": row.get("Subject Marks", ""),
                    }
        except Exception as e:
            print(f"[!] Error loading CSV file: {e}. Starting with an empty list.")
    return students

student_list = load_data()

class Student:
    def __init__(stud, ID_Number, first_name, last_name, programme):
        stud.ID_Number = ID_Number
        stud.first_name = first_name
        stud.last_name = last_name
        stud.programme = programme
    
    def add(stud):
        stud.ID_Number = input("Enter your school ID Number: ").strip().upper()
        if stud.ID_Number in student_list:
                print(f"[!] ADM {stud.ID_Number} already exists! Use a different ID or delete the old entry first.")
                return
        stud.first_name = input("Enter your first name: ").strip()
        stud.last_name = input("Enter your last name: ").strip()
        stud.programme = input("Enter your course programme: ").strip()
        student_list[stud.ID_Number] = {"First Name": stud.first_name, "Last Name": stud.last_name, "Programme": stud.programme}
        print(f"[SUCCESS] {stud.first_name} {stud.last_name} has been added.")

        print(f"\n---------------STUDENT REPORT------------------")
        print(f" ADM: {stud.ID_Number}")
        print(f" Full Name: {stud.first_name}  {stud.last_name}")
        print(f" Course: {stud.programme}")

    def delete_student(stud):
        stud.ID_Number = input("Enter admission number to delete: ").strip()
        print("\n--- Delete a Student ---")
           
        if stud.ID_Number in student_list:
            student_list.pop(stud.ID_Number)
            print(f"[SUCCESS] Student: {stud.first_name} {stud.last_name} (ID: {stud.ID_Number}) was removed.")
        else:
            print(f"[ERROR] Student ID '{stud.ID_Number}' does not exist.")

    def Update(stud):   
        admission_number = input("Enter student ID to update: ").strip().upper()

        if admission_number not in student_list:
            print("Student not found.")
            return
        details = student_list[admission_number]
        print("Leave a field blank to keep its current value.")
        new_first = input(f"First name [{details['First Name']}]: ").strip()
        new_last = input(f"Last name [{details['Last Name']}]: ").strip()
        new_programme = input(f"Programme [{details['Programme']}]: ").strip()
        if new_first:
            details["First Name"] = new_first
        if new_last:
            details["Last Name"] = new_last
        if new_programme:
            details["Programme"] = new_programme

        print("Student record updated successfully.")
            
        print(f"\n---------------STUDENT REPORT------------------")
        print(f" ADM:       {stud.ID_Number}")
        print(f" Full Name: {stud.first_name} {stud.last_name}")
        print(f" Course:    {stud.programme}")

    def find_student(stud):
        admission_number = input("Enter the admission number to find: ").strip().upper()

        if admission_number in student_list:
            details = student_list[admission_number]
            print("Student found!")
            print(f"ADM: {admission_number}")
            print(f"Name: {details['First Name']} {details['Last Name']}")
            print(f"Programme: {details['Programme']}")
        else:
            print("Student not found.")
    
    def display_students(stud):
        print("\n================ CURRENT STUDENT LIST================")
        if not student_list:
            print("   The database is empty. No students found.")
        else:
            for ID_Number, details in student_list.items():
                print(
                    f"   ID: {ID_Number} | "
                    f"Name: {details['First Name']} {details['Last Name']} | "
                    f"Programme: {details['Programme']} | "
                )
        print("========================================================")

class Perfomance_Track:
    def __init__(stud, ID_Number, Unit_Title1, Unit_Title2, Subject_Marks, average, grade):
        stud.ID_Number = ID_Number
        stud.Unit_Title1 = Unit_Title1
        stud.Unit_Title2 = Unit_Title2
        stud.Subject_Marks = Subject_Marks
        stud.average = average
        stud.grade = grade

        stud.result_list = {}

    def Call_Marks(stud):
        stud.ID_Number = input("Enter your ID number: ").strip().upper()

        try:
            stud.Unit_Title1 = float(input("Enter marks for unit 1: "))
            stud.Unit_Title2 = float(input("Enter marks for unit 2: "))
        except ValueError:
            print("Please enter numeric marks.")

        if not (0 <= stud.Unit_Title1 <= 100 and 0 <= stud.Unit_Title2 <= 100):
                print("Marks must be between 0 and 100.")
                return False
        return True
    save_data()

    def Total(stud):
        stud.Subject_Marks = int(stud.Unit_Title1 + stud.Unit_Title2)
    save_data()

    def Average(stud):
        stud.average = float((stud.Subject_Marks)/ 2)
    save_data()
    def Grade(stud):
        if stud.average <=100 and stud.average >69:
            Grade = "A"
        elif stud.average >59:
            Grade = "B"
        elif stud.average >49:
            Grade = "C"
        elif stud.average >39:
            Grade = "D"
        elif stud.average >0:
            Grade = "F"
        else:
            print("No Grade")
        return Grade
    save_data()

    def Results(stud):
        stud.grade = stud.Grade()
        print(f"\n---------------STUDENT REPORT------------------")
        print(f" ADM: {stud.ID_Number}")
        print(f" Total: {stud.Subject_Marks}")
        print(f" Average: {stud.average}")
        print(f"Grade: {stud.grade}")

        stud.result_list[stud.ID_Number] = {
            "ADM": stud.ID_Number,
            "Math": stud.Unit_Title1,
            "Eng": stud.Unit_Title2
        }
        student_record = student_list.setdefault(
            stud.ID_Number,
            {"First Name": "", "Last Name": "", "Programme": ""}
        )
        student_record.update({
            "Math": stud.Unit_Title1,
            "Eng": stud.Unit_Title2,
            "Subject Marks": stud.Subject_Marks,
            "Average": stud.average,
            "Grade": stud.grade,
        })
        print(f"[SUCCESS] {stud.ID_Number} has been added.")
        
class Analyzer:
    def __init__(stud, students):
        stud.student_list = students

    def _students_with_averages(stud):
        analyzed = []
        for admission_number, details in stud.student_list.items():
            average = details.get("Average")
            if average is None:
                marks = [details.get(key) for key in ("Math", "Eng")]
                if all(isinstance(mark, (int, float)) for mark in marks):
                    average = sum(marks) / len(marks)
            if isinstance(average, (int, float)):
                analyzed.append((average, admission_number, details))
        return analyzed

    def Max_Average(stud):
        students = stud._students_with_averages()
        if not students:
            print("❌ No student marks available to analyze.")
            return
        average, admission_number, details = max(students, key=lambda item: item[0])
        name = f"{details.get('First Name', '')} {details.get('Last Name', '')}".strip()
        print("\n================ TOP PERFORMING STUDENT ================")
        print(f" Name:    {name or 'Unknown'}")
        print(f" ADM:     {admission_number}")
        print(f" Course:  {details.get('Programme', 'Unknown')}")
        print(f" Highest Average Score: {average}%")
        print("========================================================")

    def Min_Average(stud):
        students = stud._students_with_averages()
        if not students:
            print("❌ No student marks available to analyze.")
            return
        average, admission_number, details = min(students, key=lambda item: item[0])
        name = f"{details.get('First Name', '')} {details.get('Last Name', '')}".strip()
        print("\n================ LOWEST PERFORMING STUDENT ================")
        print(f" Name:    {name or 'Unknown'}")
        print(f" ADM:     {admission_number}")
        print(f" Course:  {details.get('Programme', 'Unknown')}")
        print(f" Lowest Average Score: {average}%")
        print("========================================================")

class ScholarshipStudent(Student):

    def __init__(stud,ID_Number="", first_name="", last_name="", programme="", average=0, scholarship_amount=0
    ):
        super().__init__(ID_Number, first_name, last_name, programme)

        stud.average = average
        stud.scholarship_amount = scholarship_amount

    def Eligibility(stud):
        """Scholarship consideration requires an average of at least 85."""
        try:
            return float(stud.average) >= 85
        except (TypeError, ValueError):
            return False

    def student_info(stud):
        """Override the parent method with scholarship-specific information."""

        if stud.Eligibility():
            status = "Eligible for scholarship consideration"
        else:
            status = "Not eligible for scholarship consideration"

        return (
            f"{super().student_info()} | "
            f"Average: {stud.average}% | "
            f"Scholarship amount: KSh "
            f"{stud.scholarship_amount:,.2f} | "
            f"{status}"
        )
    def student_eligibility(stud):
        if stud.average is None:
            status = "Results not available"
            average_text = "Not recorded"
        else:
            try:
                average = float(stud.average)
                average_text = f"{average:.2f}%"
                status = (
                    "Eligible for scholarship consideration"
                    if average >= 85
                    else "Not eligible for scholarship consideration"
                )
            except (TypeError, ValueError):
                average_text = "Not recorded"
                status = "Results not available"

        return (
        f"ADM: {stud.ID_Number} | "
        f"Name: {stud.first_name} {stud.last_name} | "
        f"Programme: {stud.programme} | "
        f"Average: {average_text} | {status}"
    )

def main():
    student_info = Student("", "", "", "")
    perf_tracker = Perfomance_Track("", 0, 0, 0, 0,"")
    analysis = Analyzer(student_list)
    student_db = student_list
    while True:
        print("\n===== STUDENT PROGRAM =====")
        print("1. Enter and view student details")
        print("2. Analyze subject marks/ Results input")
        print("3. Update student records")
        print("4. Delete student record")
        print("5. Find Student within the list")
        print("6. Student list")
        print("7. Student with highest average")
        print("8. Student with minimum grade")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            student_info.add()
            save_data()

        elif choice == "2":
            perf_tracker.Call_Marks()
            perf_tracker.Total()
            perf_tracker.Average() 
            perf_tracker.Results()
            save_data()
            
        elif choice == "3":
            student_info.Update()
            save_data()

        elif choice == "4":
            student_info.delete_student()
            save_data()

        elif choice == "5":
            student_info.find_student()

        elif choice == "6":
            student_info.display_students()

        elif choice == "7":
            analysis.Max_Average()

        elif choice == "8":
            analysis.Min_Average()

        elif choice == "0":
            print("Program closed.")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 0.")


if __name__ == "__main__":
    main()