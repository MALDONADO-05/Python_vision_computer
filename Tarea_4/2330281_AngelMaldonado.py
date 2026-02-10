#Problem 1: Temperature converter and range flag
"""
Problem 1: Temperature converter and range flag
Description: 
 Converts Celsius temperature to Fahrenheit and Kelvin scales using standard 
 formulas. Also sets boolean flag indicating high temperature condition (>= 30°C).

Inputs:
 temp_c (float): temperature in Celsius

Outputs:
 "Fahrenheit: <temp_f>"
 "Kelvin: <temp_k>"
 "High temperature: True|False"

Validations:
 Input must convert to float
 temp_c >= -273.15°C (absolute zero limit)

Test cases:
 Normal: 25.0 Fahrenheit: 77.0, Kelvin: 298.15, High temperature: False
 Edge case: 30.0 Fahrenheit: 86.0, Kelvin: 303.15, High temperature: True
 Error: -300.0 Error: invalid input
"""

temp_c_txt = input("Enter temperature in Celsius: ").strip()

try:
    temp_c = float(temp_c_txt)
    
    if temp_c < -273.15:
        print("Error: invalid input")
    else:
        # Convert to Fahrenheit and Kelvin
        temp_f = temp_c * 9 / 5 + 32
        temp_k = temp_c + 273.15
        
        # Check high temperature condition
        is_high_temp = temp_c >= 30.0
        
        print(f"Fahrenheit: {temp_f}")
        print(f"Kelvin: {temp_k}")
        print(f"High temperature: {is_high_temp}")
        
except ValueError:
    print("Error: invalid input")

#Problem 2: Work hours and overtime payment
"""
Problem 2: Work hours and overtime payment
Description: 
 Calculates weekly worker payment splitting regular hours (≤40) at normal rate 
 and overtime hours (>40) at 150% rate. Determines boolean flag for overtime work.

Inputs:
 hours_worked (int): total weekly hours
 hourly_rate (float): payment per regular hour

Outputs:
 "Regular pay: <amount>"
 "Overtime pay: <amount>" 
 "Total pay: <total>"
 "Has overtime: True|False"

Validations:
 hours_worked >= 0
 hourly_rate > 0

Test cases:
 Normal: 45, 20.0  Regular: 800.0, Overtime: 150.0, Total: 950.0, Has overtime: True
 Edge case: 40, 15.0  Regular: 600.0, Overtime: 0.0, Total: 600.0, Has overtime: False
 Error: -5, 10.0  Error: invalid input
"""

hours_txt = input("Enter weekly hours: ").strip()
rate_txt = input("Enter hourly rate: ").strip()

try:
    hours_worked = int(hours_txt)
    hourly_rate = float(rate_txt)
    
    if hours_worked < 0 or hourly_rate <= 0:
        print("Error: invalid input")
    else:
        # Calculate regular and overtime hours
        regular_hours = min(hours_worked, 40)
        overtime_hours = max(hours_worked - 40, 0)
        
        # Compute payments
        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * 1.5
        total_pay = regular_pay + overtime_pay
        
        # Overtime flag
        has_overtime = hours_worked > 40
        
        print(f"Regular pay: {regular_pay}")
        print(f"Overtime pay: {overtime_pay}")
        print(f"Total pay: {total_pay}")
        print(f"Has overtime: {has_overtime}")
        
except ValueError:
    print("Error: invalid input")

#Problem 3: Discount eligibility with booleans
"""
Problem 3: Discount eligibility with booleans
Description: 
 Determines customer discount eligibility using boolean logic (student OR senior OR 
 large purchase). Applies 10% discount to eligible purchases and shows final total.

Inputs:
 purchase_total (float): purchase amount
 is_student_text (string): "YES" or "NO" 
 is_senior_text (string): "YES" or "NO"

Outputs:
 "Discount eligible: True|False"
 "Final total: <amount>"

Validations:
 purchase_total >= 0.0
 is_student_text/is_senior_text must be exactly "YES" or "NO"

Test cases:
 Normal: 1200.0, "YES", "NO". Discount eligible: True, Final total: 1080.0
 Edge case: 500.0, "NO", "YES". Discount eligible: True, Final total: 500.0
 Error: 100.0, "abc", "NO". Error: invalid input
"""

total_txt = input("Enter purchase total: ").strip()
student_txt = input("Are you student? (YES/NO): ").strip().upper()
senior_txt = input("Are you senior? (YES/NO): ").strip().upper()

try:
    purchase_total = float(total_txt)
    
    if purchase_total < 0:
        print("Error: invalid input")
    elif student_txt not in ["YES", "NO"] or senior_txt not in ["YES", "NO"]:
        print("Error: invalid input")
    else:
        # Convert to booleans
        is_student = student_txt == "YES"
        is_senior = senior_txt == "YES"
        
        # Check eligibility with OR logic
        discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)
        
        # Calculate final total
        final_total = purchase_total * 0.9 if discount_eligible else purchase_total
        
        print(f"Discount eligible: {discount_eligible}")
        print(f"Final total: {final_total}")
        
