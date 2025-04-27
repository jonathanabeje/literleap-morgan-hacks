from flask import Flask, render_template
import logging
import traceback
import sys
from app import app

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger("debug_server")

# Wrap the app with error handlers
@app.errorhandler(Exception)
def handle_exception(e):
    logger.error(f"Unhandled exception: {str(e)}")
    logger.error(traceback.format_exc())
    return f"""
    <h1>Server Error</h1>
    <h2>{str(e)}</h2>
    <pre>{traceback.format_exc()}</pre>
    """, 500

if __name__ == '__main__':
    logger.info("Starting debug server on port 5003")
    app.run(debug=True, port=5003) 