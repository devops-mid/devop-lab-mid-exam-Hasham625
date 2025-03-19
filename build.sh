#!/bin/bash
echo "Building the application..."

# Install dependencies from requirements.txt
if [ -f "requirements.txt" ]; then
    echo "Installing dependencies..."
    pip install -r requirements.txt
else
    echo "requirements.txt not found!"
    exit 1
fi

# Optionally, you can add any build steps if required (e.g., setting up the environment, compiling assets)
# Example (for Flask app, you might not need this):
# echo "Setting up environment..."
# export FLASK_APP=app.py
# export FLASK_ENV=development
