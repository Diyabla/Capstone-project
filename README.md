# Inventory Management API

A RESTful Inventory Management API built using **Django** and **Django REST Framework**.

This project allows authenticated users to manage inventory items securely, track stock changes, and filter or sort inventory data efficiently.

---

## 📌 Project Overview

This API simulates a real-world inventory management system where users can:

- Create inventory items  
- View inventory levels  
- Update stock quantities  
- Delete items  
- Track inventory changes  
- Filter and sort inventory data  

Each user can only access and manage their own inventory items.

---

## 🛠 Tech Stack

- Python
- Django
- Django REST Framework
- JWT Authentication (SimpleJWT)
- SQLite (Development)
- PostgreSQL (Production Ready)
- django-filter

---

## 🚀 Features

### 👤 User Management
- Create users
- Secure password handling
- JWT-based authentication
- Authenticated access control

### 📦 Inventory Management (CRUD)
- Create inventory items
- Retrieve inventory items
- Update inventory items
- Delete inventory items

Each inventory item contains:

- Name
- Description
- Quantity
- Price
- Category
- Date Added
- Last Updated

---

### 🔍 Filtering and Sorting

Filter inventory by:

- Category  
- Price range  
- Low stock threshold  

Sort inventory by:

- Name  
- Quantity  
- Price  
- Date Added  

---

### 📄 Pagination

- Page number pagination enabled globally
- 10 items per page

---

### 📊 Inventory Change Tracking

- Automatically logs quantity updates
- Tracks:
  - Previous quantity
  - New quantity
  - User who made the change
  - Timestamp
- Dedicated endpoint to view inventory change history

---

## 🔐 Authentication

This API uses JWT authentication.

### Obtain Access Token

**POST**
