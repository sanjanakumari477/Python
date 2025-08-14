PASS_MARK = 33        # per-subject pass mark
MAX_MARK = 100        # per-subject maximum marks

# Grade scale (percentage)
def overall_grade(pct):
    if pct >= 90: return "A+"
    if pct >= 80: return "A"
    if pct >= 70: return "B+"
    if pct >= 60: return "B"
    if pct >= 50: return "C"
    if pct >= 40: return "D"
    return "F"

# Per-subject grade (based on marks out of MAX_MARK)
def subject_grade(marks):
    pct = (marks / MAX_MARK) * 100
    return overall_grade(pct)

# Safe input helpers
def read_nonempty(prompt):
    while True:
        val = input(prompt).strip()
        if val:
            return val
        print("  -> Please enter a value.")

def read_int(prompt, min_v=None, max_v=None):
    while True:
        try:
            val = int(input(prompt).strip())
            if (min_v is not None and val < min_v) or (max_v is not None and val > max_v):
                print(f"  -> Enter a number between {min_v} and {max_v}.")
                continue
            return val
        except ValueError:
            print("  -> Please enter a valid integer.")

# Collect student info
college = read_nonempty("College/Institute Name : ")
student_name = read_nonempty("Student Name         : ")
roll_no = read_nonempty("Roll/Reg No.         : ")
course = read_nonempty("Course/Class         : ")
session = read_nonempty("Session (e.g. 2022-25): ")

# Subjects setup
print("\nEnter subject names (press ENTER on a blank line to finish).")
subjects = []
i = 1
while True:
    s = input(f"  Subject {i} name: ").strip()
    if s == "":
        if len(subjects) == 0:
            print("  -> Please add at least one subject.")
            continue
        break
    subjects.append(s)
    i += 1

# Collect marks
print("\nEnter obtained marks (0–100) for each subject:")
marks = []
for s in subjects:
    m = read_int(f"  {s}: ", 0, MAX_MARK)
    marks.append(m)

# Calculations
total = sum(marks)
max_total = len(subjects) * MAX_MARK
percentage = (total / max_total) * 100
all_pass = all(m >= PASS_MARK for m in marks)
overall = "PASS" if all_pass else "FAIL"
grade = overall_grade(percentage) if all_pass else "F"

# Division (commonly used in some boards)
def division(pct):
    if not all_pass:
        return "-"
    if pct >= 60: return "First"
    if pct >= 45: return "Second"
    if pct >= 33: return "Third"
    return "-"
div_text = division(percentage)

# Prepare table formatting
sub_col_w = max(8, max(len(s) for s in subjects))
mark_w = max(5, len(str(MAX_MARK)))
line = "-" * (6 + sub_col_w + 3 + mark_w + 3 + 6)

# Print Marksheet
print("\n" + "="*60)
print(f"{college.center(60)}")
print("MARKSHEET".center(60))
print("="*60)

print(f"Name    : {student_name}")
print(f"Roll No : {roll_no}")
print(f"Course  : {course}")
print(f"Session : {session}")
print("-"*60)

# Header
print(line)
print(f"| {'Sub#':<4} | { 'Subject'.ljust(sub_col_w) } | {'Marks':>{mark_w}} | Grd |")
print(line)

# Rows
for idx, (s, m) in enumerate(zip(subjects, marks), start=1):
    print(f"| {idx:<4} | {s.ljust(sub_col_w)} | {m:>{mark_w}} | {subject_grade(m):<3} |")
print(line)

# Summary
print(f"Total: {total}/{max_total}")
print(f"Percentage: {percentage:.2f}%")
print(f"Result: {overall}   Grade: {grade}   Division: {div_text}")
if not all_pass:
    failed = [s for s, m in zip(subjects, marks) if m < PASS_MARK]
    print("Remarks: Fail in -> " + ", ".join(failed))
else:
    print("Remarks: Congratulations!")

print("="*60)




#output
============================================================
    Z.A ISLAMIA COLLEGE OF TECHNOLOGY AND MANAGEMENT     
                         MARKSHEET                         
============================================================
Name    : Sanjana Kumari
Roll No : 12345
Course  : BCA
Session : 2022-25
------------------------------------------------------------
------------------------------------------------------------
| Sub# | Subject        | Marks | Grd |
------------------------------------------------------------
| 1    | Python         |    85 | A   |
| 2    | Mathematics    |    76 | B+  |
| 3    | Data Science   |    92 | A+  |
| 4    | Web Development|    88 | A   |
| 5    | DBMS           |    79 | B+  |
------------------------------------------------------------
Total: 420/500
Percentage: 84.00%
Result: PASS   Grade: A   Division: First
Remarks: Congratulations!
============================================================

