from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models import User
from datetime import datetime
import re

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

    # Validate Phone Number: Check if it is numeric and exactly 10 digits
    if phone and (not phone.isdigit() or len(phone) != 10):
        flash("Phone number must be numeric and exactly 10 digits long.", "error")
        return redirect(url_for('index'))

    # Validate Date of Birth
    date_of_birth = datetime.strptime(date_of_birth_str, '%Y-%m-%d') if date_of_birth_str else None

    # Create the User object and save to the database
    user = User(name=name, email=email, phone=phone, adress=adress, date_of_birth=date_of_birth)
    db.session.add(user)
    db.session.commit()

    # Flash success message
    flash("User successfully added!", "success")
    return redirect(url_for('index'))
