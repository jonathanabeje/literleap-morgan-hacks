import sys
import os
import traceback
from flask import Flask
from app import app

def start_server():
    """Start the Flask server with detailed error logs"""
    try:
        app.debug = True
        # Use a custom error handler
        @app.errorhandler(Exception)
        def handle_error(e):
            print(f"\nERROR: {str(e)}\n")
            print(traceback.format_exc())
            return f"""
            <h1>Server Error</h1>
            <p>{str(e)}</p>
            <pre>{traceback.format_exc()}</pre>
            """, 500
        
        # Ensure static folder exists
        static_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
        css_folder = os.path.join(static_folder, 'css')
        js_folder = os.path.join(static_folder, 'js')
        
        if not os.path.exists(css_folder):
            os.makedirs(css_folder)
        if not os.path.exists(js_folder):
            os.makedirs(js_folder)
        
        # Check template directory
        template_folder = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
        if not os.path.exists(template_folder):
            os.makedirs(template_folder)
        
        # List all template files
        print("\nAvailable templates:")
        for root, dirs, files in os.walk(template_folder):
            for file in files:
                print(f"  - {os.path.join(root, file)}")
        
        # Start the server
        print("\nStarting Flask server on port 5002...")
        app.run(host='127.0.0.1', port=5002)
        
    except Exception as e:
        print(f"Failed to start server: {e}")
        print(traceback.format_exc())

if __name__ == "__main__":
    start_server() 