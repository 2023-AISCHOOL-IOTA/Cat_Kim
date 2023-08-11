# Serial port를 통해 입력받은 센서 값 전달
from flask import Flask, jsonify, request, Response, redirect, render_template
from flask_cors import CORS
# import serial as pyserial
import db
import json

# Flask 앱 인스턴스 생성
app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)


# 센서 데이터를 저장할 딕셔너리
sensor_data = {
    'humidity': None,
    'temperature': None,
    'water_temp': None,
    'water_detected': None
}

PORT = 'COM8'
BaudRate = 9600
TimeOut = 5


@app.route('/')  # 메인 페이지 라우트
def welcome():
    return render_template('index.html')


# @app.route('/sensor', methods=['GET'])
# def get_sensor_data_from_arduino():
#     with pyserial.Serial(port=PORT, baudrate=BaudRate, timeout=TimeOut) as ser:
#         line = ser.readline().decode('utf-8').strip()
#         values = line.split('\t')

#         if len(values) != 4:
#             return jsonify({"error": "Invalid data from sensor"}), 400
#         try:
#             humidity, temp_dht, temp_ds18b20, water_detected = map(
#                 int, line.split('\t'))
#             sensor_data.update({
#                 'humidity': humidity,
#                 'temperature': temp_dht,
#                 'water_temp': temp_ds18b20,
#                 'water_detected': water_detected
#             })

#             db.save_sensor_data(sensor_data)
#             return jsonify(sensor_data)

#         except ValueError:
#             return jsonify({"error": "Parsing error"}), 400

# DB 조회


@app.route('/db/<table_name>', methods=['GET'])
def view_data(table_name):
    if table_name == 'sensor':
        data = db.get_sensor_data()
        formatted_data = [
            {
                "code": item[0],
                "name": item[1],
                "value": item[2]
            }
            for item in data
        ]
    elif table_name == 'fish':
        data = db.get_fish_data()
        formatted_data = [
            {
                "code": item[0],
                "name": item[1],
                "description": item[2],
                "min_temp": item[3],
                "max_temp": item[4]
            }
            for item in data
        ]
    elif table_name == 'plant':
        data = db.get_plant_data()
        formatted_data = [
            {
                "code": item[0],
                "name": item[1],
                "description": item[2],
                "min_temp": item[3],
                "max_temp": item[4]
            }
            for item in data
        ]
    elif table_name == 'user':
        data = db.get_user_data()
        formatted_data = [
            {
                "code": item[0],
                "name": item[1],
                "description": item[2],
                "min_temp": item[3],
                "max_temp": item[4]
            }
            for item in data
        ]
    else:
        return jsonify({"error": "Invalid table name"}), 400

    # formatted_data = '<br>'.join(map(str, data))
    # return f"<a href=../../>Home</a><h1>DB Data</h1><pre>{formatted_data}</pre>"
    print(formatted_data)
    response_data = json.dumps(formatted_data, ensure_ascii=False)
    response = Response(
        response_data, content_type="application/json; charset=utf-8")
    return response

# DB 추가


@app.route('/db/add', methods=['POST'])
def add_to_db():
    humidity = request.form.get('humidity')
    temperature = request.form.get('temperature')
    water_level = request.form.get('water_level')
    water_detected = request.form.get('water_detected')

    if not all([humidity, temperature, water_level, water_detected]):
        return jsonify({"error": "All fields are required"}), 400

    data = {
        'humidity': humidity,
        'temperature': temperature,
        'water_level': water_level,
        'water_detected': water_detected
    }

    db.save_sensor_data(data)
    return redirect('/db/sensor')

# 검색


@app.route('/search/fish', methods=['POST'])
def search_fish():
    fish_name = request.form['fish_name']
    data = db.search_fish_data(fish_name)

    formatted_data = [
        {
            "code": item[0],
            "name": item[1],
            "description": item[2],
            "min_temp": item[3],
            "max_temp": item[4]
        }
        for item in data
    ]

    if data:
        return jsonify(formatted_data)
    else:
        return jsonify({"message": "No fish found with that name!"})


@app.route('/search/plant', methods=['POST'])
def search_plant():
    plant_name = request.form['plant_name']
    data = db.search_plant_data(plant_name)
    print(jsonify(data))
    # formatted_data = []

    # for item in data:
    #     try:
    #         formatted_data.append({
    #             "code": item[0],
    #             "name": item[1],
    #             "description": item[2],
    #             "min_temp": item[3],
    #             "max_temp": item[4]
    #         })
    #     except IndexError:
    #         formatted_data.append({
    #             "code": item[0] if len(item) > 0 else "N/A",
    #             "name": item[1] if len(item) > 1 else "N/A",
    #             "description": item[2] if len(item) > 2 else "N/A",
    #             "min_temp": item[3] if len(item) > 3 else "N/A",
    #             "max_temp": item[4] if len(item) > 4 else "N/A"
    #         })

    if data:
        return jsonify(data)
    else:
        return jsonify({"message": "No plant found with that name!"})


# Flask 앱 실행
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=9000, debug=True)
