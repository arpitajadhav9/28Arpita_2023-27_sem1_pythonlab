# NESTED TUPLE
# WAP TO PRINT THE NAME OF THE TOPPER (OUR NAME) AND HIS/HER MARKS IN FOUR SUBJECTS WHEREIN THE MARKS ARE SPECIFIED AS A LIST IN THE TUPLE TOPPER.
# NAME OF THE TUPLE IS TOPPER....

topper = (
    ("Sakshi Kore", [90, 95, 94, 91]),
    ("Yashika", [80, 85, 72, 88]),
    ("Arpita", [88, 90, 78, 90]),
    ("Bhagyasgree", [82, 89, 84, 91])
)
topper_name = ""
topper_marks = 0
for student, marks in topper:
    total_marks = sum(marks)
    if total_marks > topper_marks:
        topper_name = student
        topper_marks = total_marks
print("The topper is", topper_name, "with marks:", topper_marks)
topper_index = [student[0] for student in topper].index(topper_name)
print("Marks of", topper_name, "are:", topper[topper_index][1])