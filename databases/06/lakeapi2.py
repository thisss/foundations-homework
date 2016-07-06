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
    if lake_type !='' and lake_sort !='':
            cursor.execute("SELECT name, elevation, area, type FROM lake WHERE type=%s ORDER BY %s DESC", [lake_type, lake_sort])
    elif lake_type != '':
        cursor.execute("SELECT name, elevation, area, type FROM lake WHERE type=%s", [lake_type])
    elif lake_sort != '':
        print(lake_sort)
        cursor.execute("SELECT name, elevation, area, type FROM lake ORDER BY {} DESC".format(lake_sort))
#        cursor.execute("SELECT name, elevation, area, type FROM lake ORDER BY " + lake_sort + " DESC") #, [lake_sort])
    else:
        cursor.execute("SELECT name, elevation, area, type FROM lake ORDER BY name")
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

app.run()
# cursor.execute("SELECT name, elevation, area, type FROM lake")
