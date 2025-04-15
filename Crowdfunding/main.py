from backend import functions as f
from backend import admin as a
from backend import report

def user_menu(user_id):
    while True:
        print("\n--- USER MENU ---")
        print("1. Create Project")
        print("2. View Projects")
        print("3. Donate to Project")
        print("4. View My Donations")
        print("5. Logout")

        choice = input("Choose: ")

        if choice == '1':
            title = input("Project title: ")
            desc = input("Description: ")
            goal = float(input("Goal amount: "))
            f.create_project(title, desc, goal, user_id)

        elif choice == '2':
            for p in f.view_all_projects():
                print(p)

        elif choice == '3':
            pid = int(input("Project ID: "))
            amt = float(input("Amount to donate: "))
            f.donate_to_project(pid, user_id, amt)

        elif choice == '4':
            print(f.view_user_donations(user_id))

        elif choice == '5':
            break

def admin_menu():
    while True:
        print("\n--- ADMIN MENU ---")
        print("1. View All Users")
        print("2. Delete User")
        print("3. View All Projects")
        print("4. Delete Project")
        print("5. Export Top Projects")
        print("6. Exit Admin")

        choice = input("Choose: ")

        if choice == '1':
            print(a.view_all_users())

        elif choice == '2':
            uid = int(input("User ID to delete: "))
            a.delete_user(uid)

        elif choice == '3':
            print(a.view_all_projects())

        elif choice == '4':
            pid = int(input("Project ID to delete: "))
            a.delete_project(pid)

        elif choice == '5':
            report.export_top_projects()

        elif choice == '6':
            break

# ---------- Main Entry ----------
while True:
    print("\n=== Welcome to CrowdfundX ===")
    print("1. Register")
    print("2. Login as User")
    print("3. Admin Panel")
    print("4. Exit")

    option = input("Select: ")

    if option == '1':
        uname = input("Username: ")
        pwd = input("Password: ")
        f.register_user(uname, pwd)

    elif option == '2':
        uname = input("Username: ")
        pwd = input("Password: ")
        uid = f.login_user(uname, pwd)
        if uid:
            print(f"🔓 Welcome, {uname}!")
            user_menu(uid)
        else:
            print("❌ Invalid credentials")

    elif option == '3':
        uname = input("Admin Username: ")
        pwd = input("Admin Password: ")
        if uname == 'admin' and pwd == 'admin123':
            print("🔐 Welcome, Admin!")
            admin_menu()
        else:
            print("❌ Access Denied.")

    elif option == '4':
        print("👋 Goodbye!")
        break
