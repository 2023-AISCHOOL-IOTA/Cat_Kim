# Serial port를 통해 입력받은 센서 값 전달
from flask import Flask, jsonify
import serial
from threading import Thread

# 병렬처리

# 시리얼 포트 설정
ser = serial.Serial('COM3', 9600)

# 센서 데이터를 저장할 딕셔너리
# 온도 습도 수위 외 추가해야 함
sensor_data = {
    'humidity': None,
    'temperature': None,
    'water_level': None,
}


def read_sensor_data():  # 센서 데이터 읽기 함수
    # 병렬 처리를 위해 새로운 스레드에서 실행
    global sensor_data
    while True:
        line = ser.readline().decode('utf-8').strip()  # 시리얼 포트에서 데이터 읽기
        humidity, temperature = map(float, line.split('\t'))  # 데이터 파싱
        sensor_data = {'humidity': Humidity,
                       'temperature': temperatureC,
                       'water_level': water_level}  # 전역 변수에 저장


# read_sensor_data 함수를 새로운 스레드에서 실행
Thread(target=read_sensor_data).start()


app = Flask(__name__)


@app.route('/sensor_data', methods=['GET'])  # /sensor_data 경로에 대한 Flask route 설정
def get_sensor_data():
    # /sensor_data 경로로 GET 요청이 들어오면 센서 데이터를 JSON 형태로 반환
    return jsonify(sensor_data)

# Flask 앱 실행
if __name__ == '__main__':
    app.run(port=5000)
