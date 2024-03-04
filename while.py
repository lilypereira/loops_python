total = 0
count = 0 
excluded_numeber = -1

while True:
    user_input = int(input("Please enter a number: ")) 
    
    if user_input != excluded_numeber:
        total += user_input
        count += 1
        average = total / count
    
    
    elif user_input == -1:
        break
    
if count > 0 :

    print(f'The average of numbers entered is: {average}')
    

    