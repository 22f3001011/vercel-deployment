from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Load the marks data from the JSON file
with open('q-vercel-python.json', 'r') as file:
    marks_data = json.load(file)

@app.route('/api', methods=['GET'])
def get_marks():
    names = request.args.getlist('name')  # Get all values for the 'name' parameter
    marks = []

    for name in names:
        # Find the marks for the given name
        student = next((item for item in marks_data if item["name"] == name), None)
        if student:
            marks.append(student["marks"])
        else:
            marks.append(0)  # Default to 0 if the name is not found

    return jsonify({"marks": marks})

if __name__ == '__main__':
    app.run(debug=True)