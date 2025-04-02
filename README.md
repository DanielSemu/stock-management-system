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

### 1️⃣ Users Table (`users`)
Stores user details and roles.

| Field    | Type                         | Description     |
|----------|------------------------------|----------------|
| id       | Integer (PK)                  | Unique user ID |
| username | String                        | Unique username |
| email    | String                        | Email address |
| password | String (Hashed)               | User password |
| role     | Enum(Admin, Manager, Staff)   | User role |

---

## 2. Inventory Management Tables

### 2️⃣ Stock Items Table (`stock_items`)
Stores stock details and tracking information.

| Field         | Type        | Description |
|--------------|------------|-------------|
| id          | Integer (PK) | Unique stock item ID |
| name        | String       | Stock item name |
| category_id | ForeignKey   | References `categories(id)` |
| quantity    | Integer      | Available stock quantity |
| price       | Decimal      | Price per unit |
| supplier_id | ForeignKey   | References `suppliers(id)` |
| warehouse_id| ForeignKey   | References `warehouses(id)` |
| min_stock_level | Integer  | Minimum stock level for alerts |

### 3️⃣ Categories Table (`categories`)
Stores different stock categories.

| Field  | Type        | Description |
|--------|------------|-------------|
| id     | Integer (PK) | Unique category ID |
| name   | String       | Category name |

### 4️⃣ Warehouses Table (`warehouses`)
Stores warehouse details.

| Field    | Type        | Description |
|----------|------------|-------------|
| id       | Integer (PK) | Unique warehouse ID |
| name     | String       | Warehouse name |
| location | String       | Warehouse address |

---

## 3. Supplier & Customer Management Tables

### 5️⃣ Suppliers Table (`suppliers`)
Stores supplier details.

| Field    | Type        | Description |
|----------|------------|-------------|
| id       | Integer (PK) | Unique supplier ID |
| name     | String       | Supplier name |
| contact  | String       | Contact information |

### 6️⃣ Customers Table (`customers`)
Stores customer details.

| Field  | Type        | Description |
|--------|------------|-------------|
| id     | Integer (PK) | Unique customer ID |
| name   | String       | Customer name |
| email  | String       | Customer email |
| phone  | String       | Contact number |

---

## 4. Order Management Tables

### 7️⃣ Purchase Orders Table (`purchase_orders`)
Stores details of stock purchased from suppliers.

| Field       | Type        | Description |
|------------|------------|-------------|
| id         | Integer (PK) | Unique order ID |
| supplier_id| ForeignKey   | References `suppliers(id)` |
| order_date | DateTime     | Date of purchase |
| status     | Enum(Pending, Completed, Cancelled) | Order status |

### 8️⃣ Sales Orders Table (`sales_orders`)
Stores sales transactions.

| Field       | Type        | Description |
|------------|------------|-------------|
| id         | Integer (PK) | Unique sales order ID |
| customer_id| ForeignKey   | References `customers(id)` |
| order_date | DateTime     | Date of order |
| status     | Enum(Pending, Completed, Cancelled) | Order status |

### 9️⃣ Order Items Table (`order_items`)
Stores the items included in each sale or purchase.

| Field         | Type        | Description |
|--------------|------------|-------------|
| id          | Integer (PK) | Unique order item ID |
| order_id    | ForeignKey   | References `sales_orders(id)` or `purchase_orders(id)` |
| stock_id    | ForeignKey   | References `stock_items(id)` |
| quantity    | Integer      | Quantity of stock ordered |
| price       | Decimal      | Price per unit |

---

## 5. Stock Movements & Reports

### 🔟 Stock Movements Table (`stock_movements`)
Tracks stock transfers between warehouses.

| Field        | Type        | Description |
|-------------|------------|-------------|
| id          | Integer (PK) | Unique movement ID |
| stock_id    | ForeignKey   | References `stock_items(id)` |
| from_warehouse_id | ForeignKey | Source warehouse (nullable) |
| to_warehouse_id   | ForeignKey | Destination warehouse |
| quantity    | Integer      | Quantity transferred |
| movement_date | DateTime   | Date of movement |

### 1️⃣1️⃣ Stock Alerts Table (`stock_alerts`)
Stores stock level alerts.

| Field    | Type        | Description |
|----------|------------|-------------|
| id       | Integer (PK) | Unique alert ID |
| stock_id | ForeignKey   | References `stock_items(id)` |
| alert_type | Enum(Low Stock, Overstock) | Type of alert |
| created_at | DateTime  | Timestamp of alert |

---

## 6. Authentication & Permissions

### 1️⃣2️⃣ User Permissions Table (`user_permissions`)
Stores user-specific permissions.

| Field    | Type        | Description |
|----------|------------|-------------|
| id       | Integer (PK) | Unique permission ID |
| user_id  | ForeignKey   | References `users(id)` |
| permission | Enum(Add, Edit, Delete, View) | Allowed action |

---

## 7. Additional Features (Optional)

### 1️⃣3️⃣ Returns & Refunds Table (`returns`)
Stores records of returned products.

| Field       | Type        | Description |
|------------|------------|-------------|
| id         | Integer (PK) | Unique return ID |
| order_id   | ForeignKey   | References `sales_orders(id)` |
| stock_id   | ForeignKey   | References `stock_items(id)` |
| quantity   | Integer      | Quantity returned |
| return_reason | String    | Reason for return |

---

### 🎯 **Why is this schema great?**
✅ **Well-structured relationships**  
✅ **Covers all stock management needs**  
✅ **Supports order processing & tracking**  
✅ **Future-proof with extra tables like Returns & Permissions**  

## ✅ Django Apps
1️⃣ users → Handles authentication and user roles

User model (manages roles, permissions)

2️⃣ inventory → Manages stock items, categories, and warehouses

StockItem, Category, Warehouse models (stock management)

3️⃣ orders → Manages purchase orders, sales orders, and order items

PurchaseOrder, SalesOrder, OrderItem models (order processing)

4️⃣ suppliers_customers → Manages supplier and customer information

Supplier, Customer models (supplier/customer data)

5️⃣ stock_movement → Handles stock movements and alerts

StockMovement, StockAlert models (stock transfers and alerts)

6️⃣ returns → Manages product returns

Return model (returns and refunds)
