import pymysql as ps

# MySQL 연결 설정
conn = ps.connect(host='project-db-stu3.smhrd.com', port=3307,
                  user='Insa4_IOTA_hacksim_4', password='aishcool4', database='Insa4_IOTA_hacksim_4')


def save_sensor_data(sensor_data):  # 센서 데이터 저장
    with conn.cursor() as curs:
        sql = 'INSERT INTO sensor(humidity, temperature, water_temp, water_detected) VALUES(%s, %s, %s, %s)'
        curs.execute(
            sql, (sensor_data['humidity'], sensor_data['temperature'], sensor_data['water_level'], sensor_data['water_detected']))
        conn.commit()


def get_sensor_data():  # 센서 데이터 조회
    with conn.cursor() as curs:
        sql = 'select * from sensor'
        curs.execute(sql)

        result = curs.fetchall()
        print(result)
        return result


def get_fish_data():
    with conn.cursor() as curs:
        sql = 'select * from fish'
        curs.execute(sql)

        result = curs.fetchall()
        print(result)
        return result


def get_plant_data():
    with conn.cursor() as curs:
        sql = 'select * from plant'
        curs.execute(sql)

        result = curs.fetchall()
        print(result)
        return result


# # 데이터 저장 및 조회 예제
# save_sensor_data({'humidity': 30.5, 'temperature': 25.0, 'water_level': 5.5})
# get_sensor_data()


# curs.close()
# conn.close()
