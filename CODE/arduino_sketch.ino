// servo_ps5_multi.ino
// Drives four servos from commands sent over USB serial by ps5_servo_multi.py.
//
// Each command is one line: servo number, a colon, then the angle.
// "3:120" moves servo 3 to 120 degrees. A bare angle such as "90" moves servo 1.
//
// Servos don't jump straight to a new angle: each one moves toward it at the
// speed set in SPEED below, so motion is slower and smoother.
//
// Test without the Mac script: open Serial Monitor at 115200 baud,
// set line ending to "Newline", and type e.g. 1:0, 2:180, 3:90, 4:45.
//
// Wiring: each servo's brown -> GND, red -> 5V, orange -> its pin in SERVO_PIN.
// Power: four SG90s can draw more than the board can supply over USB. If the
// board resets or the servos jitter, power the servos' red wires from a separate
// 5V supply and connect that supply's ground to the Arduino's GND.

#include <Servo.h>

// ============================ SETTINGS (edit these) ============================
// One column per servo. Servo numbers 1-4 match CONTROLS in ps5_servo_multi.py.
//                           claw       elbow  shoulder  base
const int SERVO_PIN[]   = {    9,      10,     11,      12  };  // orange signal wire pin
const int MIN_ANGLE[]   = {   80,      100,      20,       0  };  // lowest angle allowed
const int MAX_ANGLE[]   = {  150,     170,     80,     180  };  // highest angle allowed
const int START_ANGLE[] = {  150,     100,     80,       0  };  // position on power-up
const int SPEED[]       = {  180,     180,    180,     180  };  // degrees per second:
                          // lower = slower and smoother (180 = 180 degrees in 1 second),
                          // 0 = no limit (jump straight to the new angle)

const long BAUD_RATE    = 115200;  // must match BAUD_RATE in ps5_servo_multi.py
const unsigned long UPDATE_MS = 20; // ms between small steps (20 matches the servo's own refresh)
// ===============================================================================

const int NUM_SERVOS = sizeof(SERVO_PIN) / sizeof(SERVO_PIN[0]);

Servo servos[NUM_SERVOS];
float current[NUM_SERVOS];   // where each servo is now
int   target[NUM_SERVOS];    // where each servo is heading
unsigned long lastUpdate = 0;

char buf[12];   // holds one incoming command, e.g. "3:120"
byte len = 0;

void setup() {
  Serial.begin(BAUD_RATE);
  for (int i = 0; i < NUM_SERVOS; i++) {
    current[i] = START_ANGLE[i];
    target[i]  = START_ANGLE[i];
    servos[i].attach(SERVO_PIN[i]);
    servos[i].write(START_ANGLE[i]);
  }
  lastUpdate = millis();
}

// Apply one complete command line held in buf: set that servo's target
void handleCommand() {
  buf[len] = '\0';

  int servoNumber = 1;           // no colon means servo 1
  char *angleText = buf;
  char *colon = strchr(buf, ':');
  if (colon) {
    *colon = '\0';
    servoNumber = atoi(buf);
    angleText = colon + 1;
  }
  if (*angleText == '\0') return;               // nothing after the colon

  int i = servoNumber - 1;
  if (i < 0 || i >= NUM_SERVOS) return;         // no such servo

  int angle = atoi(angleText);
  target[i] = constrain(angle, MIN_ANGLE[i], MAX_ANGLE[i]);
}

// Every UPDATE_MS, move each servo one small step toward its target
void updateServos() {
  unsigned long now = millis();
  if (now - lastUpdate < UPDATE_MS) return;
  float seconds = (now - lastUpdate) / 1000.0;
  lastUpdate = now;

  for (int i = 0; i < NUM_SERVOS; i++) {
    float remaining = target[i] - current[i];
    float maxStep = SPEED[i] * seconds;

    if (SPEED[i] <= 0 || fabs(remaining) <= maxStep) {
      current[i] = target[i];                   // close enough: arrive
    } else if (remaining > 0) {
      current[i] += maxStep;
    } else {
      current[i] -= maxStep;
    }
    servos[i].write((int)round(current[i]));
  }
}

void loop() {
  while (Serial.available()) {
    char c = Serial.read();

    if (c == '\n' || c == '\r') {
      if (len > 0) handleCommand();
      len = 0;
    } else if ((isDigit(c) || c == ':') && len < sizeof(buf) - 1) {
      buf[len++] = c;   // collect digits and the colon, ignore anything else
    }
  }

  updateServos();
}
