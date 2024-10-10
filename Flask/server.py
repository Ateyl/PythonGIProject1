
from flask import Flask, redirect, url_for, render_template, request, session, flash
from sqlalchemy import desc
from datetime import timedelta, datetime
import hashlib
from flask_sqlalchemy import SQLAlchemy
from utils.helpers import allowed_file, unique_filename


app = Flask(__name__)
app.secret_key = 'hello'
app.permanent_session_lifetime = timedelta(minutes=30)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:1234@localhost/flask_python15gi'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['UPLOAD_FOLDER'] = 'static/upload'
app.config['MAX_CONTENT_LENGTH'] = 16*1024*1024


db = SQLAlchemy(app)

class Post(db.Model):
    # __tablename__ = 'user-post'
    _id_ = db.Column('post_id', db.Integer, primary_key=True)
    title = db.Column('title', db.String(100))
    content = db.Column('content', db.String(1000))
    date_added = db.Column('date_added', db.DateTime())
    owner = db.Column('owner', db.String(20))
    def __init__(self, title, content, owner):
        self.title = title
        self.content = content
        self.owner = owner
        self.date_added = datetime.now()

class User(db.Model):
    _id = db.Column('user_id', db.Integer, primary_key=True)
    login = db.Column('login',db.String(20), unique=True)
    password = db.Column('password', db.String(32))
    email = db.Column('email', db.String(100))
    avatar = db.column('avatar', db.String(100))

    def __init__(self, login, password, email='', avatar=''):
        self.login = login
        self.password = password
        self.email = email
        self.avatar = avatar

@app.route('/')
def home():
    posts = Post.query.order_by(desc('date_added')).all()
    return render_template(
        'index.html',
        posts=posts
    )

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
                flash('Logged in successfully.', 'success')
                return redirect(url_for('user_profile'))
            else:
                flash('wrong password.', 'danger')
                return redirect(url_for('login'))
        else:
            new_user = User(user_name, user_pass, '')
            db.session.add(new_user)
            db.session.commit()

            session['login'] = user_name
            session['email'] =''
            flash('User account is created', 'success')
            return redirect(url_for('user_profile'))

    else:
        if 'login' in session:
            flash('you are already logged in', 'info')
            return redirect(url_for('user_profile'))
        return render_template('login.html')

@app.route('/<name>/')
def user(name):
    return f'Hello {name}'

@app.route('/user_profile/', methods=['GET', 'POST'])
def user_profile():
    if 'login' in session:
        if request.method == 'POST':
            user_email = request.form['user-email']
            user_in_db = User.query.filter_by(login=session['login']).first()
            user_in_db.email = user_email
            db.session.commit()
            session['email'] = user_email
            flash('Email was saved', 'success')

        return render_template('user.html',login=session['login'], email=session['email'])
    else:
        flash('Please log in.', 'info')
        return redirect(url_for('login'))

@app.route('/admin/')
def admin():
    return redirect(url_for('home'))


@app.route('/logout/')
def logout():
    session.pop('login', None)
    session.pop('email', None)
    flash('logged out', 'info')
    return redirect(url_for('login'))


@app.route('/delete_user')
def delete_user():
    User.query.filter_by(login=session['login']).delete()
    db.session.commit()
    session.pop('login', None)
    session.pop('email', None)
    flash('User was deleted', 'success')
    return redirect(url_for('home'))

@app.route('/post/', methods=['GET', 'POST'])
def post():
    if 'login' in session:
        if request.method == 'POST':
            title = request.form['post-title']
            content = request.form['post-content']
            new_post = Post(title, content, session['login'])
            db.session.add(new_post)
            db.session.commit()
            flash('Post saved', 'success')
            return redirect(url_for('home'))
        else:
            return render_template('post.html')
    else:
        return redirect(url_for('login'))

@app.route('/delete_post/<post_id>')
def delete_post(post_id):
    post = Post.query.filter_by(_id_=post_id).first()
    if 'login' in session and post.owner == session['login']:
        Post.query.filter_by(_id_=post_id).delete()
        db.session.commit()
        flash('Post was deleted','success')
    return redirect(url_for('home'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)

