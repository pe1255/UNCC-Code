/*
Program 1B: Last N-elements of a Sequence

By: Eric Lee

*/

#include <iostream>
#include <cstdlib>
#include <iomanip>

using namespace std;

const int arrSize = 3;

int main() {
    //for array placement
    int i = 0;
    int sum = 0, numInputs = 0, input;
    //array for last three inputs
    int lastThree[arrSize];

    while (!cin.eof()) {
        cin >> input;
        if (input == 0)
            break;
        numInputs++;
        sum += input;
        //saves the last three inputs
        lastThree[i] = input;
        i++;
        // loop back in order to keep last three inputs in array
        if (i == 3)
            i = 0;
    }

    cout << "number-of-inputs = " << numInputs
        << setw(10) << "sum = " << sum << endl;
    // output last three inputs from most recent input     
    for (int j = 2; j >= 0; j--)
        cout << lastThree[j] << endl;

    return EXIT_SUCCESS;
}