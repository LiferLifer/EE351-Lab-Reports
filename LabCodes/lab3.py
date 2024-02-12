import RPi.GPIO as GPIO
import time

# 设置GPIO模式为BCM
GPIO.setmode(GPIO.BCM)

# 定义GPIO口
button_pin = 26
led_pin_red = 19
led_pin_green = 13

# 设置GPIO口的模式
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led_pin_red, GPIO.OUT)
GPIO.setup(led_pin_green, GPIO.OUT)

# 定义LED状态
LED_OFF = 0
LED_RED_ON = 1
LED_RED_BLINK = 2
LED_GREEN_ON = 3
LED_GREEN_BLINK = 4

current_led_state = LED_OFF
GPIO.output(led_pin_red, GPIO.LOW)
GPIO.output(led_pin_green, GPIO.LOW)

now_time = time.perf_counter()

print("Init!")

def toggle_led_state():
    global current_led_state
    if current_led_state == LED_OFF:
        current_led_state = LED_RED_ON
        GPIO.output(led_pin_red, GPIO.HIGH)
    elif current_led_state == LED_RED_ON:
        current_led_state = LED_RED_BLINK
        now_time = time.perf_counter()
        # blink_led(led_pin_red)
    elif current_led_state == LED_RED_BLINK:
        current_led_state = LED_GREEN_ON
        GPIO.output(led_pin_red, GPIO.LOW)
        GPIO.output(led_pin_green, GPIO.HIGH)
    elif current_led_state == LED_GREEN_ON:
        current_led_state = LED_GREEN_BLINK
        # blink_led(led_pin_green)
        now_time = time.perf_counter()
    elif current_led_state == LED_GREEN_BLINK:
        current_led_state = LED_OFF
        GPIO.output(led_pin_red, GPIO.LOW)
        GPIO.output(led_pin_green, GPIO.LOW)

def blink_led(led_pin):
    for _ in range(10):
        GPIO.output(led_pin, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led_pin, GPIO.LOW)
        time.sleep(0.5)

try:
    while True:
        button_state = GPIO.input(button_pin)
        if button_state == GPIO.LOW:
            time.sleep(0.005)
            button_state = GPIO.input(button_pin)
            if button_state == GPIO.LOW:
                toggle_led_state()

        if current_led_state == LED_RED_BLINK:
            last_time = now_time
            now_time = time.perf_counter()
            if (now_time - last_time)*1000 > 250:
                GPIO.output(led_pin_red, not GPIO.input(led_pin_red))
        elif current_led_state == LED_GREEN_BLINK:
            last_time = now_time
            now_time = time.perf_counter()
            if (now_time - last_time)*1000 > 250:
                GPIO.output(led_pin_green, not GPIO.input(led_pin_green))

        time.sleep(0.3)

except KeyboardInterrupt:
    pass

# 清理GPIO口
GPIO.cleanup()