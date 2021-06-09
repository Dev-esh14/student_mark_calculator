"""
Mr.Jochen working on creating application for his school. Here are the following
functions that he would to like create -
1. get_student_marks - which takes student mark1, mark2 and mark3
and return its total.
2. get_student_grade - which calls get_student_marks and returns “A”
grade if mark1 is greater than 50, else it should return grade “B”.
3. validate_marks - which validates mark1, mark2, mark3. Here are the
validations -
1. If any of the mark is less than zero or not a number, this function
should return False.
2. If any of the mark is greater than 25, then this function should
return False.
3. Else, this function should return True
 4. validate_student_name - this function should check whether student
name is of length > 5 and less than 25. If name valid, return True, else return False
 5. main - Function which should take name and marks (m1, m2, m3
respectively).
	 	 a. Call validate_student_name function if it gives False, print “Invalid
Student Name”.
	 	 b. If not, Call validate_marks function and if it gives False, print
“Invalid Mark input”.
	 	 c. If not, do a simple check, ensure minimum score of each marks
(m1, m2, m3) is greater than or equal to 7. If not, print “You got failed, grades
cannot be calculated”.
	 	 d. If not, call get_student_grade method and print the grade which this
function returned as the output.
"""

def get_student_marks(mark1,mark2,mark3):
    total=mark1+mark2+mark3
    return total
def get_student_grade(get_student_marks):
    if mark1 >= 50:
        return "A"
    else:
        return "B"
def validate_marks(get_student_marks):
    if mark1<=0 or mark2<=0 or mark3 <=0:
        return False
    elif mark1>=25 or mark2>=25 or mark3 >=25:
        return False
    else:
        return True
def validate_student_name(student_name):
    if len(student_name)>5 and len(student_name)<25 :
        return True
    else:
        return False
def main(validate_student_name,get_student_marks,validate_marks,get_student_grade):
    if validate_student_name(student_name) == False:
        return "Invalid Student Name"
    elif validate_marks(get_student_marks) == False:
        return "Invalid Mark input"
    elif mark1<=7 or mark2<=7 or mark3<=7 :
        return "You got failed, grades cannot be calculated"
    else:
        return get_student_grade(get_student_marks)
mark1=int(input("enter the mark:"))
mark2=int(input("enter the mark:"))
mark3=int(input("enter the mark:"))
print(get_student_marks(mark1,mark2,mark3))
get_student_grade(get_student_marks)
validate_marks(get_student_marks)
student_name=input("enter your name:")
validate_student_name(student_name)
print(main(validate_student_name,get_student_marks,validate_marks,get_student_grade))

"""
OUTPUT:
enter the mark:50
enter the mark:45
enter the mark:60
155
enter your name:hari
"Invalid Student Name"
"""