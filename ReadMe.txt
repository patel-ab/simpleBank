# **Bank Management System**

A Django-based web application for managing bank accounts, transactions, and users. This project provides functionalities for deposits, withdrawals, money transfers, and transaction history tracking, offering a simple and secure banking solution.

---

## **Table of Contents**
- [Introduction](#introduction)
- [Purpose](#Purpose)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)


---

## **Introduction**

The **Bank Management System** is a web-based application built using Django that simplifies banking operations. It is ideal for small-scale banking solutions or as a learning project for those interested in web development and database management using Python Django Framework. 

### **Purpose**
- Facilitate basic banking operations like deposits, withdrawals, and transfers.
- Provide transaction history for users.
- Secure user authentication and account management.

---

## **Technologies Used**
- **Backend**: Python, Django
- **Frontend**: Javascript, HTML, CSS
- **Database**: SQLite (default)
- **Authentication**: Django Authentication System

---

## **Features**
- User authentication and session management.
- View account balance.
- Deposit and withdraw funds.
- Transfer money to other registered users.
- View transaction history.
- Simple and responsive user interface.

---

## **Installation**

### **Prerequisites**
Ensure you have the following installed on your system:
- Python 3.8+
- Django 4.0+
- A database system like SQLite (default) or PostgreSQL

### **Steps**
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/bank-management-system.git
   cd bank-management-system
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate     # For Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run migrations to set up the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser for admin access:
   ```bash
   python manage.py createsuperuser
   ```

6. Start the server:
   ```bash
   python manage.py runserver
   ```

7. Access the application at `http://127.0.0.1:8000/`.

---

## **Usage**

1. **Admin Access**:
   - Log in as a superuser at `http://127.0.0.1:8000/admin/`.
   - Manage users, accounts, and transactions.

2. **User Operations**:
   - Sign up to create a new user.
   - Log in to view the dashboard.
   - Perform deposits, withdrawals, and transfers.
   - View transaction history.

3. **Transfer Money**:
   - Go to the transfer page.
   - Enter the recipient's name and the amount to transfer.
   - Confirm the transaction.


---

