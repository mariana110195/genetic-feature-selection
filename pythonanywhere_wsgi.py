"""
WSGI Configuration for PythonAnywhere Deployment
Student 6: Use this file to deploy the application on pythonanywhere.com

Instructions:
1. Upload all project files to pythonanywhere
2. Install requirements: pip install -r requirements.txt
3. Configure this file in the Web tab
4. Set the working directory to your project folder
5. Reload the web app
"""

import sys
import os

# Add your project directory to the sys.path
project_home = '/home/YOUR_USERNAME/genetic-feature-selection'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Import Flask app
from web import create_app

# Create application instance
application = create_app()

# Optional: Set up logging
import logging
logging.basicConfig(level=logging.INFO)

