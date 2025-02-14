def function_with_uncommon_bug_solution(x):
    try:
        if x == 0:
            return 0  # Handle division by zero explicitly
        else:
            result = 1 / x
            return result
    except ZeroDivisionError:
        return "Division by zero occurred"
    except Exception as e:
        return f"An unexpected error occurred: {e}"

# Improved handling of potential errors
number = 10
result = function_with_uncommon_bug_solution(number)
print(f"The result of division is: {result}")

list_of_numbers = [1, 2, 3, 0, 5]
for num in list_of_numbers:
    processed_number = function_with_uncommon_bug_solution(num)
    print(f"The result of {num} is: {processed_number}") #Error handling prevents silent failures