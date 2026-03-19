student = {}

# Add student
def add_student(records, name, marks):
    records[name] = marks

# View students
def view_students(records):
    for name, marks in records.items():
        print(name, ":", marks)

# Find student
def find_student(records, name):
    if name in records:
        print(name, "marks:", records[name])
    else:
        print("Student not found")


# Main program
add_student(student, "Rakesh", 78)
add_student(student, "Rahul", 85)
add_student(student, "Anita", 92)

print("All Students:")
view_students(student)

print("\nSearch Result:")
find_student(student, "Rakesh")
