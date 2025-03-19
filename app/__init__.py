from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Create a new SQLAlchemy object, but don't bind it to the app yet
db = SQLAlchemy()

def create_app():
    # Initialize the Flask app
    app = Flask(__name__)

    # Configure the app
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@postgres-db-service/mydb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Bind the db object to the app
    db.init_app(app)

    # Import routes and models
    from app import routes, models

    return app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@postgres-db-service/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from app import routes, models
