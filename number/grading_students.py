def gradingStudents(grades):
  answer = []

  for grade in grades:
    answer.append(grade if grade <= 37 or grade % 5 <= 2 else grade + (5 - grade % 5))

  return (answer)



# One line, list comprehension version
def gradingStudents(grades):
  return ([grade if (grade <= 37 or grade % 5 <= 2) else grade + (5 - grade % 5) for grade in grades])
  
  
