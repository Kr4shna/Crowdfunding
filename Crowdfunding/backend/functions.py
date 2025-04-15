import sqlite3

def get_connection():
    return sqlite3.connect("crowdfunding.db")

# ---------------- USER FUNCTIONS ----------------

def register_user(username, password):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO user (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        print("✅ Registered successfully!")
    except sqlite3.IntegrityError:
        print("❌ Username already exists.")
    conn.close()

def login_user(username, password):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM user WHERE username=? AND password=?", (username, password))
    result = cur.fetchone()
    conn.close()
    return result[0] if result else None

# ---------------- PROJECT FUNCTIONS ----------------

def create_project(title, description, goal, creator_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO project (title, description, goal, raised, creator_id) VALUES (?, ?, ?, ?, ?)",
                (title, description, goal, 0.0, creator_id))
    conn.commit()
    conn.close()
    print("✅ Project created!")

def view_all_projects():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, title, goal, raised FROM project")
    projects = cur.fetchall()
    conn.close()
    return projects

def view_project_details(project_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM project WHERE id=?", (project_id,))
    project = cur.fetchone()
    conn.close()
    return project

# ---------------- DONATION FUNCTIONS ----------------

def donate_to_project(project_id, user_id, amount):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO donation (amount, donor_id, project_id) VALUES (?, ?, ?)", (amount, user_id, project_id))
    cur.execute("UPDATE project SET raised = raised + ? WHERE id=?", (amount, project_id))
    conn.commit()
    conn.close()
    print(f"✅ Donated ₹{amount} to project {project_id}")

def view_user_donations(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT project_id, amount FROM donation WHERE donor_id=?", (user_id,))
    donations = cur.fetchall()
    conn.close()
    return donations

# ---------------- ADMIN FUNCTIONS ----------------

def view_all_users():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, username FROM user")
    users = cur.fetchall()
    conn.close()
    return users

def delete_user(user_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM user WHERE id=?", (user_id,))
    conn.commit()
    conn.close()
    print(f"🗑 User {user_id} deleted.")

def delete_project(project_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM project WHERE id=?", (project_id,))
    conn.commit()
    conn.close()
    print(f"🗑 Project {project_id} deleted.")
