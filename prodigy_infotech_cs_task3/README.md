Password Complexity Checker

A simple Python program to evaluate the strength of a password based on specific criteria such as length, uppercase and lowercase letters, numbers, and special characters. It provides actionable feedback to improve password strength and allows users to check multiple passwords or exit the program.



Features

Evaluates Password Strength:
  - Classifies passwords as Weak, Moderate, or Strong.
  
Feedback and Suggestions:
  - Provides specific suggestions to improve password strength if it doesn't meet certain criteria.

Interactive:
  - Allows users to check multiple passwords in one session.

- Criteria for a Strong Password:
  1. At least 8 characters long.
  2. Contains at least one uppercase letter.
  3. Contains at least one lowercase letter.
  4. Includes at least one number.
  5. Uses at least one special character (e.g., `!@#$%^&*()`).


Getting Started

Prerequisites

- Python 3.x installed on your machine.

---

 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/password-complexity-checker.git
   cd password-complexity-checker
   ```

2. Run the script:
   ```bash
   python password_checker.py
   ```

---

Usage

1. The program will prompt you to enter a password.
2. It will evaluate the password's strength and provide suggestions if the password is not strong.
3. After each check, you can choose to evaluate another password or exit.

---

 Example

```plaintext
Enter your password: Pass123
Password Strength: Moderate
Suggestions:
- Use at least one special character (e.g., !, @, #).

Would you like to check another password? (yes/no): yes

Enter your password: StrongPass@2024
Password Strength: Strong

Would you like to check another password? (yes/no): no
Exiting. Thank you!
```

---

File Structure

```plaintext
password-complexity-checker/
│
├── password_checker.py   # Main script for password checking
├── README.md             # Documentation file
```

---

Contribution

Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-new-feature
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add a new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-new-feature
   ```
5. Open a pull request.

---

License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Acknowledgements

- Python for being an awesome programming language.
- The open-source community for inspiring the project.
