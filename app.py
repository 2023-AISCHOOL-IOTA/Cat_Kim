# Serial port를 통해 입력받은 센서 값 전달
from flask import Flask, jsonify, request
import serial as pyserial
from threading import Thread

# 병렬처리

# Flask 앱 인스턴스 생성
app = Flask(__name__)


# 시리얼 포트 설정
ser = pyserial.Serial(port='COM3', baudrate=9600)

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
thread = Thread(target=read_sensor_data)
thread.start()


@app.route('/')  # 메인 페이지 라우트
def welcome():
    return "Welcome to the Aqua Cycle Project!"


@app.route('/sensor', methods=['GET'])  # Flask route 설정
def get_sensor_data():
    # /sensor_data 경로로 GET 요청이 들어오면 센서 데이터를 JSON 형태로 반환
    return jsonify(sensor_data)


# Flask 앱 실행
if __name__ == '__main__':
    app.run(port=5000, debug=True)
