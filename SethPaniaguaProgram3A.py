

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
