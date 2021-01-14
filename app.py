from db import DB
from flask import Flask, render_template, request, url_for, flash, redirect
from werkzeug.exceptions import abort

app = Flask(__name__)
app.config['SECRET_KEY'] = 'admin'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods=('GET', 'POST'))
def form():
    if request.method == 'POST':
        name = request.form['name']
        forname = request.form['forname']
        email = request.form['email']
        donate = request.form['donate']

        if not name:
            flash('Name is required!')
        elif not forname:
            flash('Forname is required!')
        elif not email:
            flash('Email is required!')
        elif not donate:
            flash('Donation is required!')
        else:
            DB.send_form(name, forname, email, donate)
            return redirect(url_for('index'))
        
    return render_template('form.html')

@app.route('/contributors')
def contributors():
    top = DB.get_top()
    don = DB.get_don()
    sum = 0
    for d in don:
        sum += int(d['donate'])
    return render_template('contrib.html', top=top, don=don, sum=sum)

@app.route('/infos')
def infos():
    return render_template('infos.html')

if __name__ == '__main__':
    app.run(port=8000, debug=True)
