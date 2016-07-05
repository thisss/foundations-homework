from flask import Flask, jsonify, request
import pg8000

app = Flask(__name__)
conn = pg8000.connect(database="mondial", user="postgres", password="strongpassword")

@app.route("/lakes")
def get_lakes():
	cursor = conn.cursor()
	cursor.execute("SELECT name, elevation, area, type FROM lake ORDER BY name")
	if request.args['type','']:
		get_types()
	else:
		output = []
		for item in cursor.fetchall():
			temp_lake = {}
			temp_lake['name'] = item[0]
			try:
				temp_lake['elevation'] = int(item[1])
			except:
				temp_lake['elevation'] = None
			try:
				temp_lake['area'] = int(item[2])
			except:
				temp_lake['area'] = None
			try:
				temp_lake['type'] = int(item[3])
			except:
				temp_lake['type'] = None
			output.append(temp_lake)
		return jsonify(output)

def get_types():
		output = []
		lake_type = request.args['type']
		if lake_type == 'salt':
				cursor.execute('SELECT name, elevation, area, type FROM lake WHERE type=\'salt\'')
				output = lake_type
app.run()
