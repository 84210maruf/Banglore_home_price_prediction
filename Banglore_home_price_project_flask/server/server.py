from flask import Flask, request, jsonify
import utils

app = Flask(__name__)

#Function Decorators
@app.route('/hello')
def hello():
	return 'Hello'


#GET mean to fetch data from Backend to Website
#POST send the data from webiste forms to Backend
@app.route('/get_location_names')
def get_location_names():
	response = jsonify({
		'locations': utils.get_locations()
		})
	response.headers.add('Access-Control-Allow-Origin', '*')
	return response

#request.form collects the data from the website
@app.route('/predict_home_price', methods=['POST'])
def predict_home_price():
	bhk = int(request.form['bhk'])
	size = float(request.form['total_sqft'])
	n_bath = int(request.form['bath'])
	locn = request.form['location']

	response = jsonify({
		'Net_Price': utils.get_estimate_price(locn, size, bhk, n_bath)
		})
	response.headers.add('Access-Control-Allow-Origin', '*')

	return response


if __name__ == '__main__':
	print('Starting Flask server')
	#print("yaya", app, "yaya")
	utils.load_data()
	app.run(debug=True)
