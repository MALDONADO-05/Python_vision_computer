#Problem 1: Full name formatter (name + initials)
"""
Problem 1: Full name formatter (name + initials)
Description: 
 Processes full name input by cleaning extra spaces, converting to title case, 
 and extracting initials from each word. Displays formatted name and initials pattern.

Inputs:
 full_name (string): complete name possibly with extra spaces/mixed case

Outputs:
 "Formatted name: <Title Case Name>"
 "Initials: <X.X.X.>"

Validation:
 full_name not empty after strip()
 Must contain at least 2 words (name + surname minimum)
 Reject strings that are only whitespace

Test cases:
 Normal: "juan pedro maldonado". Formatted name: Juan Carlos Tovar, Initials: J.P.M.
 Edge case: "ana maria".  Formatted name: Ana Maria, Initials: A.M.
 Error: "" or "john".  Error: invalid input
"""

# Get and clean input
name_input = input("Enter full name: ").strip()

if not name_input or name_input.isspace():
    print("Error: invalid input")
else:
    # Split into words and validate minimum words
    words = name_input.split()
    
    if len(words) < 2:
        print("Error: invalid input")
    else:
        # Format to title case
        formatted_name = " ".join(word.title() for word in words)
        
        # Extract initials
        initials = ".".join(word[0].upper() for word in words)
        
        print(f"Formatted name: {formatted_name}")
        print(f"Initials: {initials}")
    
#Problem 2: Simple email validator (structure + domain)
"""
Problem 2: Simple email validator (structure + domain)
Description: 
 Basic email format checker that verifies single '@' symbol, dot after '@', 
 and no spaces. Extracts domain when valid using string position methods.

Inputs:
 email_text (string): email address to validate

Outputs:
 "Valid email: True/False"
 "Domain: <domain>" if valid

Validation:
 email not empty after strip()
 Exactly one '@' symbol
 Contains '.' after '@' position
 No spaces anywhere

Test cases:
 Normal: "user@example.com". Valid email: True, Domain: example.com
 Edge case: "a@b.c". Valid email: True, Domain: b.c
 Error: "user@domain". Valid email: False
"""

email_input = input("Enter email: ").strip()

if not email_input:
    print("Valid email: False")
else:
    # Count '@' symbols and check spaces
    at_count = email_input.count('@')
    has_spaces = ' ' in email_input
    
    if at_count != 1 or has_spaces:
        print("Valid email: False")
    else:
        # Find '@' position and check for dot after
        at_position = email_input.find('@')
        domain_part = email_input[at_position + 1:]
        
        if '.' in domain_part:
            print("Valid email: True")
            print(f"Domain: {domain_part}")
        else:
            print("Valid email: False")

#Problem 3: Palindrome checker (ignoring spaces and case)
"""
Problem 3: Palindrome checker (ignoring spaces and case)
Description: 
 Checks if phrase reads same forward and backward after removing spaces 
 and converting to lowercase. Compares cleaned original with its reverse.

Inputs:
 phrase (string): text to test for palindrome property

Outputs:
 "Is palindrome: true/false"

Validation:
 phrase not empty after strip()
 At least 3 characters after space removal

Test cases:
 Normal: "Anita lava la tina". Is palindrome: true
 Edge case: "A". Is palindrome: false (too short)
 Error: "". Is palindrome: false
"""

phrase_input = input("Enter phrase: ").strip()

if not phrase_input:
    print("Is palindrome: false")
else:
    # Clean: lowercase + remove spaces
    cleaned_phrase = phrase_input.lower().replace(" ", "")
    
    # Validate minimum length after cleaning
    if len(cleaned_phrase) < 3:
        print("Is palindrome: false")
    else:
        # Check palindrome: original == reverse
        is_palindrome = cleaned_phrase == cleaned_phrase[::-1]
        print(f"Is palindrome: {str(is_palindrome).lower()}")

