from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'kunci_rahasia_anda'

# Inisialisasi database dan buat tabel jika belum ada
def initialize_db():
    conn = sqlite3.connect('laporan_osis.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
    c.execute('''CREATE TABLE IF NOT EXISTS reports (id INTEGER PRIMARY KEY, title TEXT, content TEXT, date TEXT)''')
    conn.commit()
    conn.close()

# Rute untuk halaman utama
@app.route('/')
def home():
    return render_template('index.html')

# Rute untuk halaman login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = sqlite3.connect('laporan_osis.db')
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = c.fetchone()
        conn.close()
        
        if user and check_password_hash(user[2], password):
            session['user_id'] = user[0]
            return redirect(url_for('dashboard'))
        else:
            return "Login gagal. Periksa username dan password Anda."
    return render_template('login.html')

# Rute untuk halaman dashboard
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    conn = sqlite3.connect('laporan_osis.db')
    c = conn.cursor()
    c.execute("SELECT * FROM reports")
    reports = c.fetchall()
    conn.close()
    
    return render_template('dashboard.html', reports=reports)

# Rute untuk mengunggah laporan baru
@app.route('/upload_report', methods=['GET', 'POST'])
def upload_report():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        date = request.form['date']
        
        conn = sqlite3.connect('laporan_osis.db')
        c = conn.cursor()
        c.execute("INSERT INTO reports (title, content, date) VALUES (?, ?, ?)", (title, content, date))
        conn.commit()
        conn.close()
        
        return redirect(url_for('dashboard'))
    
    return render_template('upload_laporan.html')

# Rute untuk logout
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('home'))

# Jalankan aplikasi
if __name__ == '__main__':
    initialize_db()
    app.run(debug=True)
