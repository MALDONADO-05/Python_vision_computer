#Problem 1 "Rectagle area and perimeter"
"""
Description:
 This program establishes two functions to calculate the area and perimeter of a rectangle. 
 Within the code, the following parameters are read: width and height entered by the user, validated, 
 called the functions, and displayed the results if valid, or an error message if not.

Inputs:
 width (float): only positive value for rectangle width
 height (float): only positive value for rectangle height

Outputs:
 "Area: <area_value>" if valid
 "Perimeter: <perimeter_value>" if valid
 "Error: invalid input" if invalid (non-numeric or <=0)

Validations:
 Inputs must be convertible to float
 width > 0 and height > 0
 Validate before calling functions

Test cases:
 Normal: width=5.0, height=6.0 → Area: 30.0, Perimeter: 22.0
 Edge case: width=0.001, height=0.001 → Area: 0.000001, Perimeter: 0.004
 Error: width="0" or width=-56 → Error: invalid input
 """

def calculate_area(width, height):
       return width * height  
"""
 Calculate the area of ​​a rectangle.
 Parameter: width of the rectangle (float).
 Parameter: height of the rectangle (float).
 Return: area value.
 """

def calculate_perimeter(width, height):
       
    return 2 * (width + height) 
"""
 Calculates the perimeter of a rectangle.
 Parameter: rectangle width (floating value).
 Parameter: rectangle height (floating value).
 Performs the multiplication of the width and height values ​​by 2.
 Returns: perimeter value. """  
#code
width_txt = input("enter a number for base: ")
height_txt = input("enter a number for height: ")

try:
    width = float(width_txt)
    height = float(height_txt)

    if width <= 0 or height <= 0:
            print("Error: invalid input")
    else:
            area = calculate_area(width, height)
            perimeter = calculate_perimeter(width, height)
            print(f"Area: {area}")
            print(f"Perimeter: {perimeter}")
    
    print("complete calculation :D")

except  ValueError:
    print("invalid data for height or base")


#Problem 2: Grade classifier 
"""
Problem 2: Grade classifier (function with return string)
Description:
 This program defines a function `classify_grade(score)` that receives a numerical grade (0–100)
 and returns the corresponding category: A (>=90), B (80–89), C (70–79), D (60–69), F (<60).
 The main code reads the grade, validates it, and displays the result if it is valid.


Inputs:
 score (float or int): numeric grade between 0 and 100

Outputs:
 "Score: <score_value>"
 "Category: <grade_letter>" if valid
 "Error: invalid input" if invalid (outside of 0-100 or non-numeric)

Validations:
 score must be numeric and convertible to a float
 0 <= score <= 100
 Validate before calling the function

Test cases:
 Normal: score = 78 Score: 78.0, category: C
 Borderline case: score = 0 Score: 0.0 category: F
 Error: score = 150 or score = "abc" Error: invalid input
"""

def classify_grade(score):
    
    """Classifies a grade into a letter category.
    For score: float or int, grade (0-100)
    Return: str, category ('A', 'B', 'C', 'D', or 'F')
    """
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

# code
score_txt = input("Enter a score (0-100): ") 
try:
        score = float(score_txt)
        
        if score < 0 or score > 100:
            print("Error: invalid input")
        else:
            category = classify_grade(score)
            print(f"Score: {score}")
            print(f"Category: {category}")
            
except ValueError:
        print("Error: invalid input")

#Problem 3: List statistics function (min, max, average)
"""
Descripción: 
This program defines a function summarize_numbers(numbers_list) that receives a list of numbers and returns a dictionary with the minimum, maximum, and average values.
It reads numbers separated by commas to build the list, validates it, and displays the results.

Inputs:
 numbers_text (string): comma-separated numbers, e.g., "10,20,30"
 numbers_list (list): list of float/int values ​​internally

Outputs:
 "Min: <min_value>"
 "Max: <max_value>"
 "Average: <average_value>"
 "Error: invalid input" if it fails

Validations:
 numbers_text not empty after strip()
 List not empty after conversion
 All elements convertible to float
 Validate before calling the function

Test cases:
 Normal: "10,20,30" Min: 10.0, Max: 30.0, Average: 20.0
 Borderline case: "5" Min: 5.0, Max: 5.0, Average: 5.0
 Error: "" or "10,abc,30" Error: invalid input"""

def summarize_numbers(numbers_list):
    """
    Summarizes a list of numbers with min, max, and average.
    param numbers_list: list of float/int numbers
    return: dict with 'min', 'max', 'average' keys
    """
    
    min_value = min(numbers_list)
    max_value = max(numbers_list)
    average_value = sum(numbers_list) / len(numbers_list)
    return {
        "min": min_value,
        "max": max_value,
        "average": average_value
    }

# code 
numbers_text = input("Enter numbers separated by commas: ").strip()
    
if not numbers_text:
        print("Error: invalid input")
else:
         try:
            # Convertir string a lista de floats
            numbers_str_list = numbers_text.split(',')
            numbers_list = []
            
            for num_str in numbers_str_list:
                num_str_stripped = num_str.strip()
                if not num_str_stripped:
                    raise ValueError("empty number")
                numbers_list.append(float(num_str_stripped))
            
            if not numbers_list:
                print("Error: invalid input")
            else:
                # Llamar función solo si todo es válido
                summary = summarize_numbers(numbers_list)
                print(f"Min: {summary['min']}")
                print(f"Max: {summary['max']}")
                print(f"Average: {summary['average']}")
         except ValueError:
             print("Error: invalid input")

