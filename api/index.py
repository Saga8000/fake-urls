from app import app

# Vercel serverless function handler
handler = app

# For Vercel deployment, we need to export the app
if __name__ == "__main__":
    app.run()
