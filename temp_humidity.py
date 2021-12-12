import time
import Adafruit_DHT
from Adafruit_IO import Client, Feed

DHT_DATA_PIN = 4

ADAFRUIT_IO_KEY = "aio_PKqO37GFSQP3VA3l2gzOXdOoSuo9"
ADAFRUIT_IO_USERNAME = "glimp"

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)
temperature_feed = aio.feeds('temperature')
humidity_feed = aio.feeds('humidity')

dht22_sensor = Adafruit_DHT.DHT22

while True:
	humidity, temperature = Adafruit_DHT.read_retry(dht22_sensor, DHT_DATA_PIN)
	if humidity is not None and temperature is not None:
		print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature, humidity))
		temperature = '%.2f'%(temperature)
		humidity = '%.2f'%(humidity)
		aio.send(temperature_feed.key, str(temperature))
		aio.send(humidity_feed.key, str(humidity))
		time.sleep(10)

	else:
		print('Failed to retrieve DHT22 data')

