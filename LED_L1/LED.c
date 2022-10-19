#include <msp430.h>				


/**
 * blink.c
 */
void main(void)
{
	WDTCTL = WDTPW | WDTHOLD;		// stop watchdog timer
	P1DIR |= 0x01;			// configure P1.0 as output


	volatile unsigned int i;

    while(1)
    {
        if((P2IN&0x20)!=0x20) {         // if button pressed LED OFF
            P1OUT |= 0x01;              // toggle P1.0
            for(i=10000; i>0; i--);     // delay
        }
    }
}
