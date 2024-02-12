import lirc
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)

LED_OFF = 0
LED_RED_ON = 1
LED_GREEN_ON = 2

current_led_state = LED_OFF

def toggle_led_state():
    global current_led_state
    if current_led_state == LED_OFF:
        current_led_state = LED_RED_ON
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(19, GPIO.LOW)
    elif current_led_state == LED_RED_ON:
        current_led_state = LED_GREEN_ON
        GPIO.output(19, GPIO.HIGH)
        GPIO.output(13, GPIO.LOW)
    elif current_led_state == LED_GREEN_ON:
        current_led_state = LED_OFF
        GPIO.output(13, GPIO.LOW)
        GPIO.output(19, GPIO.LOW)

try:
    with lirc.LircdConnection("irexec",) as conn:
        while True:
            string = conn.readline()
            print(string)
            if string == "echo \"KEY_OK\"":
                toggle_led_state()
                time.sleep(0.25)

except KeyboardInterrupt:
    pass
