import time
import pyotp
import qrcode

key = pyotp.random_base32()

print("Enter this to your auth app :")

print(key)

totp = pyotp.TOTP(key)

uri = pyotp.totp.TOTP(key).provisioning_uri(name="totp")

qrcode.make(uri).save("qrcode.png")

code = totp.now()
 
input_code = input("Enter the totp :" )
output = "Incorrect"  # Default output

if input_code == code:
    output = "Correct"

print(f"Output: {output}")

