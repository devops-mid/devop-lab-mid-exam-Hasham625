from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    phone = request.form.get('phone', '')  # Optional field
    adress = request.form.get('adress', '')  # Optional field
    user = User(name=name, email=email, phone=phone, adress=adress)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))
