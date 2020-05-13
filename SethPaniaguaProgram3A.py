#---------------------------------
#Programmer: Seth Paniagua
#Date Due: Feb. 18, 2020
#Date of First Version: Feb. 15,2020
#Date turned in: Feb. 16, 2020
#Title of Project: Write miles driven and gased used in CSV 
#Assignment: Assignment 3A
#----------------------------------
#Design
#Open File for Writing
#Create variable to continue the program using 'Y'
#Create While Loop to continue as long as user inputs 'Y'
#User Input Miles Driven
#User Input Gas Used
#write miles driven into CSV file and go to new line using \n
#write gas used into CSV file and go to new line using \n
#ask user if they would like to continue and promt them the command to continue
#close file and print "Finished writing file"
#print statement "Program completed saving X mileage records in CSV file
#------------------------------------

#Open File
mpg_file = open('E:\mileage.csv', 'w')
keep_going = 'Y'

#While Loop
while keep_going.upper() == 'Y':
    
    #Input
    miles_driven = (input("Please enter the miles driven: "))
    gas_used = (input("Please enter the gas used: "))
    
    #write data
    mpg_file.write(miles_driven + ',')
    mpg_file.write(gas_used + '\n')
    keep_going = input("Want to continue to add more data (Y or N): ")

#close file
mpg_file.close()
print("Program completed saving 4 mileage records in CSV file")
