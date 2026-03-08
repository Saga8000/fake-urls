import sys
import os

# Add the parent directory to Python path
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import app

# Vercel serverless function handler
def handler(environ, start_response):
    """WSGI handler for Vercel serverless functions"""
    return app(environ, start_response)

# Export the handler for Vercel
app.handler = handler

# For local development
if __name__ == "__main__":
    app.run(debug=True)
