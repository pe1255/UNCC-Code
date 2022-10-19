#include <msp430.h> 
#include "UART.h"
#include "clock_gpio.h"
#include "common.h"
#include "pin_common.h"
#include "DIN.h"
#include "DOUT.h"
#include "PWM.h"

/*
 * main.c
 *
 *  Created on: Sep 24, 2021
 *      Author: Eric
 */

unsigned int ADC_value = 0;

void main(void)
{   gpio();
    adcSetup();
    uartInit();



    while(1) {
        uartTransmitChar();
        uartReceiveChar();
        P2OUT |= 0x06;
    }
}
