from flask import Flask, redirect, url_for, render_template, request
from datetime import timedelta
import hashlib
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = 'hello'
app.permanent_session_lifetime = timedelta(seconds=10)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/flask_python15gi'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/')
def home():
    print(url_for('home'))
    return render_template(
        'index.html',
        content='Random content',
        people=['Jack', 'Mary', 'Bob'])

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_name = request.form['user-name']
        user_pass = hashlib.md5(request.form['user-pass'].encode()).hexdigest()
        return redirect(url_for('user', name=user_name))
    else:
        return render_template('login.html')

@app.route('/<name>/')
def user(name):
    return f'Hello {name}'


@app.route('/admin/')
def admin():
    return redirect(url_for('home'))


@app.route('/logout/')
def logout():
    session.pop('login', None)
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
