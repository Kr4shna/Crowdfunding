import sqlite3
import csv
import os
from datetime import datetime

def export_top_projects(limit=5, filename=None):
    if not filename:
        # Generate filename with timestamp to avoid overwriting
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"top_projects_{timestamp}.csv"
    
    try:
        # Connect to the database
        conn = sqlite3.connect("crowdfunding.db")
        cur = conn.cursor()
        
        # Retrieve the top projects based on 'raised' amount
        cur.execute("SELECT title, goal, raised FROM project ORDER BY raised DESC LIMIT ?", (limit,))
        data = cur.fetchall()
        
        # Close the connection
        conn.close()
        
        if data:
            # Writing data to CSV file
            with open(filename, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Title', 'Goal', 'Raised'])
                writer.writerows(data)
            print(f"📄 Successfully exported top {limit} projects to {filename}")
        else:
            print("❌ No data found to export.")
    
    except sqlite3.Error as e:
        print(f"❌ Error connecting to the database: {e}")
    except Exception as e:
        print(f"❌ An error occurred: {e}")

