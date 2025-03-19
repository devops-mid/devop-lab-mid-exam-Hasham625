from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import User
from datetime import datetime

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    phone = request.form.get('phone', '')  # Optional field
    adress = request.form.get('adress', '')  # Optional field
    date_of_birth_str = request.form.get('date_of_birth')  # Get date of birth from the form

    # Convert the date string to a date object
    date_of_birth = datetime.strptime(date_of_birth_str, '%Y-%m-%d') if date_of_birth_str else None

    user = User(name=name, email=email, phone=phone, adress=adress, date_of_birth=date_of_birth)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))
