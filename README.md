# Password Strength Meter 🔐

A Streamlit web application that checks password strength and generates secure random passwords.

## Features ✨

- **Password Strength Analysis**:
  - Checks for minimum 8-character length
  - Verifies uppercase and lowercase letters
  - Confirms presence of numbers (0-9)
  - Validates special characters (!@#$%^&*)
  - Provides visual strength meter

- **Password Generator**:
  - Creates 14-character secure passwords
  - Guarantees all required character types
  - Uses cryptographically secure randomization

- **User-Friendly Interface**:
  - Clear success/error indicators
  - Strength score with emoji feedback
  - Copy-to-clipboard functionality

## How It Works 🛠️

### Password Checking Logic
1. **Length Check**: Minimum 8 characters
2. **Character Diversity**:
   - At least one uppercase letter (A-Z)
   - At least one lowercase letter (a-z)
   - At least one digit (0-9)
   - At least one special character (!@#$%^&*)
3. **Strength Scoring**:
   - 5/5 = All requirements met
   - 3-4/5 = Moderate strength
   - 0-2/5 = Weak password

### Password Generation Algorithm
1. Selects one random character from each required category
2. Adds 8 more random characters from all categories
3. Shuffles the characters to prevent patterns
4. Outputs a 12-character password guaranteed to pass all checks
