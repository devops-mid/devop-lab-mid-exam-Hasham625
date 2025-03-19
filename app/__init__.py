from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create the database object (without initializing it with the app yet)
db = SQLAlchemy()

def create_app():
    # Initialize the Flask app
    app = Flask(__name__)

    # Configure the app
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@postgres-db-service/mydb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the db with the app
    db.init_app(app)

    # Import routes and models inside the create_app function to avoid circular import
    from app import routes, models

    return app
