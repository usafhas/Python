/* @file HelloKeypad.pde
|| @version 1.0
|| @author Alexander Brevig
|| @contact alexanderbrevig@gmail.com
||
|| @description
|| | Demonstrates the simplest use of the matrix Keypad library.
|| #
*/

/*
Keypad for Breifcase, using mattrix Keypad. Alarm system activates
Written and designed by usafhas@gmail.com

*/
#include <Keypad.h>

const byte ROWS = 4; //four rows
const byte COLS = 3; //three columns
char keys[ROWS][COLS] = {
  {'1','2','3'},
  {'4','5','6'},
  {'7','8','9'},
  {'*','0','#'}
};
byte rowPins[ROWS] = {5, 4, 3, 2}; //connect to the row pinouts of the keypad
byte colPins[COLS] = {8, 7, 6}; //connect to the column pinouts of the keypad

Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );

boolean Power = false;
int Blue = 12;
int Green = 11;
int Red = 13;
char key1;
char key2;
char key3;
boolean unlocked = false;

int Magnet = 0; /////////////
int Solenoid = 9;
int Speaker = 10; ////////
int Magnet_state;

char Code[] = {'4', '1', '7'};

void setup(){
  Serial.begin(9600);
  pinMode(Blue, OUTPUT);
  pinMode(Green, OUTPUT);
  pinMode(Red, OUTPUT);
  pinMode(Speaker, OUTPUT);
  pinMode(Magnet, INPUT);
  pinMode(Solenoid, OUTPUT);
}
  
void loop(){
  
  char key = keypad.getKey();
  Magnet_state = analogRead(Magnet);
  
  if (key != NO_KEY){
    Serial.println(key);
  }
  if(key == '*'){
    Power = true;
    digitalWrite(Blue, HIGH);
  }
  if(key == '#'){ 
  Lock();
  }
  
  //// Keypad get Code ///////////////////////////
  
  while(Power == true){
    key1 = keypad.getKey();
    
    while(key1 == NO_KEY){
      key1 = keypad.getKey();
      if(key1 == '#'){
       Lock();
        break;
        }
    }
      
      if(key1 == Code[0] && key1 != NO_KEY){
        key2 = keypad.getKey();
        
        while(key2 == NO_KEY){
          key2 = keypad.getKey();
            if(key2 == '#'){
              Lock();
                break;
                }
        }
        
          if(key2 = Code[1] && key2 != NO_KEY){
            key3 = keypad.getKey();
            
            while(key3 == NO_KEY){
              key3 = keypad.getKey();
                if(key3 == '#'){
                 Lock();
                 break;
                  }
            }
            
              if(key3 = Code[2] && key3 != NO_KEY){
                Unlock();
                break;
                
                
              }
              else{   
               Lock();
                break;
              }
            
          }
          else{   
               Lock();
                break;
          }  
          
      }
      else{   
                Lock();
                break;
      }
  }
  
  ////////// Alarm ///////////////////////////////
 Magnet_state = analogRead(Magnet);
  
  if(unlocked == false){
    
    if(Magnet_state >= 550){
      
     Alarm();  
     }
    }
////////////////////////////////////////////////////////     
}




void Lock(){
                digitalWrite(Solenoid, HIGH);
                digitalWrite(Red, HIGH);
                delay(500);
                digitalWrite(Red, LOW);
                delay(500);
                digitalWrite(Red, HIGH);
                delay(500);
                digitalWrite(Red, LOW);
                delay(500);
                digitalWrite(Red, HIGH);
                delay(500);
                digitalWrite(Red, LOW);
                delay(500);
                digitalWrite(Blue, LOW);
                Power = false;
                unlocked = false;
}

void Unlock(){
                unlocked = true;
                digitalWrite(Solenoid, LOW);
                digitalWrite(Green, HIGH);
                delay(500);
                digitalWrite(Green, LOW);
                delay(500);
                digitalWrite(Green, HIGH);
                delay(500);
                digitalWrite(Green, LOW);
                delay(500);
                digitalWrite(Green, HIGH);
                delay(500);
                digitalWrite(Green, LOW);
                delay(500);
                digitalWrite(Blue, LOW);
                Power = false;
}

void Alarm(){
 while(Magnet_state >= 550){
   
   for(int j = 0; j < 2; j += 1){

        for(int i = 800; i < 2000; i += 25){
        
        tone(Speaker, i);
        delay(75);
        
        }
        Magnet_state = analogRead(Magnet);
      
        for(int i = 2000; i > 800; i -= 25){
        
        tone(Speaker, i);
        delay(75);
        
        }
        
        Magnet_state = analogRead(Magnet);
      }
      
   for(int j = 0; j < 5; j +=1){
     
     tone(Speaker, 600);
     delay(500);
     tone(Speaker, 1800);
     delay(500);
     }
      
      
      
      Magnet_state = analogRead(Magnet);
 }
     
      noTone(Speaker);
}




/*
get_keu()
shiftIn()
switch... case....

*/
