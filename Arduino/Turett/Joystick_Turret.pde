// Controlling a servo position using a potentiometer (variable resistor) 
// by Michal Rinott <http://people.interaction-ivrea.it/m.rinott> 

#include <Servo.h> 

Servo Horiz;   
Servo Vert; 

int joy_H = 3;  // analog pin used to connect the potentiometer
int joy_V = 5;
int Trigger = 13;
int Click = 12;
int pos_V = 90;    // variable to store the servo position
int pos_H = 90;    // variable to store the servo position
void setup() 
{ 
  Horiz.attach(9);  // attaches the servo on pin 9 to the servo object
  Vert.attach(10);  // attaches the servo on pin 9 to the servo object
  pinMode(joy_H, INPUT);
  pinMode(joy_V, INPUT);
  pinMode(Trigger, OUTPUT);
  pinMode(Click, INPUT);
  Serial.begin(9600);

} 

void loop() 
{ 
  pos_H = analogRead(joy_H); 

  pos_V = analogRead(joy_V);  // reads the value of the potentiometer (value between 0 and 1023) 
  /*
  Serial.println("before");
  Serial.print(pos_H);
 Serial.println("  Horiz  "); 
  Serial.print(pos_V);
  Serial.println("  Vert  ");
  */
  
  pos_H = map(pos_H, 0, 1023, 0, 180); 
  pos_V = map(pos_V, 0, 1023, 0, 180);  // scale it to use it with the servo (value between 0 and 180) 
  
  
  // pos_H = map(pos_H, 0, 180, 70, 140); 
  // pos_V = map(pos_V, 0, 180, 85, 130);  // scale it to use it with the servo (value between 0 and 180) 
 /*
 Serial.println("after");
 Serial.print(pos_H); 
 Serial.println("  Horiz  "); 
 Serial.print(pos_V);
 Serial.println("  Vert  ");
 */

 if ( 70 <= pos_H && pos_H <= 140){
  
  Horiz.write(pos_H);
  delay(55); 
 }
 if( 85 <= pos_V && pos_V<= 130){
  Vert.write(pos_V);  // sets the servo position according to the scaled value 
  delay(55);
 }
  

  if(digitalRead(Click) == LOW){
    digitalWrite(Trigger, HIGH);
    delay(500);
    digitalWrite(Trigger, LOW);
  }

} 

