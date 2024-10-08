from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta
import hashlib
from flask_sqlalchemy import SQLAlchemy
from numpy.ma.extras import unique

app = Flask(__name__)
app.secret_key = 'hello'
app.permanent_session_lifetime = timedelta(seconds=10)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/flask_python15gi'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    _id = db.Column('user_id', db.Integer, primary_key=True)
    login = db.Column('login',db.String(20), unique=True)
    password = db.Column('password', db.String(32))
    email = db.Column('email', db.String(100))

    def __init__(self, login, password, email):
        self.login = login
        self.password = password
        self.email = email

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
        session.permanent = True
        user_name = request.form['user-name']
        user_pass = hashlib.md5(request.form['user-pass'].encode()).hexdigest()
        user_in_db = User.query.filter_by(login=user_name).first()
        if user_in_db:
            if user_pass == user_in_db.password:
                session['login'] = user_name
                session['email'] = user_in_db.email
                return redirect(url_for('user_profile'))
            else:
                return redirect(url_for('login'))

        session['login'] = user_name
        return redirect(url_for('user', name=user_name))
    else:
        if 'login' in session:
            return redirect(url_for('user', name=session['login']))
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
    with app.app_context():
        db.create_all()
    app.run(debug=True)

