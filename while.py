total = 0  # Initializing the total sum of numbers entered
count = 0  # Initializing the count of numbers entered
excluded_number = -1  # Specifying a number that, if entered, will not be included in calculations

# Continuous loop to receive input from the user until explicitly broken
while True:
    user_input = int(input("Please enter a number: "))  # Asking the user to input a number
    
    # Checking if the entered number is not the excluded number
    if user_input != excluded_number:
        total += user_input  # Adding the entered number to the total sum
        count += 1  # Incrementing the count of numbers entered
        average = total / count  # Calculating the current average
        
    # If the entered number matches the excluded number, exit the loop
    elif user_input == excluded_number:
        break

# If at least one number was entered
if count > 0:
    print(f'The average of numbers entered is: {average}')  # Displaying the average of the entered numbers