#Problem 4: Sentence word statistics (lengths and first/last word)
"""
Problem 4: Sentence word statistics (lengths and first/last word)
Description: 
 Analyzes sentence by splitting into words after cleaning whitespace. Reports total 
 word count, boundary words (first/last), and extreme length words using list iteration.

Inputs:
 sentence (string): input text containing multiple words

Outputs:
 "Word count: <n>"
 "First word: <first>"
 "Last word: <last>"
 "Shortest word: <shortest>"
 "Longest word: <longest>"

Validation:
 sentence not empty after strip()
 Contains at least one valid word after split()

Test cases:
 Normal: "Hello world python programming". Word count: 4, First: Hello, Last: programming, Shortest: python, Longest: programming
 Edge case: "a b c". Word count: 3, First: a, Last: c, Shortest: a, Longest: c  
 Error: "". Error: invalid input
"""

sentence_input = input("Enter sentence: ").strip()

if not sentence_input:
    print("Error: invalid input")
else:
    words_list = sentence_input.split()
    
    if len(words_list) == 0:
        print("Error: invalid input")
    else:
        # Basic statistics
        word_count = len(words_list)
        first_word = words_list[0]
        last_word = words_list[-1]
        
        # Find shortest and longest by iterating once
        shortest_word = words_list[0]
        longest_word = words_list[0]
        
        for word in words_list:
            if len(word) < len(shortest_word):
                shortest_word = word
            if len(word) > len(longest_word):
                longest_word = word
        
        # Display all results
        print(f"Word count: {word_count}")
        print(f"First word: {first_word}")
        print(f"Last word: {last_word}")
        print(f"Shortest word: {shortest_word}")
        print(f"Longest word: {longest_word}")

#Problem 5: Password strength classifier
"""
Problem 5: Password strength classifier
Description: 
 Evaluates password security level based on length and character variety. 
 Uses boolean flags to track presence of different character types during 
 character-by-character analysis.

Inputs:
 password_input (string): password to classify

Outputs:
 "Password strength: weak/medium/strong"

Validation:
 password not empty
 length analyzed for minimum requirements

Test cases:
 Normal: "YTH234!?". Password strength: strong
 Edge case: "password123". Password strength: medium  
 Error: "weak". Password strength: weak
"""

password_input = input("Enter password: ").strip()

if not password_input:
    print("Password strength: weak")
else:
    # Initialize character type flags
    has_upper = False
    has_lower = False
    has_digit = False
    has_symbol = False
    password_length = len(password_input)
    
    # Check each character type
    for char in password_input:
        if not has_upper and char.isupper():
            has_upper = True
        if not has_lower and char.islower():
            has_lower = True
        if not has_digit and char.isdigit():
            has_digit = True
        if not has_symbol and not char.isalnum():
            has_symbol = True
    
    # Classify strength using rules
    if (password_length >= 8 and 
        has_upper and has_lower and 
        has_digit and has_symbol):
        strength = "strong"
    elif (password_length >= 8 and 
          (has_upper or has_lower or has_digit)):
        strength = "medium"
    else:
        strength = "weak"
    
    print(f"Password strength: {strength}")

#Problem 6: Product label formatter (fixed-width text)
"""
Problem 6: Product label formatter (fixed-width text)
Description: 
 Creates fixed 30-character product label combining name and price in specific 
 format. Truncates if too long, pads with spaces if too short using string length 
 control and slicing operations.

Inputs:
 product_name (string): product name
 price_value (string/number): product price

Outputs:
 "Label: <exactly 30 characters>"

Validation:
 product_name not empty after strip()
 price_value converts to positive number

Test cases:
 Normal: "Laptop", 1299.99. Label: "Product: Laptop | Price: $1299.99     "
 Edge case: "A", 10. Label: "Product: A | Price: $10                 "
 Error: "", "JKY". Error: invalid input
"""

product_input = input("Enter product name: ").strip()
price_input = input("Enter price: ").strip()

if not product_input:
    print("Error: invalid input")
else:
    try:
        # Convert and validate price
        price_value = float(price_input)
        if price_value < 0:
            raise ValueError("negative price")
        
        # Create base label format
        price_str = f"{price_value:.2f}"
        base_label = f"Product: {product_input} | Price: ${price_str}"
        
        # Ensure exactly 30 characters
        if len(base_label) > 30:
            final_label = base_label[:30]  # Truncate
        else:
            final_label = base_label.ljust(30)  # Pad with spaces
        
        print(f"Label: '{final_label}'")
        print(f"Length: {len(final_label)}")  # Verify 30 chars
        
    except ValueError:
        print("Error: invalid input")
print("end of homework 3") 





