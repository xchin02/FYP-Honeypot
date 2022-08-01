import time
import pymysql.cursors
from sense_hat import SenseHat

sense = SenseHat()

temperature = round(sense.get_temperature(), 1)
pressure = round(sense.get_pressure(), 1)
humidity = round(sense.get_humidity(), 1)

connection = pymysql.connect(host='192.168.10.50',
                             user='pi',
                             password='c300',
                             db='mydb',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:

        sql = "INSERT INTO data SET date=%s, time=%s, temperature=%s, pressure=%s, humidity=%s"
        cursor.execute(sql, (time.strftime("%Y-%m-%d"),time.strftime("%H:%M:%s"),float(temperature),float(pressure),float(humidity)))

    connection.commit()
finally:
    connection.close()
