from serial import *
from time import sleep

dmm = Serial(
    port='/dev/ttyUSB0', 
    baudrate=9600, 
    bytesize=SEVENBITS, 
    parity=PARITY_EVEN, 
    stopbits=STOPBITS_ONE, 
    timeout=0.5,                      # in Sekunden
    xonxoff=False, 
    rtscts=False, 
    write_timeout=1,                # in Sekunden
    dsrdtr=False, 
    inter_byte_timeout=None
)
dmm.rts = False
dmm.dtr = True

while True:
    s = dmm.read(1000)
    print(s)
#    sleep(0.1)
