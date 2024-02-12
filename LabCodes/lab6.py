import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

trigger_pin = 17
echo_pin = 18

# print('1')

GPIO.setup(trigger_pin, GPIO.OUT)
GPIO.setup(echo_pin, GPIO.IN)

try:
    while True:
        GPIO.output(trigger_pin, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(trigger_pin, GPIO.LOW)

        start_time = time.time()
        end_time = time.time()

        while GPIO.input(echo_pin) == 0:
            start_time = time.time()

        while GPIO.input(echo_pin) == 1:
            end_time = time.time()

        pulse_duration = end_time - start_time
        distance = (pulse_duration * 34300) / 2

        print("d: {:.2f} cm".format(distance))
        time.sleep(1)

except KeyboardInterrupt:
    print("Program terminated by user.")
    GPIO.cleanup()
