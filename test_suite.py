import RPi.GPIO as GPIO
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import time

# Setup for LED
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

# Setup for MCP3008
SPI_PORT = 0
SPI_DEVICE = 0
light_sensor_Ch = 0
sound_sensor_Ch = 1
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT,SPI_DEVICE))

# Switch LED for 500ms interval
input("Press any key to do the test 1:")
for i in range(5):
	GPIO.output(11, GPIO.HIGH)
	time.sleep(0.5)
	GPIO.output(11, GPIO.LOW)
	time.sleep(0.5)

# Light sensor
input("Press any key to do the test 2:")
threshold = 500
interval = time.time()
while time.time() - interval < 5:
	light = mcp.read_adc(light_sensor_Ch)
	if light >= threshold:
		print("bright")
	else:
		print("dark")
	time.sleep(0.1)

# Switch LED for 200 interval
input("Press any key to do the test 3:")
GPIO.setmode(GPIO.BOARD)
for i in range(4):
        GPIO.output(11, GPIO.HIGH)
        time.sleep(0.2)
        GPIO.output(11, GPIO.LOW)
        time.sleep(0.2)

# Sound sensor
input("Press any key to do the test 4:")
interval = time.time()
while time.time() - interval < 5:
	GPIO.output(11, GPIO.LOW)
	sound = mcp.read_adc(sound_sensor_Ch)
	print(sound)
	if sound >= threshold:
                GPIO.output(11, GPIO.HIGH)
	time.sleep(0.1)

GPIO.cleanup()
