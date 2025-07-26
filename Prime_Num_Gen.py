#Prime Number Generator

#Function to input two positive integers
def two_positive_integers():
  while True: #Infinite loop to continuously promp the user to enter a valid input
    try:  #Exception handling code block begins
      input_str = input("Enter two positive integers:")
      num = input_str.split()

      if len(num)!=2: #Checking if the length of numbers is unequal 2
        print("Error: Please enter TWO integers")
        continue

      num1 = int(num[0])
      num2 = int(num[1])

      if num1 <= 0 or num2 <= 0:
        print("Error: Please enter POSITIVE integers")
        continue

      return num1, num2

    except ValueError:
      print("Error: Invalid input. Please enter INTEGERS only.")

    except Exception as e:
      print("An unexpected error occured:",e)

#Main program
if __name__=="__main__":
  a,b = two_positive_integers()
  print("The two positive integers that you entered are:", a,b)

start = 0
end = 0

#Deciding which will be the start and stop position for range()
if a > b:
  start = b
  end = a
else:
  start = a
  end = b

my_list = []  #Declaring an empty list to append prime number

for i in range(start, end+1): #Finding prime numbers within the range
  counter = 0 #Initializing a counter
  for j in range(1,i+1):  #Prime number will only be divisibe by 1 and itself
    if i%j == 0:
      counter +=1

  if counter == 2:  #So if the number is only divisible two times, then its prime
    my_list.append(i)    

print(my_list)  #Printing the entire list of prime numbers

#Re-initializing i and j to 0 after the previous For loop ended
i = 0 
j = 0

#Printing 10 numbers in a single line
for i in range (0,len(my_list),10): 
  for j in range(i,min(i+10,len(my_list))):
    print(my_list[j], end=", ") #Prints 10 digits in a horizontal line
  print() #Change line
