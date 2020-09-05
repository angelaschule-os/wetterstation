#!/usr/bin/env python
# encoding: utf-8

# SPDX-FileCopyrightText: © 2017 Matthias Messmer <matthias.messmer@angelaschule-osnabrueck.net>
# SPDX-License-Identifier: Apache-2.0

from serial import Serial, SEVENBITS, PARITY_EVEN, STOPBITS_ONE
from sys import stdout

# https://pyserial.readthedocs.io/en/latest/pyserial_api.html#serial.Serial
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
# https://pyserial.readthedocs.io/en/latest/pyserial_api.html#serial.Serial.rts
dmm.rts = False
# https://pyserial.readthedocs.io/en/latest/pyserial_api.html#serial.Serial.dtr
dmm.dtr = True

while True:
    # https://pyserial.readthedocs.io/en/latest/pyserial_api.html#serial.Serial.read
    s = dmm.read(1000)
    print(s)
    # You want unbuffered output whenever you want to ensure that the output
    # has been written before continuing. 
    stdout.flush()
