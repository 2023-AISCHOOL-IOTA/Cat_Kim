import pymysql as ps

# MySQL 연결 설정
conn = ps.connect(host='project-db-stu3.smhrd.com', port=3307,
                  user='Insa4_IOTA_hacksim_4', password='aishcool4', database='Insa4_IOTA_hacksim_4')

sensor_data = [
    ('S0001', 'P_온도', 20),
    ('S0002', 'P_습도', 21),
    ('S0003', 'F_온도', 22),
    ('S0004', 'F_수위', 20)
]

def save_sensor_data():  # 측정된 센서 데이터 저장
    # sql 구문 수정해야 함
    sql = 'INSERT INTO sensor(sensor_code, sensor_name, sensor_result_value) VALUES(%s, %s, %s)'
    curs.executemany(sql, sensor_data)

    conn.commit()


def get_sensor_data():  # 센서 데이터 조회
    sql = 'select * from fish'
    curs.execute(sql)

    result = curs.fetchall()
    print(result)


# 데이터 저장 및 조회 예제
save_sensor_data()
# save_sensor_data({'humidity': 30.5, 'temperature': 25.0, 'water_level': 5.5})
# get_sensor_data()


curs.close()
conn.close()
