#!/usr/bin/env python3
"""
ps5_servo_multi.py - read a PS5 controller on the Mac and drive four servos
on the Arduino running servo_ps5_multi.ino.

  Servo 1: left stick left/right
  Servo 2: right stick left/right
  Servo 3: L1 (held = one end, released = the other)
  Servo 4: L2 (how far you pull it sets the angle)

Press any button while it runs to see that button's number printed.
Quit the Arduino IDE first: only one program can use the port.
Press Ctrl+C to stop.
"""

import os
import sys
import time

# Let the controller be read from a terminal script with no window
os.environ["SDL_JOYSTICK_ALLOW_BACKGROUND_EVENTS"] = "1"
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "1"

import pygame
import serial
import serial.tools.list_ports
from enum import Enum

# ============================ SETTINGS (edit these) ============================
SERIAL_PORT = None     # None = find the Arduino automatically,
                       # or set it yourself, e.g. "/dev/cu.usbmodem1101"
BAUD_RATE   = 115200   # must match BAUD_RATE in servo_ps5_multi.ino
SEND_HZ     = 50       # how many times per second the servos are updated
DEADZONE    = 0.05     # sticks only: ignore tiny movement around the centre (0 to 1)

# One row per servo. "servo" is the number used in servo_ps5_multi.ino (1-4).
#   kind "stick"   - stick position sets the angle; centre = middle of the range
#   kind "trigger" - how far you pull sets the angle; released = min, full = max
#   kind "button"  - held = max, released = min
# "input" is pygame's axis number (stick, trigger) or button number (button)
# for a PS5 controller on a Mac. Set invert to True to flip the direction.


CONTROLS = [
    # servo  kind       input  min  max  invert      control
    (4,      "trigger", 5,     0,   180, False),   # L1 - BASE
    (3,      "stick",   3,     0,   180, True),   # right stick left/right - SHOULDER
    (2,      "stick",   1,     0,   180, False),   # left stick up/down - ELBOW
    (1,      "trigger", 4,     0,   180, True),   # L2 - CLAW
]
# ===============================================================================


def find_arduino_port():
    """Return the first serial port that looks like an Arduino, or None."""
    for p in serial.tools.list_ports.comports():
        if "usbmodem" in p.device or "Arduino" in (p.description or ""):
            return p.device
    return None


def check_controls(pad):
    """Stop with a clear message if CONTROLS names an input the controller lacks."""
    for servo, kind, index, *_ in CONTROLS:
        if kind == "button":
            available = pad.get_numbuttons()
        elif kind in ("stick", "trigger"):
            available = pad.get_numaxes()
        else:
            sys.exit(f"Servo {servo}: unknown kind '{kind}'. Use stick, trigger or button.")
        if not 0 <= index < available:
            sys.exit(f"Servo {servo}: {kind} input {index} doesn't exist on this "
                     f"controller (it has {available}). Change it in CONTROLS.")


def read_position(pad, kind, index):
    """Return where a control is, from 0.0 to 1.0."""
    if kind == "button":
        return 1.0 if pad.get_button(index) else 0.0
    value = pad.get_axis(index)                  # -1.0 to +1.0
    if kind == "stick" and abs(value) < DEADZONE:
        value = 0.0
    return (value + 1) / 2


def main():
    port = SERIAL_PORT or find_arduino_port()
    if not port:
        sys.exit("Arduino not found. Plug it in, or set SERIAL_PORT at the top of this file.")

    pygame.init()
    pygame.joystick.init()
    if pygame.joystick.get_count() == 0:
        sys.exit("No controller found. Check the PS5 controller is plugged in.")
    pad = pygame.joystick.Joystick(0)
    pad.init()
    check_controls(pad)
    print(f"Controller: {pad.get_name()}")

    try:
        arduino = serial.Serial(port, BAUD_RATE, timeout=0)
    except serial.SerialException as e:
        sys.exit(f"Could not open {port}: {e}\nIs the Arduino IDE still open?")
    time.sleep(2)  # give the board a moment in case opening the port reset it
    print(f"Arduino:    {port}")
    print("Sticks, L1 and L2 move the servos. Ctrl+C to quit.")

    last_sent = {}
    try:
        while True:
            for event in pygame.event.get():          # also refreshes controller state
                if event.type == pygame.JOYBUTTONDOWN:
                    print(f"button {event.button} pressed")

            for servo, kind, index, lo, hi, invert in CONTROLS:
                t = read_position(pad, kind, index)
                if invert:
                    t = 1 - t
                angle = round(lo + t * (hi - lo))
                if last_sent.get(servo) != angle:     # only send when it changes
                    arduino.write(f"{servo}:{angle}\n".encode())
                    last_sent[servo] = angle

            time.sleep(1 / SEND_HZ)
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        arduino.close()
        pygame.quit()


if __name__ == "__main__":
    main()
