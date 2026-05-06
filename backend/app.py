from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    return jsonify({
        "status": "ok",
        "message": "Backend is running"
    })

@app.route('/submit', methods=['POST'])
def submit():
    data = request.get_json(force=True, silent=True)
    if not data:
        return jsonify({
            "status": "error",
            "message": "Invalid or missing JSON payload"
        }), 400

    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    response = {
        "status": "success",
        "message": f"Received data from {name}",
        "data": {
            "email": email,
            "message": message
        }
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)