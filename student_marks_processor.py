#Student Marks Processor

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

def assign_grade(overall_mark): #function to assign grade
  try:
    if overall_mark >= 90:
      return "A+"
    elif overall_mark >= 80:
      return "A"
    elif overall_mark >= 70:
      return "B"
    elif overall_mark >= 60:
      return "C"
    elif overall_mark >= 50:
      return "D"
    else:
      return "F"
  except Exception:
    return "Invalid"

data_write = {
    "registration number": [
        "REG001", "REG002", "REG003", "REG004", "REG005",
        "REG006", "REG007", "REG008", "REG009", "REG010"
        ],
    "exam marks": [78, 65, 90, 55, 45, 38, 100, 72, 81, 59],
    "coursework marks": [82, 70, 85, 60, 50, 42, 100, 68, 79, 62]
}

df_write = pd.DataFrame(data_write)

#Writing the dataframe to CSV file
df_write.to_csv("student_marks.csv", index = False)

filename = "student_marks.csv"

#print("Marks written to Student Marks CSV file") #Checkpoint for creating the CSV file

#Read data with error handling
try:
  if not os.path.exists(filename):
    raise FileNotFoundError(f"{filename} not found.")
    data_read = pd.read_csv(filename)
    print("File read successfully.\n")
except FileNotFoundError as fe:
  print(f"File error: {fe}")
  data_read = pd.DataFrame()  # Empty DataFrame to avoid further crashing
except pd.errors.ParserError:
  print("Parsing error: File contents are not properly formatted.")
  data_read = pd.DataFrame()
except Exception as e:
  print(f"Unexpected error: {e}")
  data_read = pd.DataFrame()

#print(data_read) #Checkpoint for reading the created CSV file

df_read = pd.DataFrame(data_read)

#Computing overall weighted marks with error handling

exam_mark_weight = 0.6 #60% weightage of exam marks
coursework_mark_weight = 0.4 #40% weightage of exam marks

try:
  if not df_read.empty:
    df_read["overall marks"] = (
    df_read["exam marks"] * exam_mark_weight +
        df_read["coursework marks"] * coursework_mark_weight)
    print("Overall marks computed.\n")
except KeyError as ke:
    print(f"Missing column: {ke}")
except Exception as e:
    print(f"Error computing overall marks: {e}")


#print(df_read) #Checkpoint to check the new column

#Assigning grades with error handling
try:
  if "overall marks" in df_read.columns:
    df_read["Grade"] = df_read["overall marks"].apply(assign_grade) #applying the assign_grade() function to each cell
    print("Grades assigned.\n")
except Exception as e:
    print(f"Error assigning grades: {e}")

#print(df_read)  #Checkpoint

#Defining the structure of the numpy array with Exception Handling
try:
  if not df_read.empty:
    dtype = [
      ('reg_no','U10'), #Registration number can hold upto 10 characters, say
      ('exam_marks','i4'), #Int4 values
      ('coursework_marks','i4'),  #Int4 values
      ('overall_marks','f4'), #Float values
      ('grade','U2')  #Grade will hold upto 2 characters
  ]

    #Transforming the dataframe into a list of tuples
    data_tuples = list(df_read.itertuples(index=False, name=None))

    marks_arr = np.array(data_tuples,dtype) #Storing the transformed list of tuples into a structured numpy array 
    #print(marks_arr) #Checkpoint for outputting the created structured array
    print("Structured NumPy array created.\n")

except Exception as e:
    print(f"Error creating structured array: {e}")

#Sorting by overall marks with Exception Handling
try:
    if not df_read.empty:
      sorted_overall_marks = df_read.sort_values(by='overall marks', ascending=True)
      #print(sorted_overall_marks) #Checkpoint for sorted array
      print("Sorted by overall mark.\n")
except Exception as e:
    print(f"Error sorting data: {e}")

#Writing the output to a CSV file with Exception Handling
try:
    if not df_read.empty:
      sorted_overall_marks.to_csv("final_sorted_marks_file.csv", index = False) #Writing the final dataframe to CSV
      print("File written to CSV\n") #1st checkpoint for the output

except Exception as e:
    print(f"Error writing to output file: {e}")

#output_file_read = pd.read_csv("final_sorted_marks_file.csv")
#print(output_file_read) #2nd checkpoint for the output

#Printing Grade statistics
try:
    if "Grade" in sorted_overall_marks.columns:
      plt.bar(sorted_overall_marks['registration number'],sorted_overall_marks['Grade'])
      plt.xlabel("Grades")
      plt.ylabel("Number of Students")
      plt.title("Distribution of Grades")
      plt.show()

except Exception as e:
    print(f"Error displaying grade statistics: {e}")
