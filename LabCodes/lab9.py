import lirc

try:
    with lirc.LircdConnection("irexec",) as conn:
        while True:
            string = conn.readline()
            print(string)

except KeyboardInterrupt:
    pass

lirc.deinit()
