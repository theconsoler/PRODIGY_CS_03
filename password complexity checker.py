import re

def check_password_strength(password):
    # Criteria for password strength
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    number_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[\W_]', password))

    # Assessing strength
    criteria_met = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])
    
    if criteria_met == 5:
        strength = "Very Strong"
    elif criteria_met == 4:
        strength = "Strong"
    elif criteria_met == 3:
        strength = "Moderate"
    elif criteria_met == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    # Providing feedback
    feedback = []
    if not length_criteria:
        feedback.append("Your password should be at least 8 characters long.")
    if not uppercase_criteria:
        feedback.append("Your password should contain at least one uppercase letter.")
    if not lowercase_criteria:
        feedback.append("Your password should contain at least one lowercase letter.")
    if not number_criteria:
        feedback.append("Your password should contain at least one number.")
    if not special_char_criteria:
        feedback.append("Your password should contain at least one special character.")
    
    return strength, feedback

def main():
    while True:
        password = input("Enter a password to assess its strength: ")
        strength, feedback = check_password_strength(password)
        
        print(f"Password Strength: {strength}")
        if feedback:
            print("Feedback:")
            for suggestion in feedback:
                print(f"- {suggestion}")
        
        repeat = input("Do you want to assess another password? (yes/no): ").lower()
        if repeat != 'yes':
            break

if __name__ == "__main__":
    main()
