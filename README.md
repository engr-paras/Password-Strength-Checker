
# Simple Password Strength Checker with Retry

A Python-based simple password strength checker that evaluates the strength of a password based on key criteria such as length, use of uppercase & lowercase letters, numbers, and special characters. The program provides a retry mechanism for the user to enter a stronger password if the current one is weak.

## ✅ Features

- Checks for:
  - Minimum length (8 characters)
  - Presence of lowercase letters
  - Presence of uppercase letters
  - Inclusion of digits
  - Special characters (from: `@#$%^&*!?`)
- Interactive input with real-time feedback
- Provides strength classification:
  - Very Strong
  - Strong
  - Okay
  - Weak
  - Very Weak (prompts retry)

## 🚀 How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Password-Strength-Checker.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Password-Strength-Checker
   ```

3. Run the script:
   ```bash
   python password_strength_checker.py
   ```

4. Enter your password when prompted. The program will provide strength feedback and allow retries if the password is weak.

## ⚡ Example Output

```bash
Enter a password: test123
Very Weak, please try a stronger password!

Enter a password: Test123@
Strong
```

## 📚 Technologies Used

- Python 3
- Simple standard input/output

## 📂 Repository Structure

```
├── password_strength_checker.py
├── README.md
```

## 🎯 License

This project is open-source and free to use under the MIT License.

---

🔒 Secure your applications by encouraging strong password usage!
