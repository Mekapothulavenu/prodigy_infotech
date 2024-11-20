def password_strength_checker(password):
    """
    Assess the strength of a password and provide feedback.

    Parameters:
        password (str): The password to be evaluated.

    Returns:
        dict: A dictionary containing the password strength and feedback.
    """
    feedback = []
    score = 0

    # Check for length
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letter
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    # Check for lowercase letter
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    # Check for digit
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Include at least one number.")

    # Check for special characters
    special_characters = "!@#$%^&*(),.?\":{}|<>"
    if any(char in special_characters for char in password):
        score += 1
    else:
        feedback.append("Use at least one special character (e.g., !, @, #).")

    # Determine password strength
    if score == 5:
        strength = "Strong"
    elif score >= 3:
        strength = "Moderate"
    else:
        strength = "Weak"

    return {
        "strength": strength,
        "feedback": feedback
    }

# Main loop for checking passwords
def main():
    while True:
        user_password = input("Enter your password: ")
        result = password_strength_checker(user_password)
        print(f"Password Strength: {result['strength']}")
        if result['feedback']:
            print("Suggestions:")
            for suggestion in result['feedback']:
                print(f"- {suggestion}")
        
        # Ask if the user wants to check another password
        choice = input("\nWould you like to check another password? (yes/no): ").strip().lower()
        if choice not in ['yes', 'y']:
            print("Exiting. Thank you!")
            break

if __name__ == "__main__":
    main()
