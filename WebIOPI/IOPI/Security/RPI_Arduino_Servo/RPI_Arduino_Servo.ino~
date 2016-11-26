//Arduino powered servo with raspberry pi
//when raspberry pi pin is high, then the servo will rotate
//when a second pin is high then the servo will rotate opposite
//gm8 motor
//pin 17 RPI LEFT
//pin 27 RPI Right
//pin 4 RPI BOND

#include <Servo.h> 

Servo myservo;

int pos = 90;
int left = 6; //pin for left //RPI 17
int right = 7; //pin for right  //RPI24
int bond = 5; //pin for bond //RPI4
int startleft;
int startright;
int startbond;
int valleft;
int valright;
int valbond;

void setup()
{
	myservo.attach(9);//Servo pin 9
	pinMode(left, INPUT);
	pinMode(right, INPUT);
	pinMode(bond, INPUT);

        startleft = digitalRead(left);
        startright = digitalRead(right);
        startbond = digitalRead(bond);
        
}

void loop()
{
  valleft = digitalRead(left);
  valright = digitalRead(right);
  valbond = digitalRead(bond);
  

if(valbond == HIGH){
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
}//end bond

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

}
