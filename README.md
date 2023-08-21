# Ellison Private Elementary School

Instructions: Ellison Private Elementary School has three classrooms in each of nine grades, kindergarten (grade 0) through grade 8, and allows parents to pay tuition over the nine-month school year. Design the application that outputs nine tuition payment coupons for each of the 27 classrooms. Each coupon should contain the grade number (0 through 8), the classroom number (1 through 3), the month (1 through 9), and the amount of tuition due. Tuition for kindergarten is $80 per month. Tuition for the other grades is $60 per month times the grade level.


Pseudocode:
          BEGIN
            DECLARE grade = 0
            DECLARE classroom = 1
            DECLARE monthNumber = 1
            DECLARE kndrgrtn_tuition = 80
            DECLARE month = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

            WHILE grade < 9

              // kindergarten
              IF grade < 1
                PRINT "Kindergarten"
                WHILE classroom < 4
                  PRINT "Classroom " + classroom
                  monthNumber = 1  // Reset monthNumber for each classroom
                  WHILE monthNumber < 10
                    PRINT "Month " + month[monthNumber - 1]  // Adjusted index
                    PRINT "Tuition " + kndrgrtn_tuition
                    monthNumber = monthNumber + 1
                  ENDWHILE

                  classroom = classroom + 1
                ENDWHILE

              // grade 1 through 8
              else
                PRINT "Grade " + grade
                WHILE classroom < 4
                  PRINT "Classroom " + classroom
                  monthNumber = 1  // Reset monthNumber for each classroom
                  DECLARE tuition = 60 * grade
                  WHILE monthNumber < 10
                    PRINT "Month " + month[monthNumber - 1]  // Adjusted index
                    PRINT "Tuition " + tuition
                    monthNumber = monthNumber + 1
                  ENDWHILE

                  classroom = classroom + 1
                ENDWHILE
              ENDIF

              // flag variable
              grade = grade + 1 
            ENDWHILE
          END
