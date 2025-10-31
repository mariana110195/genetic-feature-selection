"""
Main Flask Application Entry Point
Genetic Algorithm Feature Selection Web Application

Run with: python app.py
"""

import os
from web import create_app

# Create Flask app instance
app = create_app()

if __name__ == '__main__':
    # Create necessary directories
    os.makedirs('uploads', exist_ok=True)
    os.makedirs('results/experiments', exist_ok=True)
    
    # Run Flask development server
    # For production, use: gunicorn -w 4 -b 0.0.0.0:5000 app:app
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True  # Set to False in production
    )

