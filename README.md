# CrowdfundX 💸

CrowdfundX is a simple crowdfunding platform built with **Python**, **Tkinter**, and **SQLite**, featuring user and admin roles. Users can create projects, donate to others, and receive email confirmations. Admins can manage users and projects.

---

## 🔧 Features

### 👤 Users
- Register/Login
- Create crowdfunding projects with goal and description
- Donate to projects
- View all active projects
- Receive **thank-you emails** after donating

### 🔐 Admin
- Admin login (default: `admin / admin123`)
- View all users and projects
- Delete users or projects from the database

---

## 🗃️ Tech Stack

- **Frontend:** Tkinter (Python GUI)
- **Backend:** SQLite3
- **Email Service:** `smtplib` + Gmail SMTP
- **Architecture:** Modularized into `backend/`, `utils/`, and `app.py`

---

## 📁 Folder Structure

Crowdfunding/
├── backend/
│   ├── __pycache__/
│   ├── admin.py
│   ├── functions.py
│   └── report.py
├── database/
│   └── schema.py
├── gui/
│   └── app.py          👈 You have to runn this
├── utils/
│   └── emailer.py
├── crowdfunding.db
├── main.py
└── seed.py

---

## ✉️ Email Setup

1. Replace sender credentials in `utils/emailer.py`:
```python
sender = "your_email@gmail.com"
password = "your_app_password"
