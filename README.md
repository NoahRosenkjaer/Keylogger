# Keylogger
This is a keylogger that uses the [keyboard](https://pypi.org/project/keyboard/) library in python to record keystrokes, on the target computer. When "enter" is pressed a string is sent to the server, using socket.

NOTE 1: keylogger.py must be run as su or with sudo privliges on linux.

NOTE 2: keylogger.py only works on Windows and Linux

## Installation

#### Linux

  ```sudo pip install keyboard```

#### Windows

  ```pip install keyboard```

## Furture features
- Saving output
  - Save to file
    - ~~.txt~~
    - .json
  - Save to database
    - MongoDB
    - MySQL

## Testing
- Works via local host (127.0.0.1)
- Linux
  - Target tested on Xubuntu-24-04 (Ubuntu based)
    - sudo was needed for security.
- Windows
  - Target tested on Windows 11
    - Admin privliges was not needed so windows is less safe!

## Known bugs
- Some characters is sent as lowercase instead as uppercase
  - Spesifically: a, d, m, n, p, t, æ, ø, å
- When the client uses backspace the deleted characters is still sent to the server
