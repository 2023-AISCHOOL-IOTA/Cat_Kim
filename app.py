# Serial port를 통해 입력받은 센서 값 전달
from flask import Flask, jsonify, request
import serial as pyserial
from threading import Thread
import bluetooth
import Cat_Kim.db as db

# 병렬처리

# Flask 앱 인스턴스 생성
app = Flask(__name__)


# 시리얼 포트 설정
#ser = pyserial.Serial(port='COM3', baudrate=9600)

# 센서 데이터를 저장할 딕셔너리
# 온도 습도 수위 외 추가해야 함
sensor_data = {
    'humidity': None,
    'temperature': None,
    'water_temp': None,
    'water_detected': None
}


def read_sensor_data():  # 센서 데이터 읽기 함수
    # 센서 데이터를 지속적으로 읽어 sensore_data에 저장
    global sensor_data
    while True:
        line = ser.readline().decode('utf-8').strip()  # 시리얼 포트에서 데이터 읽기
        try:
            humidity, temp_dht, temp_ds18b20, water_detected = map(
                int, line.split('\t'))  # 데이터 파싱
            sensor_data = {
                'humidity': humidity,
                'temperature': temp_dht,
                'water_temp': temp_ds18b20,
                'water_detected': water_detected}  # 전역 변수에 저장
        except ValueError:
            print(f"Failed to parse data: {line}")


# read_sensor_data 함수를 새로운 스레드에서 실행
#thread = Thread(target=read_sensor_data)
#thread.start()


@app.route('/')  # 메인 페이지 라우트
def welcome():
    return "Welcome to the Aqua Cycle Project!"


@app.route('/sensor', methods=['GET'])  # Flask route 설정
def get_sensor_data():
    # /sensor_data 경로로 GET 요청이 들어오면 센서 데이터를 JSON 형태로 반환
    return jsonify(sensor_data)


@app.route('/bt', methods=['GET'])
def connect_bluetooth():
    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    try:
        server_sock.bind(("", bluetooth.PORT_ANY))
        server_sock.listen(1)
        client_sock, client_info = server_sock.accept()
        data = client_sock.recv(1024).decode('utf-8').strip()
        try:
            humidity, temp_dht, temp_ds18b20, water_detected = map(
                int, data.split('\t'))
            sensor_data.update({
                'humidity': humidity,
                'temperature': temp_dht,
                'water_temp': temp_ds18b20,
                'water_detected': water_detected
            })
            print(
                f"Received data from Bluetooth: {sensor_data} \n from {client_info}")
        except ValueError:
            print(
                f"Failed to parse data: {data}. Expected format: 'humidity\ttemp_dht\ttemp_ds18b20\twater_detected'")
        client_sock.close()
    finally:
        server_sock.close()

    return f"Bluetooth connection ended."


# DB 함수 테스트
# DB 조회
@app.route('/db/view', methods=['GET'])
def view_db():
    data = db.get_sensor_data()
    # 데이터를 HTML 형식으로 보여줄 수 있도록 변환
    # 예를 들어, 간단하게 문자열 형태로 표시
    formatted_data = '<br>'.join(map(str, data))
    return f"<h1>DB Data</h1><pre>{formatted_data}</pre>"

# DB 추가


@app.route('/db/add', methods=['GET', 'POST'])
def add_to_db():
    if request.method == 'POST':
        humidity = request.form['humidity']
        temperature = request.form['temperature']
        water_level = request.form['water_level']
        water_detected = request.form['water_detected']

        data = {
            'humidity': humidity,
            'temperature': temperature,
            'water_level': water_level,
            'water_detected': water_detected
        }
        db.save_sensor_data(data)
        return redirect('/db/view')
    else:
        return '''
        <h1>Add Data to DB</h1>
        <form method="post">
            Humidity: <input type="text" name="humidity"><br>
            Temperature: <input type="text" name="temperature"><br>
            Water Level: <input type="text" name="water_level"><br>
            Water Detected: <input type="text" name="water_detected"><br>
            <input type="submit" value="Add to DB">
        </form>
        '''


def connect_bluetooth():
    server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    server_sock.settimeout(10)  # 10초 동안 대기
    try:
        server_sock.bind(("", bluetooth.PORT_ANY))
        server_sock.listen(1)
        client_sock, client_info = server_sock.accept()
        data = client_sock.recv(1024).decode('utf-8').strip()
        try:
            humidity, temp_dht, temp_ds18b20, water_detected = map(
                int, data.split('\t'))
            sensor_data.update({
                'humidity': humidity,
                'temperature': temp_dht,
                'water_temp': temp_ds18b20,
                'water_detected': water_detected
            })
            print(f"Received data from Bluetooth: {sensor_data}")
        except ValueError:
            print(
                f"Failed to parse data: {data}. Expected format: 'humidity\ttemp_dht\ttemp_ds18b20\twater_detected'")
        client_sock.close()
    except bluetooth.BluetoothError:
        return "Failed to connect to a Bluetooth device. Try again."
    finally:
        server_sock.close()

    return f"Bluetooth connection ended."


# Flask 앱 실행
if __name__ == '__main__':
    app.run(host="192.168.21.238", port=9000, debug=True)
