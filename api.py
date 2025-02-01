from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')  # Get all values for the 'name' parameter
    Marks = [marks.get(name, 0) for name in names]  # Fetch marks for each name
    return jsonify({"marks": Marks})

if __name__ == '__main__':
    app.run(debug=True)