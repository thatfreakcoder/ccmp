from flask import Flask, render_template, url_for, session, redirect
from os import urandom

app = Flask(__name__)
app.config['SECRET_KEY'] = urandom(24)

@app.route('/')
def index():
    try:
        if session['user'] == 'user':
            return render_template('index-user.html')
        elif session['user'] == 'admin':
            return render_template('index-admin.html')
    except:
        return render_template('index.html')

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/index-user.html')
def login_user():
    session['user'] = 'user'
    return redirect('/')

@app.route('/index-admin.html')
def login_admin():
    session['user'] = 'admin'
    return redirect('/')

@app.route('/register.html')
def register():
    return render_template('register.html')

@app.route('/create.html')
def create():
    return render_template('create.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/forgot-password.html')
def forgot():
    return render_template('forgot-password.html')

@app.route('/index.html')
def logout():
    session.clear()
    return redirect('/')

@app.errorhandler(404)
def error(e):
	return render_template("404.html", msg=e)

if __name__ == '__main__':
    app.run(debug=True)