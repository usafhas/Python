//Created By Heath Spidle
//USAFHAS@GMAIL.com

//Arduino powered servo with raspberry pi
//when raspberry pi pin is high, then the servo will rotate
//when second pin is high then the servo will rotate opposite
//"Bond" pans servo slowly through arc back and forth for a minute or two
//Future implement pan/tilt for camera, and/servo claw
//gm8 motor
//pin 17 RPI LEFT
//pin 27 RPI Right
//pin 4 RPI BOND

#include <Servo.h> 
#include <AFMotor.h>

Servo myservo;

int pos = 90; //servo 9
int left = 14; //pin for left //RPI 17
int right = 13; //pin for right  //RPI24
int bond = 2; //pin for bond //RPI4
AF_DCMotor left_motor(MOTOR12_1KHZ,1);//set my left
AF_DCMotor right_motor(MOTOR12_1KHZ, 2);//set my right
int lm = 16; //left motor from raspi gpio23
int rm = 17; //right motor from raspi gpio18
int back = 18; //backward from raspi gpio27
int forw = 19; //forward from raspi gpio4
//servo 9


int startleft;
int startright;
int startbond;
int valleft;
int valright;
int valbond;


void setup()
{
    Serial.begin(9600);
	myservo.attach(9);//Servo pin 9
	pinMode(left, INPUT);
	pinMode(right, INPUT);
	//pinMode(bond, INPUT);
        pinMode(lm, INPUT);
	pinMode(rm, INPUT);
	pinMode(back, INPUT);
        pinMode(forw, INPUT);

        startleft = digitalRead(left);
        startright = digitalRead(right);
        //startbond = digitalRead(bond);
        
        //setup motors
        left_motor.setSpeed(200);// 0 to 255
        right_motor.setSpeed(200);// 0 to 255
 
  left_motor.run(RELEASE);
  right_motor.run(RELEASE);
        
}

void loop()
{
  valleft = digitalRead(left);
  valright = digitalRead(right);
//  valbond = digitalRead(bond);
  

/*if(valbond == HIGH){
  for(int i = 0; i < 10; i +=1){
	for(pos = 20; pos <159; pos += 1)
	{
		myservo.write(pos);
		delay(100);
	}
	for(pos = 160; pos>20; pos -=1)
	{
		myservo.write(pos);
		delay(100);
	}
  }
  myservo.write(90);
}//end bond*/

if(valleft == HIGH){
	if(pos <= 170 && pos >= 11){
	myservo.write(pos);
	pos -= 1;
        delay(50);
       
	}

}//end left

if(valright == HIGH){
	if(pos >= 10 && pos <= 169){
	myservo.write(pos);
	pos += 1;
        delay(50);
        
	}

}//end right


//--------------------------------------------------------------------
int vallm = digitalRead(lm);
int valrm = digitalRead(rm);
int valforw = digitalRead(forw);
int valback = digitalRead(back);

if(vallm == HIGH){ // LEFT
 left_motor.run(FORWARD);
 right_motor.run(BACKWARD);
 delay(50); 
 left_motor.run(RELEASE);
 right_motor.run(RELEASE);
}
if(valrm == HIGH){ // RIGHT
 left_motor.run(BACKWARD);
 right_motor.run(FORWARD);
 delay(50); 
 left_motor.run(RELEASE);
 right_motor.run(RELEASE);
}
if(valforw == HIGH){ // RIGHT
 left_motor.run(FORWARD);
 right_motor.run(FORWARD);
 delay(50); 
 //left_motor.run(RELEASE);
// right_motor.run(RELEASE);
}
if(valback == HIGH){ // RIGHT
 left_motor.run(BACKWARD);
 right_motor.run(BACKWARD);
 delay(50); 
// left_motor.run(RELEASE);
// right_motor.run(RELEASE);
}


left_motor.run(RELEASE);
right_motor.run(RELEASE);
}
