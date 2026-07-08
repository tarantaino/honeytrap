import sqlite3
import datetime
import os

#define where to save db files (main project directory)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_PATH = os.path.join(BASE_DIR, "honeytrap.db")

def init_db():
    #inizialize DB and check if the table exsists already
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    #create "attacks" table with attribute: id, data, ip, user and password
    #cursor method allows to manage tables
    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS attacks(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp TEXT,
                    ip_address TEXT,
                    username TEXT,
                    password TEXT
                    )
                 '''  
    )

    conn.commit() #commit saves the changes
    conn.close()
    print("DB SQLite ready and initialized.")

def log_attack(ip_address, username, password):
    #Register an intrusion attempt to the db
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    #generates the exact time of the attack
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M.%S")

    #we add data carefully to avoid SQL injection
    cursor.execute('''
                    INSERT INTO attacks (timestamp, ip_address, username, password)
                    VALUES(?, ?, ?, ?)                       
                   ''', (now, ip_address, username, password)) #(?,?,?,?) cybersec measure to avoid that an attacker might insert "DROP TABLE attacks, so sqlite3 knows that those values are just junk and defuse them before saving"
    
    conn.commit()
    conn.close()

def get_all_attacks():
    #reads every attacks on db and return them as a dictionary list
    conn = sqlite3.connect(DB_PATH)

    #now we get data as columns names
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    #SQL query to get everything
    cursor.execute("SELECT * FROM attacks ORDER BY timestamp DESC")

    #fetachall() takes all the results found by cursor
    rows = cursor.fetchall()
    conn.close()

    #now we convert them in a standard python dict
    return[dict(row) for row in rows]