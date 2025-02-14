def function_with_uncommon_bug(x):
    if x == 0:
        return 0  # Handle the case where x is 0
    else:
        result = 1 / x  # This line may throw ZeroDivisionError
        return result

# This part is correct, but won't execute if error in the function
# Demonstrates a case where an error doesn't immediately crash the program but leads to unintended behavior
number = 10
result = function_with_uncommon_bug(number)
print(f"The result of division is: {result}")

# Another instance of error without immediate crash
# Illustrates a silent failure that may be difficult to track
list_of_numbers = [1, 2, 3, 0, 5]
for num in list_of_numbers:
    try:
        processed_number = function_with_uncommon_bug(num)
        print(f"The result of {num} is: {processed_number}")
    except ZeroDivisionError as e:
        print(f"Error processing {num}: {e}") #Silent failure
    except Exception as e:
        print(f"An unexpected error occurred: {e}")