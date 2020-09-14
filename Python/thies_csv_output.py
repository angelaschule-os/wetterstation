#!/usr/bin/env python
# encoding: utf-8

# SPDX-FileCopyrightText: © 2017 Matthias Messmer <matthias.messmer@angelaschule-osnabrueck.net>
# SPDX-License-Identifier: Apache-2.0

from serial import Serial, SEVENBITS, PARITY_EVEN, STOPBITS_ONE
from sys import stdout
import csv

# https://pyserial.readthedocs.io/en/latest/pyserial_api.html#serial.Serial
# See docs/Datalogger MeteoLOG TDL14.pdf page 28.
dmm = Serial(
    port='/dev/ttyUSB0',
    baudrate=9600,
    bytesize=SEVENBITS,
    parity=PARITY_EVEN,
    stopbits=STOPBITS_ONE,
    xonxoff=False,
    rtscts=False,
    dsrdtr=False,
    inter_byte_timeout=None
)
# https://pyserial.readthedocs.io/en/latest/pyserial_api.html#serial.Serial.rts
dmm.rts = False
# https://pyserial.readthedocs.io/en/latest/pyserial_api.html#serial.Serial.dtr
dmm.dtr = True
# Clear the queue so that data doesn't overlap and create erroneous data points
dmm.flushInput()

while True:
    try:
        # https://pyserial.readthedocs.io/en/latest/pyserial_api.html#serial.Serial.readline
        # Lines are concluded with "CR LF". See docs/Datalogger MeteoLOG TDL14.pdf page 20.
        # https://developer.mozilla.org/de/docs/Glossary/CRLF
        #print(dmm.readline())
        ser_bytes = dmm.readline()
        decoded_bytes = str(ser_bytes[0:len(ser_bytes)-2].decode("utf-8"))
        print(decoded_bytes)
        # You want unbuffered output whenever you want to ensure that the output
        # has been written before continuing.
        with open("telegramm.csv","a") as f:
            writer = csv.writer(f,delimiter=",")
            writer.writerow(decoded_bytes.split())
    except:
        print("Keyboard Interrupt")
        break
