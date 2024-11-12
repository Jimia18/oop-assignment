# add a constuctor for the constructor for the cohort class
#add a method to the class that prints the cohort name and the number of students
#create a new instance/object of the cohort class.
class cohort_four:
    def __init__(self,student_name,age,course_unit,start_date,end_date):
        self.student_name = student_name
        self.age = age
        self.course_unit = course_unit
        self.start_date = start_date
        self.end_date = end_date
p1 = cohort_four('Jimia','20','computer science','08/2024','08/2026')
print(f'My name is {p1.student_name} and am {p1.age}years old,pursuing a diploma in {p1.course_unit} which i started in {p1.start_date} and am finalising in {p1.end_date}')

#Add a method to the class that prints the cohort name ,and the total number of students
class cohort:
    def __init__(self,cohort_name,total_number_of_students):
        self.cohort_name = cohort_name
        self.total_number_of_students = total_number_of_students
    def method(num):
        print(f'The name of the cohort is {num.cohort_name} and the total number of students is {num.total_number_of_students}')
p1 = cohort('cohort_four',55)
p1.method()


#creating a new instance/object of the cohort class
class cohort_four:
    def __init__(self,cohort_name,cohort_size,start_date):
        self.cohort_name = cohort_name
        self.cohort_size = cohort_size
        self.start_date = start_date
p1 = cohort_four('cohort_four',55,'08/23')       
print(f'The name of our cohort is {p1.cohort_name}, its consists {p1.cohort_size} and it started on {p1.start_date}')