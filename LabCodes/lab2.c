#include <wiringPi.h>
#include <time.h>

int main()
{
	wiringPiSetup();
	pinMode(23, OUTPUT);
    pinMode(24, OUTPUT);
	while(1)
	{
		sleep(1);
		digitalWrite(23, 1);
        digitalWrite(24, 0);
		sleep(1);
        digitalWrite(24, 1);
		digitalWrite(23, 0);
	}
	return 0;
}
