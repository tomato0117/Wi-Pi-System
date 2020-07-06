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

static BlynkTransportSocket _blynkTransport;
BlynkSocket Blynk(_blynkTransport);

static const char *auth, *serv;
static uint16_t port;

//Wi-Pi difine
static int flag;
#include <BlynkWidgets.h>
#include <string.h>
#include <stdio.h>

BlynkTimer tmr;

BLYNK_WRITE(V1)
{
    printf("Got a value: %s\n", param[0].asStr());
}

BLYNK_WRITE(V2)
{
    printf("ip aGot a value: %s\n", param[0].asStr());
    //system("python /home/pi/Desktop/ir/test/led.py");
}


//BLYNK_WRITE(V10)
//{
 //  printf("ls Got a value: %s\n", param[0].asStr());
  //  system("irsend SEND_ONCE lg on");
//}

BLYNK_WRITE(V3)
{
   //printf("ls Got a value: %s\n\n\n\n", param[0].asStr());
   flag=param[0].asInt();
   
    if(flag== 0){
        printf("OFFfffffffff\n");
    }
    else{
        printf("ONnnnnnnnnnn\n");
    }
}


void setup()
{
    Blynk.begin(auth, serv, port);
    tmr.setInterval(1000, [](){
      Blynk.virtualWrite(V0, BlynkMillis()/1000);
    });
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

