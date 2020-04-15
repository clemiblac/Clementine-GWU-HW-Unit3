# Initial variable to track game play
run="y"

# Set start and last number
start=0
last_number=0

# While we are still playing...
#if run=="y":
    # Ask the user how many numbers to loop through
ask_user=int(input("How many numbers?"))
    

    # Loop through the numbers. (Be sure to cast the string into an integer.)
for x in range(start, ask_user):

    # Print each number in the range
    print(x)

# Set the next start number as the last number of the loop
next_start=ask_user
#print(f"next start number is {next_start}")
 
# Once complete... ask if the user wants to continue
ask_continue=input("Would you like to continue ? (y)es or (n)o? " )

while (ask_continue=="y"):
    
 
    # If "y", have the numbers begin at the end of the previous chain.
        ask_user=int(input("How many numbers?"))
        last_number=next_start + ask_user
        
        for x in range(next_start, last_number):
            print(x)

        #print(f"next start number is {last_number}")
        next_start = last_number
        pass
       
        ask_continue=input("Would you like to continue ? (y)es or (n)o? " )

        # If "n", exit the chain.



       