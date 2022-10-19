#include "lab2func.h"

void gpio() {
    WDTCTL = WDTPW | WDTHOLD;   // stop watchdog timer

    P1SEL |= 0x01;
    P1DIR |= 0x60;
    P2DIR |= 0x37;
}

void adcSetup(void) {

    ADC10CTL1 = INCH_0 + ADC10DIV_3;
    ADC10CTL0 = ADC10SHT_2 + ADC10ON + SREF_0;  // take samples for 2 clock cycles, adc10 on , set Vcc and Vss ref
    ADC10AE0 |= 0x01;                           // need to set after
}

void adcReadConv(void) {
    ADC10CTL0 |= ENC + ADC10SC;                 // enable conversion, start conversion
    ADC_value = ADC10MEM;                       // ADC value(10 bit so 1023), adcmem is where stored

    displaySeg();
}

void displaySeg(void) {
    switch(ADC_value) {
    case 0 :
        P1OUT |= 0x60;
        P2OUT |= 0x27;
        break;
    case 1 :
        P1OUT |= 0x00;
        P2OUT |= 0x03;
        break;
    case 2 :
        P1OUT |= 0x60;
        P2OUT |= 0x15;
        break;
    case 3 :
        P1OUT |= 0x20;
        P2OUT |= 0x17;
        break;
    case 4 :
        P1OUT |= 0x00;
        P2OUT |= 0x33;
        break;
    case 5 :
        P1OUT |= 0x20;
        P2OUT |= 0x36;
        break;
    case 6 :
        P1OUT |= 0x60;
        P2OUT |= 0x36;
        break;
    case 7 :
        P1OUT |= 0x20;
        P2OUT |= 0x03;
        break;
    case 8 :
        P1OUT |= 0x60;
        P2OUT |= 0x37;
        break;
    case 9 :
        P1OUT |= 0x20;
        P2OUT |= 0x33;
        break;
    case 10 :
        P1OUT |= 0x60;
        P2OUT |= 0x33;
        break;
    case 11 :
        P1OUT |= 0x40;
        P2OUT |= 0x36;
        break;
    case 12 :
        P1OUT |= 0x60;
        P2OUT |= 0x24;
        break;
    case 13 :
        P1OUT |= 0x40;
        P2OUT |= 0x17;
        break;
    case 14 :
        P1OUT |= 0x60;
        P2OUT |= 0x34;
        break;
    case 15 :
        P1OUT |= 0x60;
        P2OUT |= 0x30;
        break;
    default :                       // Displays " - "
        P1OUT |= 0x00;
        P2OUT |= 0x10;
    }
}
