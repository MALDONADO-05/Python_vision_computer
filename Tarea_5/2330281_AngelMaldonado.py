#Problem 1: Shopping list basics (list operations)
"""
Problem 1: Shopping list basics (list operations)
Description: 
 Creates shopping list from initial items string with quantities, adds new items, 
 counts total elements, and searches for specific products using list methods 
 with case-insensitive normalization.

Inputs:
 initial_items_text (string): "apple:2,banana:5,orange:6" format
 new_item (string): product to add to list
 search_item (string): product to search

Outputs:
 "Items list: <list>"
 "Total items: <count>"
 "Found item: True|False"

Validations:
 initial_items_text not empty after strip()
 new_item and search_item not empty
 Parse format correctly from string input

Test cases:
 Normal: "apple:2,banana:5", "orange", "banana". Items: ['apple', 'banana', 'orange'], Total: 3, Found: True
 Edge case: "", "milk", "milk". Items: ['milk'], Total: 1, Found: True
 Error: "abc", "", "xyz". Error: invalid input
"""

initial_text = input("Enter initial items (item:qty,...): ").strip()
new_item_input = input("Enter new item: ").strip()
search_item = input("Enter item to search: ").strip()

if not initial_text or not new_item_input or not search_item:
    print("Error: invalid input")
else:
    # Parse initial items (take only product names, ignore quantities)
    shopping_list = []
    if initial_text != "":
        item_pairs = initial_text.split(',')
        for pair in item_pairs:
            pair = pair.strip()
            if ':' in pair:
                product_name = pair.split(':')[0].strip().lower()
                shopping_list.append(product_name)
    
    # Add new item (normalized)
    shopping_list.append(new_item_input.lower())
    
    # Search (case insensitive)
    is_in_list = search_item.lower() in shopping_list
    
    print(f"Items list: {shopping_list}")
    print(f"Total items: {len(shopping_list)}")
    print(f"Found item: {is_in_list}")

#Problem 2: Points and distances with tuples
"""
Problem 2: Points and distances with tuples
Description: 
 Uses tuples to represent 2D coordinates for two points. Calculates Euclidean 
 distance between points and creates midpoint tuple using coordinate arithmetic 
 with tuple unpacking for clear 2D point representation.

Inputs:
 x1, y1 (float): coordinates for point A
 x2, y2 (float): coordinates for point B

Outputs:
 "Point A: (x1, y1)"
 "Point B: (x2, y2)"
 "Distance: <distance>"
 "Midpoint: (mx, my)"

Validations:
 All 4 coordinates must convert to float

Test cases:
 Normal: 0.0, 0.0, 3.0, 4.0  Distance: 5.0, Midpoint: (1.5, 2.0)
 Edge case: 1.0, 1.0, 1.0, 1.0  Distance: 0.0, Midpoint: (1.0, 1.0)
 Error: "abc", 1.0, 2.0, 3.0  Error: invalid input
"""

x1_txt = input("Enter x1 coordinate: ").strip()
y1_txt = input("Enter y1 coordinate: ").strip()
x2_txt = input("Enter x2 coordinate: ").strip()
y2_txt = input("Enter y2 coordinate: ").strip()

try:
    x1 = float(x1_txt)
    y1 = float(y1_txt)
    x2 = float(x2_txt)
    y2 = float(y2_txt)
    
    # Create coordinate tuples (immutable points)
    point_a = (x1, y1)
    point_b = (x2, y2)
    
    # Calculate Euclidean distance
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    
    # Calculate midpoint tuple
    midpoint = ((x1 + x2) / 2, (y1 + y2) / 2)
    
    print(f"Point A: {point_a}")
    print(f"Point B: {point_b}")
    print(f"Distance: {distance}")
    print(f"Midpoint: {midpoint}")
    
except ValueError:
    print("Error: invalid input")

#Problem 3: Product catalog with dictionary
"""
Problem 3: Product catalog with dictionary
Description: 
 Manages product catalog using dictionary with product names as keys and prices 
 as values. Calculates purchase total when product exists, handles missing products 
 with normalized case-insensitive lookup.

Inputs:
 product_name (string): product to purchase
 quantity (int): units to buy

Outputs:
 "Unit price: <price>" (if found)
 "Quantity: <qty>"
 "Total: <total>"
 "Error: product not found" (if missing)

Validations:
 quantity > 0
 product_name not empty after strip()
 product must exist as dictionary key

Test cases:
 Normal: "apple", 3.  Unit price: 10.0, Quantity: 3, Total: 30.0
 Edge case: "Apple", 1.  Unit price: 10.0, Quantity: 1, Total: 10.0  
 Error: "xyz", 2. Error: product not found
"""

# Initialize product catalog dictionary
product_prices = {
    "apple": 10.0,
    "banana": 5.0,
    "orange": 8.0
}

product_input = input("Enter product name: ").strip().lower()
quantity_txt = input("Enter quantity: ").strip()

if not product_input:
    print("Error: invalid input")
else:
    try:
        quantity = int(quantity_txt)
        
        if quantity <= 0:
            print("Error: invalid input")
        elif product_input in product_prices:
            unit_price = product_prices[product_input]
            total_price = unit_price * quantity
            
            print(f"Unit price: {unit_price}")
            print(f"Quantity: {quantity}")
            print(f"Total: {total_price}")
        else:
            print("Error: product not found")
            
    except ValueError:
        print("Error: invalid input")

