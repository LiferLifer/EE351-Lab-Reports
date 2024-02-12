import smbus
import math
import time

# 定义PCF8591的I2C地址和通道
pcf8591_address = 0x48
analog_channel = 0

# 初始化I2C总线
bus = smbus.SMBus(1)  # 使用I2C总线1

# 定义Steinhart-Hart方程的参数
R0 = 10000  # 标准温度下的电阻值 (10kΩ)
B = 3950    # 热敏电阻的热敏常数

while True:
    try:
        # 读取传感器的模拟输出通过A/D转换后的数字值
        analog_val = bus.read_byte_data(pcf8591_address, analog_channel)

        # 计算热敏电阻的原始模拟电压值
        Vr = 5.0 * float(analog_val) / 255

        # 计算热敏电阻值
        Rt = 10000 * Vr / (5 - Vr)

        # 使用Steinhart-Hart方程计算温度
        T0 = 298.15  # 标准温度 (25°C)
        T = 1 / (1 / T0 + (1 / B) * math.log(Rt / R0))

        # 温度转换为摄氏度
        temperature_celsius = T - 273.15

        # 打印温度值
        print("Now Temp: {:.2f} *C".format(temperature_celsius))

        time.sleep(0.5)

    except KeyboardInterrupt:
        break

bus.close()