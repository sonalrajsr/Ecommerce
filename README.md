# E-commerce Web Application

## Project Description
This is a comprehensive e-commerce web application built with Django. The application provides a seamless shopping experience for users, featuring a dynamic product catalog, user authentication, cart functionality, secure checkout, and order tracking. The project aims to offer a scalable and secure platform for online shopping.

## Features
- User Registration and Authentication
- Dynamic Product Catalog
- Shopping Cart and Checkout System
- Order Management and Tracking
- Secure Payment Gateway Integration
- Admin Interface for Managing Products, Orders, and Users
- Responsive Design for Mobile and Desktop

## Technologies Used
- **Frontend:** HTML5, CSS3, JavaScript
- **Backend:** Django, Python
- **Database:** SQLite (development), PostgreSQL (production)
- **Tools:** Git, GitHub, Django Admin
- **Other:** UUID for unique identifiers, Django ORM for database interactions, Payment Gateway API for secure transactions

## Installation
### Prerequisites
- Python 3.x
- Django
- Git

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/sonalrajsr/Ecommerce.git
    cd ecommerce-web-app
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Apply the migrations:
    ```bash
    python manage.py migrate
    ```

5. Create a superuser:
    ```bash
    python manage.py createsuperuser
    ```

6. Start the development server:
    ```bash
    python manage.py runserver
    ```

## Usage
1. Access the application in your web browser at `http://127.0.0.1:8000`.
2. Use the Django admin interface at `http://127.0.0.1:8000/admin` to manage products, orders, and users.
3. Register a new user or log in with an existing account to start shopping.
4. Add products to the cart and proceed to checkout for placing orders.
