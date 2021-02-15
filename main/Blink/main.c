//make clean all target=raspberry


/**
 * @file       main.cpp
 * @author     Volodymyr Shymanskyy
 * @license    This project is released under the MIT License (MIT)
 * @copyright  Copyright (c) 2015 Volodymyr Shymanskyy
 * @date       Mar 2015
 * @brief
 */

//#define BLYNK_DEBUG
#define BLYNK_PRINT stdout
#ifdef RASPBERRY
  #include <BlynkApiWiringPi.h>
#else
  #include <BlynkApiLinux.h>
#endif
#include <BlynkSocket.h>
#include <BlynkOptionsParser.h>
//#include <stdlib.h>
//#include "grovepi.h"
//using namespace GrovePi;

static BlynkTransportSocket _blynkTransport;
BlynkSocket Blynk(_blynkTransport);

static const char *auth, *serv;
static uint16_t port;

//Wi-Pi difine
static int flag;
static int lock;
#include <BlynkWidgets.h>
#include <string.h>
#include <stdio.h>

//Grove LED difine
//static int LED_pin = 7;

BlynkTimer tmr;


/*テンプレ
 BLYNK_WRITE(ピン番号)
{
    printf("Got a value: %s\n", param[0].asStr()); 
}
備考としてparamに対してasInt() asFloat(),asDouble(),asStr(),getBuffer(),getLengh()が型変換で使える
 */
 
 
 /*
   
  */

BLYNK_WRITE(V1)
{    //Button switch
    flag=param[0].asInt();
   
   
    if(flag== 1){
        printf("wlan onnnnnnn");
        system("sudo ip l set wlan1 up");

		delay(1000);
        
    }
    else{
        printf("wlan offfffff");
        system("sudo ip l set wlan1 down");
        
		delay(1000);
    }
    
    
    
}

BLYNK_WRITE(V2){
    //ジェスチャー認識の方も起動するだけ
    //Button switch
    flag=param[0].asInt();
   
   
    if(flag== 1 && lock!=1){
        system("lxterminal -e python /home/pi/Desktop/Wi-Pi-System/main/Wi-Pi.py");
    }

    
    }

BLYNK_WRITE(V10){
    //ボタンロック
    //Button switch
    lock=param[0].asInt();
    }



BLYNK_WRITE(V101)
{
   //Button Switch  ボタンのONOFFみるだけ
   
   //ON、OFFで処理を切り替える
   flag=param[0].asInt();
   
   
    if(flag== 0){
        printf("OFFfffffffff\n");
    }
    else{
        printf("ONnnnnnnnnnn\n");
    }
}

BLYNK_WRITE(V102)
{
   //Button　push ボタンのONOFFをみるだけ
   
   //ON、OFFで処理を切り替える
   flag=param[0].asInt();
   
   
    if(flag== 0){
        printf("OFFfffffffff\n");
    }
    else{
        printf("ONnnnnnnnnnn\n");
    }
}

BLYNK_WRITE(V103)
{
    //LED１秒間で５点滅するだけ
    
    flag=param[0].asInt();   
   
    if(flag== 1){
        printf("Got a value: %s\n", param[0].asStr());
        printf("LED 1s");
        
        system("python /home/pi/blynk-library/scripts/groveled.py");
        
        //for (int num =0; num<5 ; num++){
            // 1 second the LED is HIGH -> ON
          //  digitalWrite(LED_pin, HIGH);
            //printf("[pin %d][LED ON]\n", LED_pin);
            //delay(500);
            // and another second LED is LOW -> OFF
            //digitalWrite(LED_pin, LOW);
            //printf("[pin %d][LED OFF]\n", LED_pin);
        //}
    }
    

}

void setup()
{
    Blynk.begin(auth, serv, port);
    tmr.setInterval(1000, [](){
      Blynk.virtualWrite(V0, BlynkMillis()/1000);
    });
    //initGrovePi(); // initialize communication w/ GrovePi
    delay(500); // wait 0.5 second
}

void loop()
{
    Blynk.run();
    tmr.run();
}


int main(int argc, char* argv[])
{
    parse_options(argc, argv, auth, serv, port);

    setup();
    while(true) {
        loop();
    }

    return 0;
}
