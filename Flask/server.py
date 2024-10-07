from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

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
        user_pass = request.form['user-pass']
        return redirect(url_for('user', name=user_name))
    else:
        return render_template('login.html')

@app.route('/<name>')
def user(name):
    return f'Hello {name}'

@app.route('/admin')
def admin():
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)