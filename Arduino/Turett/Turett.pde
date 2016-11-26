// program for distance controlled Airsoft turrett.

#include <Servo.h> 
Servo Horiz;   
Servo Vert;  

 // PIR              
 /*
 int calibrationTime = 3;
 int pirPin = 3;	//the digital pin connected to the PIR sensor's out
 int on = 0;  // Time for PIR to stay on when motion is detected
 */


int pingPin = 7; 
int Trigger = 13;
const int Proximity = 10; // how close in inches to fire.

int pos_V = 90;    // variable to store the servo position
int pos_H = 90;    // variable to store the servo position

int duration, inches;

void setup() {
  // initialize serial communication:
  Serial.begin(9600);
  pinMode(13, OUTPUT);

  Horiz.attach(9);  // attaches the servo on pin 9 to the servo object
  Vert.attach(10);  // attaches the servo on pin 9 to the servo object



  /*
  // PIR
   pinMode(pirPin, INPUT);
   digitalWrite(pirPin, LOW);
   
   Serial.print("calibrating sensor ");
   for(int i = 0; i < calibrationTime; i++){ 
   Serial.print("."); 
   delay(1000);
   }
   Serial.println(" done");
   Serial.println("SENSOR ACTIVE"); 
   delay(50);
   
   
   */
}



void loop()
{
  // establish variables for duration of the ping, 
  // and the distance result in inches and centimeters:

  // if (pirPin == HIGH) {
  //   for(on; on < 300; on +=1) {

  // The PING))) is triggered by a HIGH pulse of 2 or more microseconds.
  // Give a short LOW pulse beforehand to ensure a clean HIGH pulse:
  pinMode(pingPin, OUTPUT);
  digitalWrite(pingPin, LOW);
  delayMicroseconds(2);
  digitalWrite(pingPin, HIGH);
  delayMicroseconds(5);
  digitalWrite(pingPin, LOW);

  // The same pin is used to read the signal from the PING))): a HIGH
  // pulse whose duration is the time (in microseconds) from the sending
  // of the ping to the reception of its echo off of an object.
  pinMode(pingPin, INPUT);
  duration = pulseIn(pingPin, HIGH);

  inches = microsecondsToInches(duration);
  Serial.print(inches);
  Serial.print("in, ");


  for(pos_H = 75; pos_H < 130; pos_H += 2)  // goes from 0 degrees to 180 degrees 
  {    
 
    Horiz.write(pos_H);              // tell servo to go to position in variable 'pos' 
    delay(15); 

delay(90);
    
  // The PING))) is triggered by a HIGH pulse of 2 or more microseconds.
  // Give a short LOW pulse beforehand to ensure a clean HIGH pulse:
  pinMode(pingPin, OUTPUT);
  digitalWrite(pingPin, LOW);
  delayMicroseconds(2);
  digitalWrite(pingPin, HIGH);
  delayMicroseconds(5);
  digitalWrite(pingPin, LOW);

  // The same pin is used to read the signal from the PING))): a HIGH
  // pulse whose duration is the time (in microseconds) from the sending
  // of the ping to the reception of its echo off of an object.
  pinMode(pingPin, INPUT);
  duration = pulseIn(pingPin, HIGH);
 


  inches = microsecondsToInches(duration);
  
  delay(90);

    if (inches <= Proximity && inches > 0){
      Fire();
    }
    delay(10);

  }

  for(pos_H = 130; pos_H>= 75; pos_H -= 2)     // goes from 180 degrees to 0 degrees 
  {          

  
       
    Horiz.write(pos_H);              // tell servo to go to position in variable 'pos' 
    delay(15); 

delay(90);
    
  // The PING))) is triggered by a HIGH pulse of 2 or more microseconds.
  // Give a short LOW pulse beforehand to ensure a clean HIGH pulse:
  pinMode(pingPin, OUTPUT);
  digitalWrite(pingPin, LOW);
  delayMicroseconds(2);
  digitalWrite(pingPin, HIGH);
  delayMicroseconds(5);
  digitalWrite(pingPin, LOW);

  // The same pin is used to read the signal from the PING))): a HIGH
  // pulse whose duration is the time (in microseconds) from the sending
  // of the ping to the reception of its echo off of an object.
  pinMode(pingPin, INPUT);
  duration = pulseIn(pingPin, HIGH);


  inches = microsecondsToInches(duration);
  
delay(90);
  
    if (inches <= Proximity && inches > 0){
      Fire();
    }
    delay(10);
  } 

}



void Fire(){


  digitalWrite(Trigger, HIGH);


  for(pos_V = 90; pos_V < 110; pos_V += 1)  // goes from 0 degrees to 180 degrees 
  {                                  // in steps of 1 degree 
    Vert.write(pos_V);              // tell servo to go to position in variable 'pos' 
    delay(35);                       // waits 15ms for the servo to reach the position 
  } 
  for(pos_V = 110; pos_V>=90; pos_V-=1)     // goes from 180 degrees to 0 degrees 
  {                                
    Vert.write(pos_V);              // tell servo to go to position in variable 'pos' 
    delay(35);

  }
  digitalWrite(Trigger, LOW);  

  delay(500);      // waits 15ms for the servo to reach the position 
}

long microsecondsToInches(long microseconds) {
  // According to Parallax's datasheet for the PING))), there are
  // 73.746 microseconds per inch (i.e. sound travels at 1130 feet per
  // second).  This gives the distance travelled by the ping, outbound
  // and return, so we divide by 2 to get the distance of the obstacle.
  // See: http://www.parallax.com/dl/docs/prod/acc/28015-PING-v1.3.pdf
  return microseconds / 74 / 2;
}





