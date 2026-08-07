def border(func):
    def wrapper(*args):
        print("=" * 30)
        func(*args)
        print("=" * 30)
    return wrapper


class Report:

    template = "Student Report"

    def __init__(self, name, marks, grade):
        self.name = name
        self.marks = marks
        self.grade = grade

    def __str__(self):
        return (f"{self.template}\n"
                f"Name  : {self.name}\n"
                f"Marks : {self.marks}\n"
                f"Grade : {self.grade}")

    @border
    def display(self):
        print(self)


# User Input
name = input("Enter Student Name: ")
marks = int(input("Enter Marks: "))
grade = input("Enter Grade: ")

# Create Object
student = Report(name, marks, grade)

# Display Report
student.display()
