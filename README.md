# Keylogger
This is a keylogger that uses the keyboard library in python to record keystrokes, on the target computer. When "enter" is pressed a string is sent to the server.

NOTE 1: client-keylogger.py must be run as su/Administrator or with sudo privliges.
NOTE 2: client-keylogger.py only work on Windows and Linux

## Installation

##### Linux

  ```sudo pip install keyboard```

## Testing
- Works via local host (127.0.0.1)
- Target tested on Xubuntu-24-04 (Ubuntu based)
  - sudo was needed for security.

## Known bugs
- Some characters is sent as lowercase instead as uppercase
- When the client uses backspace the deleted characters is still sent to the server
