students_data = {'Mike': '50', 'John': '40', 'Nick': '70'}

student_name = input("Please Enter student\'s name to search: ")

if student_name not in students_data.keys():
    print("Student Not Found")
else:
    print(f"{student_name}\'s marks: {students_data[student_name]}")
