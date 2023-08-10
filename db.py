import pymysql as ps

# MySQL 연결 설정
conn = ps.connect(host='project-db-stu3.smhrd.com', port=3307,
                  user='Insa4_IOTA_hacksim_4', password='aishcool4', database='Insa4_IOTA_hacksim_4')


def save_sensor_data(sensor_data):  # 센서 데이터 저장
    try:
        with conn.cursor() as curs:
            sql = 'INSERT INTO sensor(sensor_code, sensor_name, sensor_result_value) VALUES (%s, %s, %s)'
            curs.executemany(
                sql, sensor_data)
            conn.commit()
    except Exception as e:
        print("Error saving sensor data: ", e)


def get_sensor_data():  # sensor 데이터 조회
    try:
        with conn.cursor() as curs:
            sql = 'select * from sensor'
            curs.execute(sql)

            result = curs.fetchall()
            return result
    except Exception as e:
        print(f"Error fetching sensor data: {e}")
        return []


def get_fish_data():  # fish 데이터 조회
    try:
        with conn.cursor() as curs:
            sql = 'select * from fish'
            curs.execute(sql)

            result = curs.fetchall()
            return result
    except Exception as e:
        print(f"Error fetching fish data: {e}")
        return []


def get_plant_data():  # plant 조회
    try:
        with conn.cursor() as curs:
            sql = 'select * from plant'
            curs.execute(sql)
            result = curs.fetchall()
            return result
    except Exception as e:
        print(f"Error fetching plant data: {e}")
        return []


def get_user_data():  # user 조회
    try:
        with conn.cursor() as curs:
            sql = 'select * from user'
            curs.execute(sql)
            result = curs.fetchall()
            return result
    except Exception as e:
        print(f"Error fetching user data: {e}")
        return []


def search_fish_data(fish_name):
    with conn.cursor() as curs:
        sql = 'SELECT * FROM fish WHERE fish_name = %s'
        curs.execute(sql, fish_name)
        result = curs.fetchone()
        return result


def search_plant_data(plant_name):
    with conn.cursor() as curs:
        sql = 'SELECT * FROM plant WHERE plant_name = %s'
        curs.execute(sql, plant_name)
        result = curs.fetchone()
        return result


def close_connection():
    conn.close()


if __name__ == "__main__":

    # Example usage:
    # sensor_data = [
    #     ('S0001', 'P_온도', 20),
    #     ('S0002', 'P_습도', 21),
    #     ('S0003', 'F_온도', 22),
    #     ('S0004', 'F_수위', 20)
    # ]

    # save_sensor_data(sensor_data)
    # print(get_sensor_data())

    close_connection()
