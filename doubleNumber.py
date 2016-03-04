error = True
while error:
    number = raw_input("What number should I double? ")
    
    try:
        # Anything that might cause a problem
        # Try block is only for the exception causers
        number = float(number)
        error = False
            
    except ValueError:
        print("Sorry thats not a number. Try again")    

# Finally converted to float successfully
print("Double that is {}.".format(number*2))