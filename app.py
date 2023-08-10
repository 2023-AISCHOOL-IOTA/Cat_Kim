# Serial port를 통해 입력받은 센서 값 전달
from flask import Flask, jsonify, request, redirect, render_template
import serial as pyserial
import db

# Flask 앱 인스턴스 생성
app = Flask(__name__)


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
    elif table_name == 'fish':
        data = db.get_fish_data()
    elif table_name == 'plant':
        data = db.get_plant_data()
    elif table_name == 'user':
        data = db.get_user_data()
    else:
        return jsonify({"error": "Invalid table name"}), 400

    formatted_data = '<br>'.join(map(str, data))
    return f"<a href=../../>Home</a><h1>DB Data</h1><pre>{formatted_data}</pre>"

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
    if data:
        return jsonify(data)
    else:
        return jsonify({"message": "No fish found with that name!"})


@app.route('/search/plant', methods=['POST'])
def search_plant():
    plant_name = request.form['plant_name']
    data = db.search_plant_data(plant_name)
    if data:
        return jsonify(data)
    else:
        return jsonify({"message": "No plant found with that name!"})


# Flask 앱 실행
if __name__ == '__main__':
    app.run(host="192.168.21.123", port=9000, debug=True)
