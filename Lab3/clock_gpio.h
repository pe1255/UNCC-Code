/*
 * clock_gpio.h
 *
 *  Created on: Sep 24, 2021
 *      Author: Eric
 */

#ifndef CLOCK_GPIO_H_
#define CLOCK_GPIO_H_

#include <msp430.h>

extern unsigned int ADC_value;

void gpio();
void adcSetup(void);
void adcReadConv(void);
void displaySeg(void);

#endif /* CLOCK_GPIO_H_ */
