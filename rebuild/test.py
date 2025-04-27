from flask import Flask, render_template
import sys
import traceback

app = Flask(__name__)

@app.route('/test_reading')
def test_reading():
    """Test rendering the reading template"""
    try:
        return render_template('reading.html', 
                          interests=['Reading', 'Science'],
                          reading_level='medium')
    except Exception as e:
        error_info = {
            'exception': str(e),
            'traceback': traceback.format_exc()
        }
        return f"<pre>{error_info['exception']}\n\n{error_info['traceback']}</pre>"

if __name__ == '__main__':
    app.secret_key = "test-key"
    app.run(debug=True, port=5002) 