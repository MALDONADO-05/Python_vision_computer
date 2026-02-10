#Problem 1: Sum of integers in a range
"""
Problem 1: Sum of integers in a range
Description: 
 This program computes total sum from 1 to n and separately sums only even numbers 
 within that range. Uses for loop with range() to iterate through all numbers efficiently.

Inputs:
 n (int): maximum value for summation range

Outputs:
 "Sum 1..n: <total_sum>"
 "Even sum 1..n: <even_sum>"

Validations:
 Input must convert to integer successfully
 n must be 1 or greater for meaningful range

Test cases:
 Normal: n=5.  Sum 1..5: 15, Even sum 1..5: 6
 Edge case: n=1.  Sum 1..1: 1, Even sum 1..1: 0  
 Error: n=0 or non-numeric. Error: invalid input
"""

# Process input with validation
n_input = input("Enter upper limit n: ").strip()

try:
    limit = int(n_input)
    
    if limit < 1:
        print("Error: invalid input")
    else:
        # Initialize accumulators
        all_numbers_sum = 0
        even_numbers_sum = 0
        
        # Iterate using range() as specified
        for number in range(1, limit + 1):
            all_numbers_sum += number
            if number % 2 == 0:
                even_numbers_sum += number
        
        print(f"Sum 1..n: {all_numbers_sum}")
        print(f"Even sum 1..n: {even_numbers_sum}")
        
except ValueError:
    print("Error: invalid input")

    #Problem 2: Multiplication table with for
"""
Problem 2: Multiplication table with for
Description: 
 Program that generates multiplication table for a base number up to limit m. 
 Displays each multiplication in format "base x multiplier = product" using for loop 
 with range() to control table length.

Inputs:
 base (int): number to multiply
 m (int): table length limit

Outputs:
 Each line: "base x i = product" for i from 1 to m

Validations:
 Both inputs must convert to integers
 m must be 1 or greater

Test cases:
 Normal: base=5, m=4. 5 x 1 = 5, 5 x 2 = 10, 5 x 3 = 15, 5 x 4 = 20
 Edge case: base=3, m=1. 3 x 1 = 3
 Error: m=0 or non-numeric. Error: invalid input
"""

# Get and validate inputs
base_txt = input("Enter base number: ").strip()
limit_txt = input("Enter table limit m: ").strip()

try:
    base_number = int(base_txt)
    table_limit = int(limit_txt)
    
    if table_limit < 1:
        print("Error: invalid input")
    else:
        # Generate multiplication table using for + range
        for multiplier in range(1, table_limit + 1):
            product = base_number * multiplier
            print(f"{base_number} x {multiplier} = {product}")
            
except ValueError:
    print("Error: invalid input")

#Problem 3: Average of numbers with while and sentinel
"""
Problem 3: Average of numbers with while and sentinel
Description: 
 Reads numbers one by one until sentinel value (-1) is entered. Calculates average 
 of valid numbers (>=0) entered and total count. Invalid inputs are rejected and 
 re-prompted without counting.

Inputs:
 number (float): numbers entered repeatedly
 sentinel_value: fixed at -1 (hardcoded)

Outputs:
 "Count: <valid_count>"
 "Average: <average_value>"
 "Error: no data" if no valid numbers
 "Error: invalid input" for non-numeric

Validations:
 Numbers must convert to float
 Only accept numbers >= 0 (ignore sentinel)
 Reject negative numbers != -1 and non-numeric

Test cases:
 Normal: 10, 20, 30, -1. Count: 3, Average: 20.0
 Edge case: 0, -1. Count: 1, Average: 0.0
 Error: only -1 or invalid. Error: no data
"""

SENTINEL_VALUE = -1

# Initialize accumulators
total_sum = 0.0
valid_count = 0

print(f"Enter numbers (>=0). Enter {SENTINEL_VALUE} to stop:")

while True:
    number_txt = input("Enter number: ").strip()
    
    try:
        number = float(number_txt)
        
        if number == SENTINEL_VALUE:
            break  # Exit loop on sentinel
        elif number < 0:
            print("Error: invalid input (negative number)")
            continue  # Reject negative, ask again
        else:
            # Valid number: accumulate
            total_sum += number
            valid_count += 1
            
    except ValueError:
        print("Error: invalid input")  # Non-numeric, ask again

