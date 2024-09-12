# Two-Factor Authentication using Google Authenticator

This Python script implements a simple two-factor authentication (2FA) system using the `pyotp` library, allowing you to integrate with Google Authenticator.

## Setup

1. **Install the necessary libraries:**
   ```bash
   pip install pyotp qrcode
  ```bash
   git clone https://www.github.com/otherdani/2fac
   
2. Create a new Google Authenticator account:
 - Go to https://www.google.com/landing/2step/ and follow the instructions to set up your account.
3. Generate a QR code:
- This script will generate a QR code containing the secret key needed by Google Authenticator.
- Scan this QR code with the Google Authenticator app on your smartphone.
**Usage**
- Run the script:
  - Execute the script using: python main.py
  - Enter the secret key:
  - The script will print a secret key, copy this key and add it to your Google Authenticator app.
- Scan the QR code:
The script generates a QR code, scan this QR code with the Google Authenticator app on your smartphone.
Enter the generated code:
The script will prompt you to enter the six-digit code generated by Google Authenticator.
Verify the code:
The script will verify the code and print "Correct" if it matches or "Incorrect" if it doesn't.