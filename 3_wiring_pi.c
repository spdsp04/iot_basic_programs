#include <wiringPi.h>

int main(void) {
    wiringPiSetup();      // Initialize WiringPi
    pinMode(0, OUTPUT);   // WiringPi pin 0 = BCM 17 = Physical 11

    while(1) {
        digitalWrite(0, HIGH);
        delay(500);
        digitalWrite(0, LOW);
        delay(500);
    }
}