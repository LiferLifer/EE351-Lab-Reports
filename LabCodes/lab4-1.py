import smbus
import time

bus = smbus.SMBus(1)

bus.write_byte(0x48, 0x40)
bus.read_byte(0x48)

while True:
    try:
        for i in range(0, 255):
            bus.write_byte_data(0x48, 0x40, i)
            time.sleep(0.01)
        for i in range(255, 0, -1):
            bus.write_byte_data(0x48, 0x40, i)
            time.sleep(0.01)

    except KeyboardInterrupt:
        break

bus.close()
