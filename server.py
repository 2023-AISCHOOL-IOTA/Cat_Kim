import pymysql as ps
from flask import Flask, jsonify
import serial
from threading import Thread

# 병렬처리

ser = serial.Serial('COM3', 9600)

sensor_data = {
    'humidity': None,
    'temperature': None,
}


def read_sensor_data():
    global sensor_data
    while True:
        line = ser.readline().decode('utf-8').strip()
        humidity, temperature = map(float, line.split('\t'))
        sensor_data = {'humidity': humidity, 'temperature': temperature}


Thread(target=read_sensor_data).start()


conn = ps.connect()


def insert():
    return 'INSERT CLEAR'


def select():
    return 'SELECT'


app = Flask(__name__)


@app.route('/sensor_data', methods=['GET'])
def get_sensor_data():
    return jsonify(sensor_data)


if __name__ == '__main__':
    app.run(port=5000)
