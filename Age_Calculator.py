#Exercise1: Age Calculator

from datetime import datetime, date

#Prompting the user to enter the date in a specific format
date_str = input("Input the date of birth in the mm/dd/yyyy format")

#Exception handling with try...except code block
try:
  #Converting the entered date into a datetime object
  date_obj = datetime.strptime(date_str, "%m/%d/%Y")
  print("The entered date is: ", date_obj.date())

  #Calculating age
  date_today = date.today()
  age = date_today.year - date_obj.year

  print("Your age is",age, "years")

  #Formatting the date to European style
  format_date = datetime.strftime(date_obj, "%d/%m/%Y")
  print("The date in European style: ", format_date)

except:
  print("The input date of birth is not in the mm/dd/yyyy format")
