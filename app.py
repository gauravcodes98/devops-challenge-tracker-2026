from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('challenge.db')
    c = conn.cursor()

    c.execute('''
        CREATE TABLE IF NOT EXISTS progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            day INTEGER,
            topic TEXT
        )
    ''')

    conn.commit()
    conn.close()

@app.route('/')
def home():
    conn = sqlite3.connect('challenge.db')
    c = conn.cursor()

    c.execute("SELECT * FROM progress")
    data = c.fetchall()

    conn.close()

    return render_template('index.html', data=data)

if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
