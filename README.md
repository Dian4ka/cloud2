# Flask Cloud App

This is a simple Flask app deployed on Render with basic CRUD operations.

## Setup and Deployment

1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Run locally:
   ```
   python app.py
   ```

3. Deploy to Render:
   - Create a new Render web service.
   - Use `requirements.txt` for dependencies.
   - Use `Procfile` for the start command.
   ```
   web: gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```
   - Deploy and access your app.
#   c l o u d 2  
 