except ValueError:
    print("Error: invalid input")

#Problem 4: Basic statistics of three integers
"""
Problem 4: Basic statistics of three integers
Description: 
 Processes three integer inputs computing sum, average, extremes (max/min), 
 and boolean flag indicating all numbers are even using arithmetic and logical operations.

Inputs:
 n1 (int): first integer
 n2 (int): second integer  
 n3 (int): third integer

Outputs:
 "Sum: <total>"
 "Average: <avg>"
 "Max: <maximum>"
 "Min: <minimum>"
 "All even: True|False"

Validations:
 All three inputs must convert to integers
 Negative numbers allowed

Test cases:
 Normal: 2, 4, 6. Sum: 12, Average: 4.0, Max: 6, Min: 2, All even: True
 Edge case: 1, 1, 1. Sum: 3, Average: 1.0, Max: 1, Min: 1, All even: False
 Error: "abc", 2, 3. Error: invalid input
"""

num1_txt = input("Enter first number: ").strip()
num2_txt = input("Enter second number: ").strip()
num3_txt = input("Enter third number: ").strip()

try:
    n1 = int(num1_txt)
    n2 = int(num2_txt)
    n3 = int(num3_txt)
    
    # Calculate statistics
    total_sum = n1 + n2 + n3
    average_value = total_sum / 3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    
    # Check if all numbers are even
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)
    
    print(f"Sum: {total_sum}")
    print(f"Average: {average_value}")
    print(f"Max: {max_value}")
    print(f"Min: {min_value}")
    print(f"All even: {all_even}")
    
except ValueError:
    print("Error: invalid input")

#Problem 5: Loan eligibility (income and debt ratio)
"""
Problem 5: Loan eligibility (income and debt ratio)
Description: 
 Evaluates loan eligibility using income threshold, debt-to-income ratio, 
 and minimum credit score requirements. Calculates debt ratio and applies 
 all three conditions with AND logical operator.

Inputs:
 monthly_income (float): monthly earnings
 monthly_debt (float): monthly debt payments
 credit_score (int): credit rating score

Outputs:
 "Debt ratio: <ratio>"
 "Eligible: True|False"

Validations:
 monthly_income > 0.0 (avoid division by zero)
 monthly_debt >= 0.0
 credit_score >= 0

Test cases:
 Normal: 10000.0, 3000.0, 700. Debt ratio: 0.3, Eligible: True
 Edge case: 8000.0, 3200.0, 650. Debt ratio: 0.4, Eligible: True
 Error: 5000.0, 1000.0, 700. Debt ratio: 0.2, Eligible: False
"""

income_txt = input("Enter monthly income: ").strip()
debt_txt = input("Enter monthly debt: ").strip()
score_txt = input("Enter credit score: ").strip()

try:
    monthly_income = float(income_txt)
    monthly_debt = float(debt_txt)
    credit_score = int(score_txt)
    
    if monthly_income <= 0 or monthly_debt < 0 or credit_score < 0:
        print("Error: invalid input")
    else:
        # Calculate debt ratio
        debt_ratio = monthly_debt / monthly_income
        
        # Check all eligibility conditions
        eligible = (monthly_income >= 8000.0 and 
                   debt_ratio <= 0.4 and 
                   credit_score >= 650)
        
        print(f"Debt ratio: {debt_ratio}")
        print(f"Eligible: {eligible}")
        
except ValueError:
    print("Error: invalid input")

#
"""
Problem 6: Body Mass Index (BMI) and category flag
Description: 
 Calculates Body Mass Index using weight and height data. Determines three 
 mutually exclusive boolean categories: underweight, normal, overweight based 
 on standard BMI ranges with rounded display value.

Inputs:
 weight_kg (float): body weight in kilograms
 height_m (float): height in meters

Outputs:
 "BMI: <bmi_rounded>"
 "Underweight: True|False"
 "Normal: True|False" 
 "Overweight: True|False"

Validations:
 weight_kg > 0.0
 height_m > 0.0

Test cases:
 Normal: 70.0, 1.75. BMI: 22.86, Normal: True
 Edge case: 50.0, 1.60. BMI: 19.53, Normal: True
 Error: 0.0, 1.70. Error: invalid input
"""

weight_txt = input("Enter weight (kg): ").strip()
height_txt = input("Enter height (m): ").strip()

try:
    weight_kg = float(weight_txt)
    height_m = float(height_txt)
    
    if weight_kg <= 0 or height_m <= 0:
        print("Error: invalid input")
    else:
        # Calculate BMI
        bmi = weight_kg / (height_m * height_m)
        bmi_rounded = round(bmi, 2)
        
        # Determine BMI categories (mutually exclusive)
        is_underweight = bmi < 18.5
        is_normal = 18.5 <= bmi < 25.0
        is_overweight = bmi >= 25.0
        
        print(f"BMI: {bmi_rounded}")
        print(f"Underweight: {is_underweight}")
        print(f"Normal: {is_normal}")
        print(f"Overweight: {is_overweight}")
        
except ValueError:
    print("Error: invalid input")
    
    print("end of homework 4") 



