from app import app
from flask import request, jsonify
from json import dumps
from func import reach_for_data

@app.route("route")
def index():
    return "Server is running."

@app.route('/api', methods=['POST'])
def api():
    data = reach_for_data()
    return jsonify(data)