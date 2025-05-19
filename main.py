from flask import Flask, render_template,request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route('/',methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()
        conn.close()

        if user:
            session['username'] = username
            return redirect(url_for('home'))
        else:
            return "Invalid credentials. <a href='/'>Try again</a>"
        
    return render_template('login2.html')

@app.route('/home')
def home():
     if 'username' in session:
        return render_template('home.html')
     else:
        return redirect(url_for('login'))
     return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
