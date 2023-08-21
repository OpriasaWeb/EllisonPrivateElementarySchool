print("Welcome to Ellison Private Elementary School")

grade = 0
classroom = 1
monthNumber = 1
kndrgrtn_tuition = 80
month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

flag_variable = False

grade = int(input("What is your grade? "))

while grade < 10:
  
  # kindergarten
  if grade < 1:
    print("Kindergarten")
    
    while classroom < 4:
      print(f"Classroom {classroom}")
      monthNumber = 1
      
      while monthNumber < 10:
        print(f"Month of {month[monthNumber - 8]}")
        print(f"Tuition fee {kndrgrtn_tuition}")
      
        monthNumber = monthNumber + 1
        
      classroom = classroom + 1
    # break
  else:
    print(f"Grade {grade}")
    
    while classroom < 4:
      print(f"Classroom {classroom}")
      monthNumber = 1
      tuition = 60 * grade
      while monthNumber < 10:
        print(f"Month of {month[monthNumber - 8]}")
        print(f"Tuition fee {tuition}")
      
        monthNumber = monthNumber + 1
        
      classroom = classroom + 1
  
  # elementary
  
  # flag variable
  grade = grade + 1