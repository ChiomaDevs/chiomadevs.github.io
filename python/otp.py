import random

# Generate 6 random numbers between 1 and 10
otp = [random.randint(1, 6) for _ in range(6)]

# Print the OTP as a single string of numbers
print("Your one-time password is:", ''.join(map(str, otp)))
