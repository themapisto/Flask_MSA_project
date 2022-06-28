from flask import Flask
from jinja2 import escape

app = Flask(__name__)
@app.route('/')
def index():
    return 'Hello'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')