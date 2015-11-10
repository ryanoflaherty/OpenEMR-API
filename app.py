#!flask/bin/python
from flask import Flask, abort, jsonify, make_response, request, url_for
from flask.ext.httpauth import HTTPBasicAuth

app = Flask(__name__)

# Authorization handling
auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
	if username == 'admin':
		return 'pass'
	return none

@auth.error_handler
def unauthorized():
	return make_response(jsonify({'error': 'Unauthorized access'}), 403) # use 401 if we care about HTTP consistency (we dont)
	# return 403 instead of 401 to prevent browsers from displaying the default auth dialog

# Error handling, return 404 if page not found
@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)

@app.errorhandler(404)
def not_found(error):
	return make_response(jsonify({'error': 'Not Found'}), 404)

# Simple Database to hold patient data (Use an actual database IRL)
patients = [
    {
        'id': 1,
        'fname': u'Ryan',
        'lname': u'OFlaherty',
        'dob': u'11/19/1994',
        'height': 71,
        'weight': 185,
        'sex': u'Male'
    },
    {
        'id': 2,
        'fname': u'Joseph',
        'lname': u'Tierney',
        'dob': u'03/03/1994',
        'height': 72,
        'weight': 140,
        'sex': u'Male'
    }
]

# Function to return URI of patient instead of id #
def make_public_patient(patient):
    new_patient = {}
    for field in patient:
        if field == 'id':
            new_patient['uri'] = url_for('get_patient', patient_id=patient['id'], _external=True)
        else:
            new_patient[field] = patient[field]
    return new_patient

# Return all patient records
@app.route('/openemr/api/v0.0/patients', methods=['GET'])
# Uncomment if you want to require a pasword to use this function
# @auth.login_required
def get_patients():
    return jsonify({'patients': [make_public_patient(patient) for patient in patients]})

# Return a specific patient record based on id #
@app.route('/openemr/api/v0.0/patients/<int:patient_id>', methods=['GET'])
# Uncomment if you want to require a pasword to use this function
# @auth.login_required
def get_patient(patient_id):
    patient = [patient for patient in patients if patient['id'] == patient_id]
    if len(patient) == 0:
        abort(404)
    return jsonify({'patient': make_public_patient(patient[0])})

# Create a new patient record
@app.route('/openemr/api/v0.0/patients', methods=['POST'])
# Uncomment if you want to require a pasword to use this function
# @auth.login_required
def create_patient():
	if not request.json or not 'dob' in request.json:
		abort(404)
	patient = {
		'id': patients[-1]['id'] + 1,
        'fname': request.json['fname'],
        'lname': request.json['lname'],
        'dob': request.json['dob'],
        'height': request.json['height'],
        'weight': request.json['weight'],
        'sex': request.json['sex']
	}
	patients.append(patient)
	return jsonify({'patient': make_public_patient(patient)}), 201

# Update a patient record
@app.route('/openemr/api/v0.0/patients/<int:patient_id>', methods=['PUT'])
# Uncomment if you want to require a pasword to use this function
# @auth.login_required
def update_patient(patient_id):
	patient = [patient for patient in patients if patient['id'] == patient_id]
	if len(patient) == 0:
		abort(404)
	if not request.json:
		abort(400)
	if 'fname' in request.json and type(request.json['fname']) != unicode:
		abort(400)
	if 'lname' in request.json and type(request.json['lname']) != unicode:
		abort(400)
	if 'dob' in request.json and type(request.json['dob']) != unicode:
		abort(400)
	if 'sex' in request.json and type(request.json['sex']) != unicode:
		abort(400)
	patient[0]['fname'] = request.json.get('fname', patient[0]['fname'])
	patient[0]['lname'] = request.json.get('lname', patient[0]['lname'])
	patient[0]['dob'] = request.json.get('dob', patient[0]['dob'])
	patient[0]['height'] = request.json.get('height', patient[0]['height'])
	patient[0]['weight'] = request.json.get('weight', patient[0]['weight'])
	patient[0]['sex'] = request.json.get('sex', patient[0]['sex'])
	return jsonify({'patient': make_public_patient(patient[0])})

# Delete a patient record
@app.route('/openemr/api/v0.0/patients/<int:patient_id>', methods=['DELETE'])
# Uncomment if you want to require a pasword to use this function
# @auth.login_required
def delete_patient(patient_id):
    patient = [patient for patient in patients if patient['id'] == patient_id]
    if len(patient) == 0:
        abort(404)
    patients.remove(patient[0])
    return jsonify({'result': True})

if __name__ == '__main__':
	app.run(host='0.0.0.0')
