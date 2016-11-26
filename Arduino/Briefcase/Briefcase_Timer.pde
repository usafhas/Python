/*
works with Briefcase_Lock_Alarm sketch.
if briefcase is opened while locked Timer starts

*/

const byte ledCharSet[129] = //128
{
  // 00-0F: Hex digits
  B01111110, B00110000, B01101101, B01111001,	// 0123
  B00110011, B01011011, B01011111, B01110000,	// 4567
  B01111111, B01111011, B01111110, B01110111, B00011111,	// 890AB
  B01001110, B00111101, B01001111, B01000111,	// CDEF

  // 10-1F: Figure-8 drawing (8-character cycle)
  B01000000, B00100000, B00000001, B00000100,	// 1-segment
  B00001000, B00010000, B00000001, B00000010,

  B01100000, B00100001, B00000101, B00001100,	// 2-segment
  B00011000, B00010001, B00000011, B01000010,

  // 20-2F: Punctuation (barely recognizable!)
  B00000000, B10100000, B00100010, B00111111,	//  !"#
  B01011010, B01001001, B00000111, B00000010,	// $%&'
  B01001110, B01111000, B01100011, B00110001,	// ()*+
  B00010000, B00000001, B10000000, B00100101,	// ,-./

  // 30-3F: Decimal digits (alternate) and more punctuation
  B01111110, B00110000, B01101101, B01111001,	// 0123
  B00110011, B01011011, B00011111, B01110010,	// 4567
  B01111111, B01110011, B01001000, B01010000,	// 89:;
  B00001101, B00001001, B00011001, B11100000,	// <=>?

  // 40-5F: Capital letters and punctuation
  B01101110, B01110111, B00011111, B01001110,	// @ABC
  B01111100, B01001111, B01000111, B01011110,	// DEFG
  B00110111, B00000110, B00111100, B01010111,	// HIJK
  B00001110, B01110110, B00010101, B01111110,	// LMNO

  B01100111, B01110011, B01000110, B01011011,	// PQRS
  B01110000, B00111110, B00111110, B00101011,	// TUVW
  B01110101, B00111011, B01101101, B01001110,	// XYZ[
  B00010011, B01111000, B01100010, B00001000,	// \]^_

  // 60-7F: Lowercase letters and punctuation
  B01100000, B01111101, B00011111, B00001101,	// `abc
  B00111101, B01101111, B01000111, B01111011,	// defg
  B00010111, B00010000, B00011000, B00101111,	// hijk
  B00001100, B01010101, B01101010, B00011101,	// lmno

  B01100111, B01110011, B00000101, B00010011,	// pqrs
  B00001111, B00011100, B00100011, B01011101,	// tuvw
  B01101100, B00111011, B00100101, B01000011,	// xyz{
  B00110110, B01100001, B01000000, B11111111	// |}~
  
};

//// Pin connected to latch pin (ST_CP) of 74HC595
const int latchPin = 8;
//// Pin connected to clock pin (SH_CP) of 74HC595
const int clockPin = 12;
//// Pin connected to Data in (DS) of 74HC595
const int dataPin  = 11;
//// Pin connected to display's common annode
const int faderPin = 10; // digit 1
const int faderPin2 = 9; // digit 2
const int faderPin3 = 7; // digit 3
const int faderPin4 = 6; // digit 4
////////////////////////////////////////////////////////

const int delayt = 7; // int for delay between segments, lower = less blink
const int Speaker = 3; // piezobuzzer

//////////////////////////////////////////////////////////////
int Magnet = 0; /////////////
int Magnet_state = LOW;
int Red = 1;
int Red_state = LOW;
int Green = 2;
int Green_state = LOW;
int i=3;// 30 seconds
int j=0;
int m=0;//tenths
int k=0;
boolean unlocked = false;
boolean closed = true;
//////////////////////////////////
void setup() 
{
  Serial.begin(9600);
  
  pinMode(latchPin, OUTPUT);
  pinMode(clockPin, OUTPUT);
  pinMode(dataPin,  OUTPUT);
  pinMode(faderPin, OUTPUT); 
  pinMode(faderPin2, OUTPUT); 
  pinMode(faderPin3, OUTPUT);
  pinMode(faderPin4, OUTPUT);
  pinMode(Speaker, OUTPUT);
  pinMode(Magnet, INPUT);
  pinMode(Red, INPUT);
  pinMode(Green, INPUT);
  

}
////////////////////////////////////////////////////////////

void loop() 
{
  Magnet_state = analogRead(Magnet);
  if(Magnet_state >= 550){
    closed = false;
  } else{ closed = true; }
  
  Red_state = analogRead(Red);
  if(Red_state >= 550){
    unlocked = false;
  }
  
  Green_state = analogRead(Green);
  if(Green_state >= 550){
    unlocked = true;
  }
  
  
  
  
  if((closed == false) && (unlocked == false)){
  ////////////////////////////////////////////////////////////////
  for(i; i>= 0; --i)
  {
 
    for(j; j >= 0; --j){

    if((j == 0) && (i != 0)){

        j = j + 10;
        
      }
      if((j == 9) && (i != 0)){
        i--;
      }

      for(k; k >= 0; --k){

        if((( k == 0) && (m == 0)) && (j != 0)){
          
          j--;
          
          k = k + 6;
         
        }

        for(m; m >= -1; --m){

          if((m == 0) && (k != 0)){
            m = m + 10;
          }
          if((m == 9) && (k != 0)){
            k--;
          }
            for(int sec = 0; sec < 5; sec++){ // about a second at 36
                Update_LED();
              }//sec
               //////////////////////////////////////////////////////  
                    if(i == 0 && j == 0 && k == 0 && m == 0){
                        DEAD();
                        }
               //////////////////////////////////////////////////////
        }//m
      }//k
    }//j
  }//i
  
   ///////////////////////////////////////////////////
    Magnet_state = analogRead(Magnet);
  if(Magnet_state >= 550){
    closed = false;
  } else{ closed = true; }
  ////////////////////////////////////////////////////
  
  }// if 
 
}// loop

