from flask import Flask, jsonify, request
import pg8000

app = Flask(__name__)
conn = pg8000.connect(database="mondial", user='postgres', password='strongpassword')

# Main function: Getting all the lakes.
@app.route('/lakes')
def get_lakes():
    output = []
    cursor = conn.cursor()
    lake_type = request.args.get('type', '')
    lake_sort = request.args.get('sort', '')
    if lake_type !='':
        output = type_filter(lake_type, lake_sort, cursor)
        return jsonify(output)
    else:
        if lake_sort == 'elevation':
            cursor.execute('SELECT name, elevation, area, type FROM lake ORDER BY elevation DESC')
        elif lake_sort == 'area':
            cursor.execute('SELECT name, elevation, area, type FROM lake ORDER BY area DESC')
        else:
            cursor.execute('SELECT name, elevation, area, type FROM lake ORDER BY name')
        for item in cursor.fetchall():
            temp_lake = {}
            temp_lake['name'] = item[0]
            temp_lake['elevation'] = to_int(item[1])
            temp_lake['area'] = to_int(item[2])
            temp_lake['type'] = to_str(item[3])
            output.append(temp_lake)
        return jsonify(output)

# Function to convert values from the database into integers.
def to_int(number):
    try:
        return int(number)
    except:
        return None

# Function to convert values from the database into strings.
def to_str(string):
    try:
        return str(string)
    except:
        return None

# Function to filter according to the type value.
def type_filter(lake_type, lake_sort, cursor):
    output = []
    to_str(lake_type)
    if lake_type == 'salt':
        cursor.execute('SELECT name, elevation, area, type FROM lake WHERE type=\'salt\'')
        for item in cursor.fetchall():
            temp_salt = {}
            temp_salt['name'] = item[0]
            temp_salt['elevation'] = to_int(item[1])
            temp_salt['area'] = to_int(item[2])
            temp_salt['type'] = to_str(item[3])
            output.append(temp_salt)
        return output
    elif lake_type == 'dam':
        cursor.execute('SELECT name, elevation, area, type FROM lake WHERE type=\'dam\'')
        for item in cursor.fetchall():
            temp_dam = {}
            temp_dam['name'] = item[0]
            temp_dam['elevation'] = to_int(item[1])
            temp_dam['area'] = to_int(item[2])
            temp_dam['type'] = to_str(item[3])
            output.append(temp_dam)
        return output
    elif lake_type == 'caldera':
        if lake_sort == 'area':
            cursor.execute('SELECT name, elevation, area, type FROM lake WHERE type=\'caldera\' ORDER BY area DESC')
        else:
            cursor.execute('SELECT name, elevation, area, type FROM lake WHERE type=\'caldera\'')
        for item in cursor.fetchall():
            temp_caldera = {}
            temp_caldera['name'] = item[0]
            temp_caldera['elevation'] = to_int(item[1])
            temp_caldera['area'] = to_int(item[2])
            temp_caldera['type'] = to_str(item[3])
            output.append(temp_caldera)
        return output

app.run()
