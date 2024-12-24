students = {"Rohan": 85,"Spoorthi": 90,"Aditi": 78,"Tanya": 92}
print("Q2. Student Marks Calculation:")
print("Student with the highest marks: ", max(students, key=students.get))
print("Averge Marks: ", sum(students.values())/len(students))
newstud="Ajith" ; newmark = 91 ; students[newstud] = newmark
print("Updated List: ", students)
