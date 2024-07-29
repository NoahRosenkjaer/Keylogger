# Keylogger
This is a keylogger that uses the [keyboard](https://pypi.org/project/keyboard/) library in python to record keystrokes, on the target computer. When "enter" is pressed a string is sent to the server, using socket.

NOTE 1: keylogger.py must be run as su or with sudo privliges on linux.

## Installation

#### Linux

  ```sudo pip install keyboard```

#### Windows

  ```pip install keyboard```

## Furture features
- Saving output
  - Save to file
    - ~~.txt~~
  - Save to database
    - ~~MongoDB (Using a docker instance)~~
      - Make it a Time-Series Database (Use datetime)
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
- When the client uses backspace the deleted characters is still sent to the server (Maybe not bug but feature?)

## Thoughts
- Maybe the roles should be reversed to the keylogger is the server and the server becomes the client?
  - This would make it more use full in a real world senario, where the attacker connects to the target any time they want to look at what the target is typing.
  - Right now the target connects to the attacker.
