import sqlite3

def get_connection():
    return sqlite3.connect("crowdfunding.db")

def view_all_users():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, username FROM user")
    users = cur.fetchall()
    conn.close()
    return users

def view_all_projects():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, title, goal, raised FROM project")
    projects = cur.fetchall()
    conn.close()
    return projects

def delete_user(user_id):
    conn = get_connection()
    cur = conn.cursor()
    # Check if the user exists before deleting
    cur.execute("SELECT * FROM user WHERE id=?", (user_id,))
    user = cur.fetchone()
    if user:
        try:
            cur.execute("DELETE FROM user WHERE id=?", (user_id,))
            conn.commit()
            print(f"🗑 User {user_id} deleted.")
        except sqlite3.Error as e:
            print(f"❌ Error deleting user {user_id}: {e}")
    else:
        print(f"❌ User {user_id} does not exist.")
    conn.close()

def delete_project(project_id):
    conn = get_connection()
    cur = conn.cursor()
    # Check if the project exists before deleting
    cur.execute("SELECT * FROM project WHERE id=?", (project_id,))
    project = cur.fetchone()
    if project:
        try:
            cur.execute("DELETE FROM project WHERE id=?", (project_id,))
            conn.commit()
            print(f"🗑 Project {project_id} deleted.")
        except sqlite3.Error as e:
            print(f"❌ Error deleting project {project_id}: {e}")
    else:
        print(f"❌ Project {project_id} does not exist.")
    conn.close()
