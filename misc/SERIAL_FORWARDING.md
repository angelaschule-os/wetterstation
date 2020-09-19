# Serial forwarding

On raspberry pi:


pi@raspberrypi:~ $ socat /dev/ttyUSB0 tcp4-listen:23366

On the other pc:
socat  pty,link=tty0,raw  tcp:100.80.119.20:23366
