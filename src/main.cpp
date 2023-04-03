#include <Arduino.h>

/**********************************************************************
  Filename    : Joystick
  Description : Read data from joystick.
  Auther      : www.freenove.com
  Modification: 2020/07/11
**********************************************************************/
int xyzPins[] = {25, 26, 27};   //x,y,z pins
void setup() {
  Serial.begin(115200);
  pinMode(xyzPins[2], INPUT_PULLUP);  //z axis is a button.
  pinMode(25, INPUT_PULLUP); 
  pinMode(13, INPUT_PULLUP); 
}

void loop() {
  int xVal = analogRead(xyzPins[1]);
  int yVal = analogRead(xyzPins[2]);
  int zVal = digitalRead(25);
  int buttonVal = digitalRead(13);
  Serial.printf("X,Y,Z: %d,\t%d,\t%d, button: %d\n", xVal, yVal, zVal, buttonVal);
  delay(100);
}