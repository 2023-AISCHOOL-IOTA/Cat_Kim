import pymysql as ps

# MySQL 연결 설정
conn = ps.connect(host='project-db-stu3.smhrd.com', port=3307,
                  user='Insa4_IOTA_hacksim_4', password='aishcool4', database='Insa4_IOTA_hacksim_4')

curs = conn.cursor()


def save_sensor_data(sensor_data):  # 측정된 센서 데이터 저장
    # sql 구문 수정해야 함
    sql = 'INSERT INTO sensor(humidity, temperature, water_level) VALUES(%s, %s, %s)'
    curs.execute(
        sql, (sensor_data['humidity'], sensor_data['temperature'], sensor_data['water_level']))
    conn.commit()


def get_sensor_data():  # 센서 데이터 조회
    sql = 'select * from fish'
    curs.execute(sql)

    result = curs.fetchall()
    print(result)


# 데이터 저장 및 조회 예제
save_sensor_data({'humidity': 30.5, 'temperature': 25.0, 'water_level': 5.5})
get_sensor_data()


curs.close()
conn.close()
