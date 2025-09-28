from flask import Flask, request, jsonify

#flask server
app = Flask(__name__)

#temprature initial value 
temperature = {"value": 20}

#route to temprature page to get value 
@app.route('/temperature', methods=['GET'])
def get_temperature():
    return jsonify(temperature)

#route to temprature page to post new value 
@app.route('/temperature', methods=['POST'])
def update_temperature():
    new_value = request.json.get('value')
    if new_value is not None:
        temperature['value'] = new_value
        return jsonify({"message": "Temperature updated", "new_value": new_value})
    else:
        return jsonify({"error": "No value provided"}), 400

if __name__ == '__main__':
    app.run(debug=True)

