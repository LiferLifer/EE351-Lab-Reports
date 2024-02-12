import RPi.GPIO as GPIO
import smbus
import time

# 设置GPIO模式为BCM
GPIO.setmode(GPIO.BCM)

# 定义LED引脚
x_led_pin = 18  # 用于表示X坐标的LED
y_led_pin = 17  # 用于表示Y坐标的LED

# 初始化LED引脚
GPIO.setup(x_led_pin, GPIO.OUT)
GPIO.setup(y_led_pin, GPIO.OUT)

# 初始化PWM对象
x_pwm = GPIO.PWM(x_led_pin, 100)  # 使用100Hz的频率
y_pwm = GPIO.PWM(y_led_pin, 100)

# 启动PWM
x_pwm.start(0)  # 初始亮度为0%
y_pwm.start(0)

# 初始化I2C总线
bus = smbus.SMBus(1)

# PCF8591的I2C地址
pcf8591_address = 0x48

# 读取PS2操纵杆的X和Y坐标以及按钮状态
def read_ps2_joystick():
    # 读取X坐标
    x_value = bus.read_byte_data(pcf8591_address, 1)
    # 读取Y坐标
    y_value = bus.read_byte_data(pcf8591_address, 0)
    return x_value, y_value

try:
    while True:
        x, y = read_ps2_joystick()

        # 使用X坐标的值来控制X坐标LED的亮度
        x_duty_cycle = (x / 255.0) * 100
        x_pwm.ChangeDutyCycle(x_duty_cycle)

        # 使用Y坐标的值来控制Y坐标LED的亮度
        y_duty_cycle = (y / 255.0) * 100
        y_pwm.ChangeDutyCycle(y_duty_cycle)

        # print(f"X: {x}, Y: {y}")

        time.sleep(0.1)

except KeyboardInterrupt:
    # 停止PWM并清理GPIO设置
    x_pwm.stop()
    y_pwm.stop()
    GPIO.cleanup()
    pass