#Problem 4: Apply Discount to List (Pure Function = Do Not Modify Input)
"""
Description: 
 This program defines a function `apply_discount(prices_list, discount_rate)` that receives a list of 
 prices and a discount rate, and returns a new list with discounted prices (without modifying the original). 
 The code creates lists from text, validates them, and displays both lists.

Inputs:
 prices_text (string): prices separated by commas, e.g., "100,200,300"
 discount_rate (float): discount rate, values ​​between 0 and 1 (e.g., 0.10 = 10%)

Outputs:
 "Original prices: <original_list>"
 "Discounted prices: <discount_list>"
 "Error: invalid input" in case of failure

Validations:
 prices_text not empty and list not empty
 All prices > 0
 0 <= discount_rate <= 1
 Validate BEFORE Calling a function

Test cases:
 Normal: "100,200,300", 0.10. Original: [100.0, 200.0, 300.0], Discounted: [90.0, 180.0, 270.0]
 Edge case: "50", 0.0. Original: [50.0], Discounted: [50.0]
 Error: "100,-50", 1.5 or "".  Error: invalid input
"""

def apply_discount(prices_list, discount_rate):
    """
    Applies discount to prices list creating a new list (pure function).
    param prices_list: list of float prices (>0)
    param discount_rate: float discount rate (0-1)
    return: list of discounted prices (new list)
    """
    discounted_prices = []
    for price in prices_list:
        discounted_price = price * (1 - discount_rate)
        discounted_prices.append(discounted_price)
    return discounted_prices

# Códe
prices_text = input("Enter prices separated by commas: ").strip()
discount_rate_txt = input("Enter discount rate (0-1): ").strip()

try:
    # Convert discount rate
    discount_rate = float(discount_rate_txt)
    
    # Validate rate
    if discount_rate < 0 or discount_rate > 1:
        print("Error: invalid input")
    else:
        # Build price list
        prices_str_list = prices_text.split(',')
        prices_list = []
        
        if not prices_text:
            print("Error: invalid input")
        else:
            # Convert and validate each price
            for price_str in prices_str_list:
                price_str_stripped = price_str.strip()
                if not price_str_stripped:
                    raise ValueError("empty price")
                price = float(price_str_stripped)
                if price <= 0:
                    raise ValueError("negative price")
                prices_list.append(price)
            
            if not prices_list:
                print("Error: invalid input")
            else:
                # Create discounted list (without modifying the original)
                discounted_prices = apply_discount(prices_list, discount_rate)
                
                # Show results
                print(f"Original prices: {prices_list}")
                print(f"Discounted prices: {discounted_prices}")
                
except ValueError:
    print("Error: invalid input")
#Problem 5: Greeting function with default parameters
"""
Problem 5: Greeting function with default parameters
Descripción: 
Program implementing greet(name, title="") to create personalized greetings. 
Places title before name if provided; otherwise uses name only. 
Tests both positional and named arguments with prior validation.

Inputs:
- name (string): required user name
- title (string optional): professional prefix like "Dr.", "Eng."

Outputs:
- "Greeting: Hello, <full_name>!"
- "Error: invalid input" when name is empty

Validations:
- Check name has content after strip()
- title cleaned with strip() but optional

Test cases:
 Normal: name="Alice", title="Dr.". Greeting: Hello, Dr. Alice!
 Edge case: name="Bob", title="".  Greeting: Hello, Bob!
 Error: name="". Error: invalid input
"""

def greet(name, title=""):
    """
    Creates a greeting message with optional title.
     param name: str, person's name (required)
     param title: str, optional title prefix (default empty)
     return: str, formatted greeting message
    """
    if title.strip():
        full_name = f"{title.strip()} {name.strip()}"
    else:
        full_name = name.strip()
    return f"Hello, {full_name}!"

# Códe
name = input("Enter name: ").strip()
title = input("Enter title (optional): ").strip()

if not name:
    print("Error: invalid input")
else:
    # Try using named arguments
    greeting = greet(name=name, title=title)
    print(f"Greeting: {greeting}")

#Problem 6: Factorial function (iterative implementation)
"""
Problem 6: Factorial function (iterative implementation)
Description: 
Program defining factorial(n) function using iterative approach (for loop) for efficiency 
and to avoid recursion depth issues. Main code reads n, validates it, calls the function, 
and displays the factorial result.

Inputs:
 n (int): non-negative integer for factorial calculation

Outputs:
 "n: <n_value>"
 "Factorial: <factorial_value>"
 "Error: invalid input" for invalid cases

Validations:
 n must be integer and convertible from input
 0 <= n <= 20 (reasonable limit for manageable results)
 Check before calling factorial function

Test cases:
 Normal: n=5 → n: 5, Factorial: 120
 Edge case: n=0 → n: 0, Factorial: 1
 Error: n=-1 or n=25 or "ght" → Error: invalid input
"""

def factorial(n):
    """
    Calculates factorial of n using iterative approach.
    Chosen iterative over recursive for better performance and no stack overflow risk.
     param n: int, non-negative integer
     return: int, n! (factorial value)
    """
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Main code
n_txt = input("Enter a non-negative integer (0-20): ").strip()

try:
    n = int(n_txt)
    
    if n < 0 or n > 20:
        print("Error: invalid input")
    else:
        fact_value = factorial(n)
        print(f"n: {n}")
        print(f"Factorial: {fact_value}")
        
except ValueError:
    print("Error: invalid input")
print("end of homework 1")    