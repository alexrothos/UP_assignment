from app import app
from flask import request, jsonify
from json import dumps

@app.route("route")
def index():
    return "Server is running."

@app.route('/api', methods=['POST'])
def api():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        return jsonify(data)