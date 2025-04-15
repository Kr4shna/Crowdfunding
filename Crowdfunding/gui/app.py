import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import tkinter as tk
from tkinter import messagebox
from backend import functions as f
from backend import admin as a
from utils.emailer import send_thank_you

# ---------- AUTH FUNCTIONS ----------

def login():
    username = entry_username.get()
    password = entry_password.get()
    user_id = f.login_user(username, password)
    if user_id:
        window.destroy()
        open_user_dashboard(user_id, username)
    else:
        messagebox.showerror("Error", "Invalid username or password")

def register():
    username = entry_username.get()
    password = entry_password.get()
    f.register_user(username, password)
    messagebox.showinfo("Success", "User registered. Please log in.")

def admin_login():
    username = entry_username.get()
    password = entry_password.get()
    if username == "admin" and password == "admin123":
        window.destroy()
        open_admin_dashboard()
    else:
        messagebox.showerror("Error", "Invalid admin credentials")

# ---------- USER DASHBOARD ----------

def open_user_dashboard(user_id, username):
    user_win = tk.Tk()
    user_win.title(f"Welcome {username}")
    user_win.geometry("500x500")

    def create_project():
        title = entry_title.get()
        desc = entry_desc.get()
        goal = float(entry_goal.get())
        f.create_project(title, desc, goal, user_id)
        messagebox.showinfo("Done", "Project created!")

    def donate():
        pid = int(entry_project_id.get())
        amt = float(entry_donation.get())
        f.donate_to_project(pid, user_id, amt)
        project = f.view_project_details(pid)
        send_thank_you(to_email=f"{username}@example.com", username=username, project_title=project[1], amount=amt)
        messagebox.showinfo("Thanks", f"Donated ₹{amt} and email sent!")

    tk.Label(user_win, text="Create Project").pack()
    entry_title = tk.Entry(user_win)
    entry_title.insert(0, "Title")
    entry_title.pack()

    entry_desc = tk.Entry(user_win)
    entry_desc.insert(0, "Description")
    entry_desc.pack()

    entry_goal = tk.Entry(user_win)
    entry_goal.insert(0, "Goal")
    entry_goal.pack()

    tk.Button(user_win, text="Create", command=create_project).pack(pady=10)

    tk.Label(user_win, text="Donate to Project").pack()
    entry_project_id = tk.Entry(user_win)
    entry_project_id.insert(0, "Project ID")
    entry_project_id.pack()

    entry_donation = tk.Entry(user_win)
    entry_donation.insert(0, "Amount")
    entry_donation.pack()

    tk.Button(user_win, text="Donate", command=donate).pack(pady=10)

    def show_projects():
        all_p = f.view_all_projects()
        text.delete("1.0", tk.END)
        for p in all_p:
            text.insert(tk.END, f"ID: {p[0]} | {p[1]} - ₹{p[3]}/{p[2]}\n")

    tk.Button(user_win, text="View All Projects", command=show_projects).pack(pady=10)

    def go_back():
        user_win.destroy()
        show_login_window()

    tk.Button(user_win, text="← Go Back", command=go_back).pack(pady=10)

    text = tk.Text(user_win, height=10, width=60)
    text.pack()

    user_win.mainloop()

# ---------- ADMIN DASHBOARD ----------

def open_admin_dashboard():
    admin_win = tk.Tk()
    admin_win.title("Admin Dashboard")
    admin_win.geometry("500x500")

    def show_users():
        text.delete("1.0", tk.END)
        for u in a.view_all_users():
            text.insert(tk.END, f"ID: {u[0]} - {u[1]}\n")

    def show_projects():
        text.delete("1.0", tk.END)
        for p in a.view_all_projects():
            text.insert(tk.END, f"ID: {p[0]} - {p[1]} ₹{p[3]}/{p[2]}\n")

    def delete_user():
        uid = int(entry_admin_id.get())
        a.delete_user(uid)
        messagebox.showinfo("Done", f"User {uid} deleted.")

    def delete_project():
        pid = int(entry_admin_id.get())
        a.delete_project(pid)
        messagebox.showinfo("Done", f"Project {pid} deleted.")

    tk.Button(admin_win, text="Show All Users", command=show_users).pack()
    tk.Button(admin_win, text="Show All Projects", command=show_projects).pack()

    entry_admin_id = tk.Entry(admin_win)
    entry_admin_id.insert(0, "ID")
    entry_admin_id.pack()

    tk.Button(admin_win, text="Delete User", command=delete_user).pack()
    tk.Button(admin_win, text="Delete Project", command=delete_project).pack()

    def go_back():
        admin_win.destroy()
        show_login_window()

    tk.Button(admin_win, text="← Go Back", command=go_back).pack(pady=10)

    text = tk.Text(admin_win, height=15, width=60)
    text.pack()

    admin_win.mainloop()

# ---------- LOGIN WINDOW ----------

def show_login_window():
    global window
    window = tk.Tk()
    window.title("CrowdfundX Login")
    window.geometry("400x300")

    tk.Label(window, text="Username").pack(pady=5)
    global entry_username
    entry_username = tk.Entry(window)
    entry_username.pack()

    tk.Label(window, text="Password").pack(pady=5)
    global entry_password
    entry_password = tk.Entry(window, show="*")
    entry_password.pack()

    tk.Button(window, text="Login", command=login).pack(pady=10)
    tk.Button(window, text="Register", command=register).pack()
    tk.Button(window, text="Admin Login", command=admin_login).pack(pady=10)

    window.mainloop()

# ---------- Run App ----------
show_login_window()
