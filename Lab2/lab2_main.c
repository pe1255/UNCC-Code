#include <msp430.h> 
#include "lab2func.h"

unsigned int ADC_value = 0;

void main(void)
{   gpio();
    adcSetup();

	while(1) {
	    adcReadConv();
	}
}
