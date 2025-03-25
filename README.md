# 🏦 ATM Simulation System

## 📌 Overview
This project is a simple command-line ATM (Automated Teller Machine) simulation system written in Python. It allows users to perform various banking operations such as withdrawing cash, checking their balance, changing their password, and recharging phone credit through Fawry services.

## ✨ Features
- 🔐 **User Authentication:** Users can log in using their account ID and password.
- 🔏 **Secure Password Handling:** Uses `stdiomask` to mask password input.
- 💵 **Cash Withdrawal:** Allows withdrawal of specific amounts with constraints.
- 📊 **Balance Inquiry:** Displays the user's current balance.
- 🔄 **Password Change:** Users can securely update their passwords.
- 📱 **Fawry Service:** Enables mobile recharge for Orange, Etisalat, Vodafone, and We.
- 🚨 **Security Measures:** Blocks users after three incorrect password attempts.

## ⚙️ Prerequisites
Ensure you have Python installed on your system. This script is compatible with Python 3.x.

## 🔧 Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/ATM-Simulation.git
   cd ATM-Simulation
   ```
2. Install dependencies:
   ```bash
   pip install stdiomask
   ```

## ▶️ Usage
1. Run the script:
   ```bash
   python atm.py
   ```
2. Enter your account ID when prompted.
3. Authenticate using your password.
4. Choose from the available options:
   - 💸 Withdraw Cash
   - 📄 Check Balance
   - 🔑 Change Password
   - 📲 Mobile Recharge (Fawry Service)
   - 🚪 Exit

## 📝 Notes
- 📌 Account information is stored in a dictionary within the script.
- 🔢 The system ensures that passwords are four-digit numbers.
- 📞 Phone numbers must be 11 digits, starting with zero.
- 🚫 Users who enter the wrong password three times will be blocked.
