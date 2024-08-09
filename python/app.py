from flask import Flask, render_template, request
import random

app = Flask(__name__)

def generate_otp():
    """Function to generate a 6-digit OTP"""
    otp = random.randint(100000, 999999)
    return otp

@app.route("/", methods=["GET", "POST"])
def index():
    otp = None
    if request.method == "POST":
        # Generate OTP
        otp = generate_otp()
    return render_template("index.html", otp=otp)

if __name__ == "__main__":
    app.run(debug=True)
