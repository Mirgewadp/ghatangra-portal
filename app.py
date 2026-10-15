from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'gram_secret_key'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    gp_id = request.form.get('gp_id')
    email = request.form.get('email')
    password = request.form.get('password')
    
    if gp_id == '476137' and email == 'pamamirge1990@gmail.com' and password == 'Shivansh@123':
        return render_template('dashboard.html', gp_name='घटांग्रा')
    else:
        return "लॉगिन अयशस्वी! कृपया अचूक माहिती टाका."

if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('grampanchayat.db')
    cursor = conn.cursor()
    # नमुना ८ टेबल
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS namuna8 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            property_no TEXT, village TEXT, owner_name TEXT, occupant_name TEXT,
            tax_year TEXT, house_tax REAL, health_tax REAL, light_tax REAL, total_tax REAL
        )
    ''')
    # नमुना ९ टेबल (वसूल पावती नोंदवही)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS namuna9 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            receipt_no TEXT, date TEXT, taxpayer_name TEXT, details TEXT, paid_amount REAL
        )
    ''')
    # नमुना १० टेबल (जमा-खर्च तपशील)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS namuna10 (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT, particulars TEXT, receipt REAL, payment REAL, balance REAL
        )
    ''')
    conn.commit()
    conn.close()

init_db()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    return render_template('dashboard.html')

# --- नमुना ८ रूट्स ---
@app.route('/namuna8')
def namuna8_list():
    conn = sqlite3.connect('grampanchayat.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM namuna8')
    records = cursor.fetchall()
    conn.close()
    return render_template('namuna8_list.html', records=records)

@app.route('/print_namuna8/<int:id>')
def print_namuna8(id):
    conn = sqlite3.connect('grampanchayat.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM namuna8 WHERE id = ?', (id,))
    data = cursor.fetchone()
    conn.close()
    return render_template('print_namuna8.html', data=data)

# --- नमुना ९ रूट्स ---
@app.route('/namuna9')
def namuna9_list():
    conn = sqlite3.connect('grampanchayat.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM namuna9')
    records = cursor.fetchall()
    conn.close()
    return render_template('namuna9_list.html', records=records)

# --- नमुना १० रूट्स ---
@app.route('/namuna10')
def namuna10_list():
    conn = sqlite3.connect('grampanchayat.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM namuna10')
    records = cursor.fetchall()
    conn.close()
    return render_template('namuna10_list.html', records=records)

if __name__ == '__main__':
    app.run(debug=True)
