import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app import app

# Vercel serverless function handler
handler = app

# For Vercel deployment, we need to export the app as a WSGI app
def handler(request):
    return app(request.environ, start_response)

# For Vercel deployment, we need to export the app
if __name__ == "__main__":
    app.run()
