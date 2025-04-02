# 📈 Stock Management System  

*A web-based system for managing shares, investors, and transactions efficiently. Built with Django.*

## 🚀 Features  
- 📜 **Investor Management** – Register, update, and manage shareholders.  
- 🔄 **Share Transactions** – Buy, sell, and transfer shares.  
- 📊 **Dividends Calculation** – Automatically calculate and distribute dividends.  
- 🏦 **Financial Reports** – Generate reports on shareholder holdings and transactions.  
- 🔐 **User Authentication & Role Management** – Admin, Investors, and Staff access levels.  
- 📡 **Real-time Updates** – Track live changes in share allocations.  
- 🖥 **Responsive UI** – Seamless experience across all devices.  

## 🛠 Tech Stack  
- **Backend:** Django, Django REST Framework  
- **Frontend:** HTML, CSS, JavaScript  
- **Database:** PostgreSQL / SQLite  
- **Authentication:** Django Authentication & Authorization  
- **Deployment:** Docker, Nginx, Gunicorn  

## 📌 Installation  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/yourusername/share-management-system.git
cd share-management-system
```
### 2️⃣ Create a Virtual Environment & Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
### 3️⃣ Set Up the Database
```bash
python manage.py migrate
```
### 4️⃣ Create a Superuser (Admin Panel)
```bash
python manage.py createsuperuser
```
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



