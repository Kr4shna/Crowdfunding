import sqlite3

def create_tables():
    conn = sqlite3.connect("crowdfunding.db")
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS project (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT,
        goal REAL,
        raised REAL DEFAULT 0,
        creator_id INTEGER,
        FOREIGN KEY (creator_id) REFERENCES user(id)
    )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS donation (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL,
        donor_id INTEGER,
        project_id INTEGER,
        FOREIGN KEY (donor_id) REFERENCES user(id),
        FOREIGN KEY (project_id) REFERENCES project(id)
    )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS admin (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS payment (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        amount REAL,
        date TEXT,
        FOREIGN KEY (user_id) REFERENCES user(id)
    )''')

    cur.execute('''CREATE TABLE IF NOT EXISTS platform_fee (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        donation_id INTEGER,
        fee_percent REAL,
        FOREIGN KEY (donation_id) REFERENCES donation(id)
    )''')

    conn.commit()
    conn.close()
    print("✅ All tables created successfully.")

# Run only when you want to create tables
if __name__ == '__main__':
    create_tables()
