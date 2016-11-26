/*
 Example code for driving a single 7-segment display with
 a 74HC595 8-bit shift register
 
 The code cycles through the the entire 7-segment character
 set that was written by Eli McIlveen:
 
 (http://www.forgeryleague.com/lab/entry/arduino_7_segment_output/)
 
 In case of a COMMON ANODE display the bytes need to be inverted
 as shown in the loop() function: bitsToSend = bitsToSend ^ B11111111
 
 Hardware:
 
 * 74HC595 shift register attached to pins 2, 3, and 4 of the Arduino,
 as detailed below.
 
 * Pins to connect to common-cathode LED display via a 74HC595:
 DP-15, A-1, B-2, C-3, D-4, E-5, F-6, G-7 (shiftOut using LSBFIRST)
 Or:
 DP-7, A-6, B-5, C-4, D-3, E-2, F-1, G-15 (shiftOut using MSBFIRST)
 
 Created 12 October 2010
 by Ole Weidner (http://www.oleweidner.com/?p=434
 */

const byte ledCharSet[128] = //128
{
  // 00-0F: Hex digits
  B01111110, B00110000, B01101101, B01111001,	// 0123
  B00110011, B01011011, B01011111, B01110000,	// 4567
  B01111111, B01111011, B01110111, B00011111,	// 89AB
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

const int delayt = 7;


const int Speaker = 3;

int btn_min = 2;
int btn_sec = 4;
int btn_start = 5;

boolean start;

int Min_1 = 0;
int Min_2 = 0;
int Sec_1 = 0;
int Sec_2 = 0;
int i;
int j;
int m;
int k;



////////////////////////////////////////////////////////////////////////////////////////////////////
//
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
  pinMode(13, OUTPUT);
  pinMode(btn_min, INPUT);
  pinMode(btn_sec, INPUT);
  pinMode(btn_start, INPUT);
  start = false;

}

////////////////////////////////////////////////////////////////////////////////////////////////////
//
void loop() 
{

  while(start != true){
    //////////////////////////////////////////
    if(digitalRead(btn_min) == HIGH){
      delay(100);
      Min_1++;

      if(Min_1 == 10){
        Min_1 = 0;
        Min_2++;  
      }  
    }
    /////////////////////////////////////////////
    if(digitalRead(btn_sec) == HIGH){
      delay(100);
      Sec_1++;
      if(Sec_1 == 10){
        Sec_1 = 0;
        Sec_2++;
        if(Sec_2 == 6){
          Sec_2 = 0;
          Min_1++;
        }
      }
    }
    ////////////////////////////////////////////////
    if(digitalRead(btn_start) == HIGH){
      delay(100);
      start = true;
    } 
    
    byte temp = ledCharSet[Min_2];
    temp = temp ^ B11111111;
    byte temp1 = ledCharSet[Min_1];
    temp1 = temp1 ^ B11111111;
    byte temp2 = ledCharSet[Sec_2];
    temp2 = temp2 ^ B11111111;
    byte temp3 = ledCharSet[Sec_1];
    temp3 = temp3 ^ B11111111;
    
    
     /// Digit 1 ////////////////////////////////////////////////////   
            // turn off the output so the pins don't light up
            // while you're shifting bits:
            digitalWrite(latchPin, LOW);


            // shift the bits out:
            shiftOut(dataPin, clockPin, MSBFIRST, temp);

            // turn on the output so the LEDs can light up:
            digitalWrite(latchPin, HIGH);

            digitalWrite(faderPin, LOW);
            delay(delayt);
            digitalWrite(faderPin, HIGH);
            /////////////////////////////////////////////////////////////////
            // Digit 2 /////////////////////////////////////////////////////

            digitalWrite(latchPin, LOW);

            shiftOut(dataPin, clockPin, MSBFIRST, temp1);
            digitalWrite(latchPin, HIGH);

            digitalWrite(faderPin2, LOW);
            delay(delayt);
            digitalWrite(faderPin2, HIGH);

            ///////////////////////////////////////////////////////////////////
            // Digit 3 ///////////////////////////////////////////////////////

            digitalWrite(latchPin, LOW);

            shiftOut(dataPin, clockPin, MSBFIRST, temp2);
            digitalWrite(latchPin, HIGH);

            digitalWrite(faderPin3, LOW);
            delay(delayt);
            digitalWrite(faderPin3, HIGH);

            ///////////////////////////////////////////////////////////////////
            /// Digit 4 //////////////////////////////////////////////////////

            digitalWrite(latchPin, LOW);

            shiftOut(dataPin, clockPin, MSBFIRST, temp3);
            digitalWrite(latchPin, HIGH);

            digitalWrite(faderPin4, LOW);
            delay(delayt);
            digitalWrite(faderPin4, HIGH);
            ///////////////////////////////////////////////////////////////
i = Min_2;
j = Min_1;
k = Sec_2;
m = Sec_1;

  }



  for(i; i>= 0; --i)
  {

      
      
    for(j; j >= 0; --j){

    if(j == 0){
        if(i != 0){
        
        j = j + 10;
        }
      }
      if(j == 9){
        i = i - 1;
      }

      for(k; k >= 0; --k){

        if( k == 0){
          if(j != 0){
          j = j - 1;
          k = k + 6;
          }
        }

        for(m; m >= 0; --m){

          if(m == 0){
            if(k != 0){
            
            m = m + 10;
            }
           
          }
          if(m==9){
            k = k - 1;
          }
          
          
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
          

          for(int sec = 0; sec < 36; ++sec){

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


            if(i == 0 && j == 0 && k == 0 && m == 0){

              tone(Speaker, 2000);
              digitalWrite(13, HIGH);
              delay(500);
              digitalWrite(13, LOW);
              delay(500);
              digitalWrite(13, HIGH);
              delay(500);
              digitalWrite(13, LOW);
              delay(500);
              digitalWrite(13, HIGH);
              delay(500);
              digitalWrite(13, LOW);
              delay(500);
              noTone(Speaker);   
              ////////////////////////////

              for(int D = 0; D < 50; ++D){
                byte d = ledCharSet[13];
                d = d ^ B11111111;
                byte e = ledCharSet[14];
                e = e ^ B11111111;
                byte a = ledCharSet[10];
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
        }

        tone(Speaker, 1500, 10);
      }
      tone(Speaker, 1500, 10);
    }
  }
 
}