/////////////////////////////////////////////////////////////////////////////
void Update_LED(){
   byte bitsToSend = ledCharSet[i];
           // invert bitmas - we're using a common ANODE display. 
           // for common cathode, comment out the following line.
           bitsToSend = bitsToSend ^ B11111111;     
              byte bitsToSend2 = ledCharSet[j];
              bitsToSend2 = bitsToSend2 ^ B11111111;
                byte bitsToSend3 = ledCharSet[k];
                bitsToSend3 = bitsToSend3 ^ B11111111;
                  byte bitsToSend4 = ledCharSet[m];
                  bitsToSend4 = bitsToSend4 ^ B11111111;
                  
           /// Digit 1 ////////////////////////////////////////////////////   
            // turn off the output so the pins don't light up
            // while you're shifting bits:
            digitalWrite(latchPin, LOW);
            // shift the bits out:
            shiftOut(dataPin, clockPin, MSBFIRST, bitsToSend);

            // turn on the output so the LEDs can light up:
            digitalWrite(latchPin, HIGH);

            digitalWrite(faderPin, LOW);
            delay(delayt);
            digitalWrite(faderPin, HIGH);
            /////////////////////////////////////////////////////////////////
            // Digit 2 /////////////////////////////////////////////////////

            digitalWrite(latchPin, LOW);

            shiftOut(dataPin, clockPin, MSBFIRST, bitsToSend2);
            digitalWrite(latchPin, HIGH);

            digitalWrite(faderPin2, LOW);
            delay(delayt);
            digitalWrite(faderPin2, HIGH);

            ///////////////////////////////////////////////////////////////////
            // Digit 3 ///////////////////////////////////////////////////////

            digitalWrite(latchPin, LOW);

            shiftOut(dataPin, clockPin, MSBFIRST, bitsToSend3);
            digitalWrite(latchPin, HIGH);

            digitalWrite(faderPin3, LOW);
            delay(delayt);
            digitalWrite(faderPin3, HIGH);

            ///////////////////////////////////////////////////////////////////
            /// Digit 4 //////////////////////////////////////////////////////

            digitalWrite(latchPin, LOW);

            shiftOut(dataPin, clockPin, MSBFIRST, bitsToSend4);
            digitalWrite(latchPin, HIGH);

            digitalWrite(faderPin4, LOW);
            delay(delayt);
            digitalWrite(faderPin4, HIGH);
            ///////////////////////////////////////////////////////////////
}
////////////////////////////////////////////////////////////

/////////////////////////////////////////////////////////////
void DEAD(){
if((i == 0 && j == 0 && k == 0 && m == 0) && (closed = false)){
  
  Magnet_state = analogRead(Magnet);
  if(Magnet_state >= 550){
    closed = false;
  } else{ closed = true; }

                tone(Speaker, 2000);
              digitalWrite(13, HIGH);
              delay(500);
              digitalWrite(13, LOW);
              delay(500);
              noTone(Speaker); 
              ////////////////////////////

              for(int D = 0; D < 50; ++D){
                
                
                /////////////////////////////////////////////////
                byte d = ledCharSet[14];
                d = d ^ B11111111;
                byte e = ledCharSet[15];
                e = e ^ B11111111;
                byte a = ledCharSet[11];
                a = a ^ B11111111;

                digitalWrite(latchPin, LOW);

                shiftOut(dataPin, clockPin, MSBFIRST, d);
                digitalWrite(latchPin, HIGH);

                digitalWrite(faderPin, LOW);
                delay(delayt);
                digitalWrite(faderPin, HIGH);
                //////////////////////////////////////////

                digitalWrite(latchPin, LOW);

                shiftOut(dataPin, clockPin, MSBFIRST, e);
                digitalWrite(latchPin, HIGH);

                digitalWrite(faderPin2, LOW);
                delay(delayt);
                digitalWrite(faderPin2, HIGH);

                ///////////////////////////////////////////

                digitalWrite(latchPin, LOW);

                shiftOut(dataPin, clockPin, MSBFIRST, a);
                digitalWrite(latchPin, HIGH);

                digitalWrite(faderPin3, LOW);
                delay(delayt);
                digitalWrite(faderPin3, HIGH);

                ///////////////////////////////////////////

                digitalWrite(latchPin, LOW);

                shiftOut(dataPin, clockPin, MSBFIRST, d);
                digitalWrite(latchPin, HIGH);

                digitalWrite(faderPin4, LOW);
                delay(delayt);
                digitalWrite(faderPin4, HIGH);
                //////////////////////////////////////////////
              }
}
}
//////////////////////////////////////////////////////////////////////////

