#!/bin/bash

# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate

# Install requirements
pip install -r requirements.txt

# Create .env file from example if it doesn't exist
if [ ! -f .env ]; then
    cp .env.example .env
    echo "Created .env file. Please edit it to add your Groq API key."
fi

echo "Setup complete! To run Suho PDF Reader:"
echo "1. Activate the virtual environment: source venv/bin/activate"
echo "2. Make sure you've added your Groq API key to the .env file"
echo "3. Run the app: streamlit run app.py"
