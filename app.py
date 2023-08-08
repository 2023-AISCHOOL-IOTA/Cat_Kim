# Serial port를 통해 입력받은 센서 값 전달
from flask import Flask, jsonify
import serial as pyserial


# 병렬처리

# Flask 앱 인스턴스 생성
app = Flask(__name__)


# 블루투스 서비스 설정
# server_sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
# server_sock.bind(("", bluetooth.PORT_ANY))
# server_sock.listen(1)

# 센서 데이터를 저장할 딕셔너리
# 온도 습도 수위 외 추가해야 함
sensor_data = {
    'humidity': None,
    'temperature': None,
    'water_temp': None,
    'water_detected': None
}
print(sensor_data)


@app.route('/')  # 메인 페이지 라우트
def welcome():
    return "Welcome to the Aqua Cycle Project!"


@app.route('/sensor', methods=['GET'])
def get_sensor_data_from_arduino():
    with pyserial.Serial(port='COM8', baudrate=9600, timeout=5) as ser:
        line = ser.readline().decode('utf-8').strip()
        try:
            humidity, temp_dht, temp_ds18b20, water_detected = map(
                int, line.split('\t'))
            sensor_data.update({
                'humidity': humidity,
                'temperature': temp_dht,
                'water_temp': temp_ds18b20,
                'water_detected': water_detected
            })
            print(sensor_data)
        except ValueError:
            print(
                f"Failed to parse data: {line}. Expected format: 'humidity\ttemp_dht\ttemp_ds18b20\twater_detected'")
    return jsonify(sensor_data)


@app.route('/bluetooth-connect', methods=['GET'])
def connect_bluetooth():
    #  with bluetooth.BluetoothSocket(bluetooth.RFCOMM) as server_sock:
    #     server_sock.bind(("", bluetooth.PORT_ANY))
    #     server_sock.listen(1)
    #     client_sock, client_info = server_sock.accept()
    return f"Bluetooth connection established. Update with actual logic."


# Flask 앱 실행
if __name__ == '__main__':
    app.run(port=9000, debug=True)
