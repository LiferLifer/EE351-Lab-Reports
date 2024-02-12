import smbus
import time

bus = smbus.SMBus(1)

bus.write_byte(0x48, 0x40)
bus.read_byte(0x48)

while True:
    try:
        value = bus.read_byte(0x48)
        print('value:', value)
        bus.write_byte_data(0x48, 0x40, value)
        time.sleep(0.5)

    except KeyboardInterrupt:
        break

bus.close()
