from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/flask-test', methods=['GET'])
def flast_test():
	return jsonify("Hello, World!")