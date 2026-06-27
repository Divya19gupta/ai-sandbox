from flask import Flask
from flask_cors import CORS
# Initialize Flask app (additionally exporting app if needed elsewhere)
app = Flask(__name__)
CORS(app, resources={
    r"/api/*": {
        "origins": "http://localhost:5173"
    }
})
x = 'random shit'

@app.route('/api/test')
def test():
    return x

if __name__ == '__main__':
    app.run(debug=True)