# Show results only if valid data exists
if valid_count > 0:
    average = total_sum / valid_count
    print(f"Count: {valid_count}")
    print(f"Average: {average}")
else:
    print("Error: no data")

#Problem 4: Password attempts with while
"""
Problem 4: Password attempts with while
Description: 
 Simple password attempt system with limited tries. Uses hardcoded correct password 
 and MAX_ATTEMPTS constant. Success grants access; exhausting attempts locks account.

Inputs:
 user_password (string): password attempts from user

Outputs:
 "Login success" on correct password
 "Account locked" after max attempts

Validations:
 MAX_ATTEMPTS constant > 0 (set to 3)
 Exact string match (case sensitive)
 Proper attempt counting

Test cases:
 Normal: password="admin123" (1st try). Login success
 Edge case: correct on 3rd try.  Login success  
 Error: 3 wrong passwords.  Account locked
"""

MAX_ATTEMPTS = 3
CORRECT_PASSWORD = "angel2330281"

attempts = 0

print(f"You have {MAX_ATTEMPTS} attempts to enter the password.")

while attempts < MAX_ATTEMPTS:
    user_attempt = input("Enter password: ").strip()
    attempts += 1
    
    if user_attempt == CORRECT_PASSWORD:
        print("Login success")
        break  # Exit on success
    else:
        remaining = MAX_ATTEMPTS - attempts
        if remaining > 0:
            print(f"Wrong password. {remaining} attempts remaining.")
        else:
            print("Account locked")

#Problem 5: Simple menu with while
"""
Problem 5: Simple menu with while
Description: 
 Interactive text menu that loops until user selects exit (0). Supports greeting, 
 counter display, and counter increment. Invalid options are rejected and menu 
 repeats until valid exit choice.

Inputs:
 option (string/int): user menu selection (0,1,2,3)

Outputs:
 "Hello!" (option 1)
 "Counter: <value>" (option 2) 
 "Counter incremented" (option 3)
 "Bye!" (option 0)
 "Error: invalid option" for others

Validations:
 option must convert to int 0-3
 Invalid inputs repeat menu loop

Test cases:
 Normal: 1. Hello!, 2. Counter:0, 3. Counter incremented, 0. Bye!
 Edge case: immediate 0. Bye!
 Error: "letras". Error: invalid option (menu continues)
"""

counter = 0
option = -1  # Initial value as suggested

print("Menu:")
print("1) Show greeting")
print("2) Show current counter value") 
print("3) Increment counter")
print("0) Exit")

while option != 0:
    option_txt = input("Select option: ").strip()
    
    try:
        option = int(option_txt)
        
        if option == 1:
            print("Hello!")
        elif option == 2:
            print(f"Counter: {counter}")
        elif option == 3:
            counter += 1
            print("Counter incremented")
        elif option == 0:
            print("Bye!")
            break
        else:
            print("Error: invalid option")
            
    except ValueError:
        print("Error: invalid option")

#Problem 6: Pattern printing with nested loops
"""
Problem 6: Pattern printing with nested loops
Description: 
 Uses nested for loops to print right triangle asterisk pattern. First prints 
 ascending triangle, then inverted triangle. Each row contains exactly i asterisks 
 using string accumulation in inner loop.

Inputs:
 n (int): number of rows for triangle pattern

Outputs:
 Ascending triangle pattern line by line
 Inverted triangle pattern line by line

Validations:
 n must convert to integer
 n >= 1 for meaningful pattern

Test cases:
 Normal: n=4  prints full triangle + inverted triangle
 Edge case: n=1  "*" + "*" (both patterns)
 Error: n=0 or non-numeric  Error: invalid input
"""

# Get input and validate
rows_txt = input("Enter number of rows: ").strip()

try:
    rows = int(rows_txt)
    
    if rows < 1:
        print("Error: invalid input")
    else:
        # First pattern: ascending triangle
        print("Ascending triangle:")
        for i in range(1, rows + 1):
            line = ""
            for j in range(i):
                line += "*"
            print(line)
        
        # Second pattern: inverted triangle (both patterns as bonus)
        print("Inverted triangle:")
        for i in range(rows, 0, -1):
            line = ""
            for j in range(i):
                line += "*"
            print(line)
            
except ValueError:
    print("Error: invalid input")
print("end of homework 2") 



