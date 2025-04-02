# 🏢 Stock Management System

A powerful Django-based stock management system that helps businesses track their inventory, suppliers, sales, and purchases efficiently.  

---

## 🚀 Features
- ✅ Inventory management (Add, Update, Delete stock)
- ✅ Warehouse tracking
- ✅ Supplier & Customer management
- ✅ Sales & Purchase orders
- ✅ Stock movement tracking
- ✅ Low stock alerts & notifications
- ✅ Role-based authentication (Admin, Manager, Staff)
- ✅ Reports & analytics

---

## 🛠 Installation Guide
### 1️⃣ Clone the repository
```sh
git clone https://github.com/your-username/stock-management.git
cd stock-management
```
2️⃣ Set up a virtual environment
```sh
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate
```
3️⃣ Install dependencies
```sh
pip install -r requirements.txt
```
4️⃣ Run database migrations
```sh
python manage.py makemigrations
python manage.py migrate
```
5️⃣ Create a superuser
```sh
python manage.py createsuperuser
```
6️⃣ Run the server
```sh
python manage.py runserver
```
Now, visit http://127.0.0.1:8000/ in your browser! 🎉

## 🔥 Common Django Commands
| Command	                            | Description                  |
|---------------------------------------|------------------------------|
| python manage.py startapp app_name	| Create a new Django app      |
| python manage.py runserver	        | Start the development server |
| python manage.py createsuperuser	    | Create an admin user         |
| python manage.py makemigrations	    | Prepare database changes     |
| python manage.py migrate	            | Apply database changes       |
| python manage.py shell	            | Open Django shell            |
## 📊 Database Schema
## 1. User & Authentication Tables
### 1️⃣ Users Table (users)
Stores user details and roles.
| Field	    | Type	                     |Description     |
|-----------|----------------------------|----------------|
| id	    | Integer (PK)	             |Unique user ID  |
| username  | String                     |Unique username |
| email	    | String                     |Email address   |
| password  | String (Hashed)            |User password   |
| role      | Enum(Admin, Manager, Staff)| User role      |


##  2. Inventory & Stock Tables
### 2️⃣ Stock Items Table (stock_items)
Stores products in stock.
| Field	          | Type         |Description             |
|-----------------|--------------|------------------------|
| id	          | Integer (PK) | Unique stock item ID   | 
| name            | String       | Stock item name        | 
| category_id     | ForeignKey   | Category of stock      | 
| quantity        | Integer      | Available quantity     | 
| price           | Decimal      | Price per unit         | 
| supplier_id	  | ForeignKey   | Supplier providing item| 
| warehouse_id    | ForeignKey   | Warehouse location     | 
| min_stock_level | Integer      | Low stock alert limit  | 



## 1. User & Authentication Tables
### 1️⃣ Users Table (users)
Stores user details and roles.
| Field	    | Type	                     |Description     |
|-----------|----------------------------|----------------|
| id	    | Integer (PK)	             |Unique user ID  |
| username  | String                     |Unique username |
| email	    | String                     |Email address   |
| password  | String (Hashed)            |User password   |
| role      | Enum(Admin, Manager, Staff)| User role      |
## 1. User & Authentication Tables
### 1️⃣ Users Table (users)
Stores user details and roles.
| Field	    | Type	                     |Description     |
|-----------|----------------------------|----------------|
| id	    | Integer (PK)	             |Unique user ID  |
| username  | String                     |Unique username |
| email	    | String                     |Email address   |
| password  | String (Hashed)            |User password   |
| role      | Enum(Admin, Manager, Staff)| User role      |
## 1. User & Authentication Tables
### 1️⃣ Users Table (users)
Stores user details and roles.
| Field	    | Type	                     |Description     |
|-----------|----------------------------|----------------|
| id	    | Integer (PK)	             |Unique user ID  |
| username  | String                     |Unique username |
| email	    | String                     |Email address   |
| password  | String (Hashed)            |User password   |
| role      | Enum(Admin, Manager, Staff)| User role      |
## 1. User & Authentication Tables
### 1️⃣ Users Table (users)
Stores user details and roles.
| Field	    | Type	                     |Description     |
|-----------|----------------------------|----------------|
| id	    | Integer (PK)	             |Unique user ID  |
| username  | String                     |Unique username |
| email	    | String                     |Email address   |
| password  | String (Hashed)            |User password   |
| role      | Enum(Admin, Manager, Staff)| User role      |
## 1. User & Authentication Tables
### 1️⃣ Users Table (users)
Stores user details and roles.
| Field	    | Type	                     |Description     |
|-----------|----------------------------|----------------|
| id	    | Integer (PK)	             |Unique user ID  |
| username  | String                     |Unique username |
| email	    | String                     |Email address   |
| password  | String (Hashed)            |User password   |
| role      | Enum(Admin, Manager, Staff)| User role      |
## 1. User & Authentication Tables
### 1️⃣ Users Table (users)
Stores user details and roles.
| Field	    | Type	                     |Description     |
|-----------|----------------------------|----------------|
| id	    | Integer (PK)	             |Unique user ID  |
| username  | String                     |Unique username |
| email	    | String                     |Email address   |
| password  | String (Hashed)            |User password   |
| role      | Enum(Admin, Manager, Staff)| User role      |
## 1. User & Authentication Tables
### 1️⃣ Users Table (users)
Stores user details and roles.
| Field	    | Type	                     |Description     |
|-----------|----------------------------|----------------|
| id	    | Integer (PK)	             |Unique user ID  |
| username  | String                     |Unique username |
| email	    | String                     |Email address   |
| password  | String (Hashed)            |User password   |
| role      | Enum(Admin, Manager, Staff)| User role      |
## 1. User & Authentication Tables
### 1️⃣ Users Table (users)
Stores user details and roles.
| Field	    | Type	                     |Description     |
|-----------|----------------------------|----------------|
| id	    | Integer (PK)	             |Unique user ID  |
| username  | String                     |Unique username |
| email	    | String                     |Email address   |
| password  | String (Hashed)            |User password   |
| role      | Enum(Admin, Manager, Staff)| User role      |
## 1. User & Authentication Tables
### 1️⃣ Users Table (users)
Stores user details and roles.
| Field	    | Type	                     |Description     |
|-----------|----------------------------|----------------|
| id	    | Integer (PK)	             |Unique user ID  |
| username  | String                     |Unique username |
| email	    | String                     |Email address   |
| password  | String (Hashed)            |User password   |
| role      | Enum(Admin, Manager, Staff)| User role      |
## 1. User & Authentication Tables
### 1️⃣ Users Table (users)
Stores user details and roles.
| Field	    | Type	                     |Description     |
|-----------|----------------------------|----------------|
| id	    | Integer (PK)	             |Unique user ID  |
| username  | String                     |Unique username |
| email	    | String                     |Email address   |
| password  | String (Hashed)            |User password   |
| role      | Enum(Admin, Manager, Staff)| User role      |








## 🏗 Future Enhancements
- ✅ Automated Dividend Payouts
- ✅ Graphical Dashboards & Reports
- ✅ Integration with Payment Gateways
## 🤝 Contributing
Feel free to fork the repo, submit issues, or create pull requests!

## 📜 License
This project is licensed under the MIT License.



