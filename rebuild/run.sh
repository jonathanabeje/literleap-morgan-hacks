#!/bin/bash

# Create and activate virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python -m venv venv
fi

# Activate virtual environment
if [[ "$OSTYPE" == "msys" || "$OSTYPE" == "win32" ]]; then
    # Windows
    source venv/Scripts/activate
else
    # Linux and MacOS
    source venv/bin/activate
fi

# Install requirements
echo "Installing requirements..."
pip install -r requirements.txt

# Run the application
echo "Starting LiterLeap Flask application..."
export FLASK_APP=app.py
export FLASK_ENV=development
python -m flask run --port=5000
# Note: this doesn't deactivate the venv to avoid terminating the Flask server 