#Problem 4: Student grades with dict and list
"""
Problem 4: Student grades with dict and list
Description: 
 Manages student grades using dictionary where keys are student names and values 
 are lists of float grades. Calculates average grade and determines pass/fail status 
 for specified student using list sum and length operations.

Inputs:
 student_name (string): name of student to query

Outputs:
 "Grades: <grades_list>" (if found)
 "Average: <average>"
 "Passed: True|False"
 "Error: student not found" (if missing)

Validations:
 student_name not empty after strip()
 Student must exist as dictionary key
 Grades list must not be empty for average calculation

Test cases:
 Normal: "Alice". Grades: [90.0, 85.0, 88.0], Average: 87.67, Passed: True
 Edge case: "Bob". Grades: [70.0], Average: 70.0, Passed: True
 Error: "xyz". Error: student not found
"""

# Student grades dictionary (name -> list of grades)
student_grades = {
    "Alice": [90.0, 85.0, 88.0],
    "Bob": [70.0],
    "Charly": [45.0, 60.0, 55.0]
}

name_input = input("Enter student name: ").strip()

if not name_input:
    print("Error: invalid input")
elif name_input in student_grades:
    grades_list = student_grades[name_input]
    
    if len(grades_list) == 0:
        print("Error: invalid input")
    else:
        # Calculate average using sum and length
        average_grade = sum(grades_list) / len(grades_list)
        
        # Check pass status (average >= 70.0)
        is_passed = average_grade >= 70.0
        
        print(f"Grades: {grades_list}")
        print(f"Average: {average_grade}")
        print(f"Passed: {is_passed}")
else:
    print("Error: student not found")

#Problem 5: Word frequency counter (list + dict)
"""
Problem 5: Word frequency counter (list + dict)
Description: 
 Analyzes sentence by creating word list after cleaning punctuation and case, 
 then builds frequency dictionary by iterating through words. Identifies most 
 common word through manual dictionary value comparison.

Inputs:
 sentence (string): text containing multiple words

Outputs:
 "Words list: <word_list>"
 "Frequencies: <frequency_dict>"
 "Most common word: <word>"

Validations:
 sentence not empty after strip()
 Resulting word list not empty after processing
 Basic punctuation removal (. , ! ? ;)

Test cases:
 Normal: "Hello world. Hello Python!". Words: ['hello', 'world', 'hello', 'python'], Most common: hello
 Edge case: "a b a".  Words: ['a', 'b', 'a'], Most common: a
 Error: "".  Error: invalid input
"""

sentence_input = input("Enter sentence: ").strip()

if not sentence_input:
    print("Error: invalid input")
else:
    # Clean punctuation and normalize case
    cleaned = sentence_input.lower()
    for punct in ".,!?;:":
        cleaned = cleaned.replace(punct, "")
    
    # Create word list
    words_list = cleaned.split()
    
    if len(words_list) == 0:
        print("Error: invalid input")
    else:
        # Build frequency dictionary
        word_freq = {}
        for word in words_list:
            if word in word_freq:
                word_freq[word] += 1
            else:
                word_freq[word] = 1
        
        # Find most common word
        most_common = ""
        max_count = 0
        for word, count in word_freq.items():
            if count > max_count:
                max_count = count
                most_common = word
        
        print(f"Words list: {words_list}")
        print(f"Frequencies: {word_freq}")
        print(f"Most common word: {most_common}")

#
"""
Problem 6: Simple address book (dictionary CRUD)
Description: 
 Implements basic address book CRUD operations (Create/Read/Update/Delete) using 
 dictionary with normalized contact names and phone numbers. Supports ADD, SEARCH, 
 DELETE actions with proper validation and feedback messages.

Inputs:
 action_text (string): "ADD", "SEARCH", or "DELETE"
 name (string): contact name
 phone (string): phone number (ADD only)

Outputs:
 ADD: "Contact saved: <name> <phone>"
 SEARCH: "Phone: <number>" or "Error: contact not found"
 DELETE: "Contact deleted: <name>" or "Error: contact not found"

Validations:
 action_text must be ADD/SEARCH/DELETE (case insensitive)
 name and phone not empty after strip()
 Name normalized with .title()

Test cases:
 Normal: "ADD", "Alice", "1234567890". Contact saved: Alice 1234567890
 Edge case: "SEARCH", "Bob". Phone: 555-1234
 Error: "XYZ", "John", "". Error: invalid input
"""

# Initial address book
contacts = {
    "Alice": "834-456-7890",
    "Bob": "834-1234",
    "Carol": "834-654-3210"
}

action_input = input("Enter action (ADD/SEARCH/DELETE): ").strip().upper()
contact_name = input("Enter contact name: ").strip().title()

# Validate action
if action_input not in ["ADD", "SEARCH", "DELETE"]:
    print("Error: invalid input")
elif not contact_name:
    print("Error: invalid input")
else:
    if action_input == "ADD":
        phone_number = input("Enter phone number: ").strip()
        
        if not phone_number:
            print("Error: invalid input")
        else:
            contacts[contact_name] = phone_number
            print(f"Contact saved: {contact_name} {phone_number}")
            
    elif action_input == "SEARCH":
        if contact_name in contacts:
            print(f"Phone: {contacts[contact_name]}")
        else:
            print("Error: contact not found")
            
    else:  # DELETE
        if contact_name in contacts:
            del contacts[contact_name]
            print(f"Contact deleted: {contact_name}")
        else:
            print("Error: contact not found")

print("end of homework 5") 


