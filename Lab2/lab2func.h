#ifndef LAB2FUN_H_
#define LAB2FUNC_H_

#include <msp430.h>

extern unsigned int ADC_value;

void gpio();
void adcSetup(void);
void adcReadConv(void);
void displaySeg(void);

#endif
