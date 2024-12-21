# **Simple Bank**

A Django-based web application designed to provide basic banking functionalities like managing accounts, tracking transactions, and enabling deposits, withdrawals, and transfers. Simple Bank offers a user-friendly and secure platform for small-scale banking operations.

---

## **Introduction**

**Simple Bank** is a lightweight, Django-powered web application ideal for users looking to learn or manage essential banking operations. This project serves as a foundation for understanding how web frameworks and database systems can be integrated to create functional banking applications.

### **Purpose**
- Simplify and secure basic banking operations.
- Provide transparency in financial management through transaction history.
- Offer a responsive and intuitive interface for users.

---

## **Technologies Used**
- **Backend**: Python, Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite
- **Authentication**: Django's built-in authentication system

---

## **Features**
- Secure user authentication with session management.
- View and manage account balances.
- Perform deposits, withdrawals, and transfers between accounts.
- Access transaction history with timestamps.
- Mobile-friendly and responsive design.

---

## **Installation**

### **Prerequisites**
Ensure you have the following installed:
- Python 3.8+ (recommended)
- Django 4.0+
- SQLite or another compatible database

### **Steps**
1. Clone the repository:
   ```bash
   git clone https://github.com/patel-ab/simpleBank.git
   cd simpleBank
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate   # For Windows
   ```

3. Install dependencies:
   ```bash
   pip install Django
   pip install djangorestframework
   pip install django-cors-headers
   
   ```

4. Apply migrations to set up the database schema:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Create a superuser for administrative tasks:
   ```bash
   python manage.py createsuperuser
   ```

6. Start the development server:
   ```bash
   python manage.py runserver
   ```

7. Open your browser and navigate to `http://127.0.0.1:8000/`.

---

## **Usage**

### **Admin Panel**
- Access the admin panel at `http://127.0.0.1:8000/admin/` using the superuser credentials.
- Manage users, accounts, and transactions.

### **User Dashboard**
- Users can log in to view their account details, perform transactions, and review their transaction history.

### **Transactions**
- **Deposit**: Add funds to your account.
- **Withdraw**: Remove funds from your account.
- **Transfer**: Send money to another user's account.

---

## **Future Enhancements**
- Integration with third-party payment APIs.
- Email notifications for transactions.
- Support for multiple currencies.

---

## **License**
This project is open-source and available under the MIT License.
