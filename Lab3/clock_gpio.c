#include "clock_gpio.h"
#include "PWM.h"
#include "UART.h"
#include "pin_common.h"

/*
 * clock_gpio.c
 *
 *  Created on: Sep 24, 2021
 *      Author: Eric
 */

const struct PinDescriptor RX = {GPIO_PORT_P1, GPIO_PIN1};
const struct PinDescriptor TX  = {GPIO_PORT_P1, GPIO_PIN2};

void gpio() {
    WDTCTL = WDTPW | WDTHOLD;   // stop watchdog timer

    //P1DIR |= 0x60;
    P2DIR |= 0x06;
}

void adcSetup(void) {

    ADC10CTL1 = INCH_0 + ADC10DIV_3;
    ADC10CTL0 = ADC10SHT_2 + ADC10ON + SREF_0;  // take samples for 2 clock cycles, adc10 on , set Vcc and Vss ref
    ADC10AE0 |= 0x08;                           // need to set after
}

void adcReadConv(void) {
    ADC10CTL0 |= ENC + ADC10SC;                 // enable conversion, start conversion
    ADC_value = ADC10MEM;                       // ADC value(10 bit so 1023), adcmem is where stored
}

