import pymysql as ps

conn = ps.connect(host='project-db-stu3.smhrd.com', port=3307,
                  user='Insa4_IOTA_hacksim_4', password='aishcool4', database='Insa4_IOTA_hacksim_4')

curs = conn.cursor()

sql = 'select * from member'
curs.execute(sql)

result = curs.fetchall()
print(result)

curs.close()
conn.close()
