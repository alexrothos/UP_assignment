from flask import Flask, request, jsonify
from json import dumps

app = Flask(__name__)



@app.route('/api', methods=['POST'])
def api():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
