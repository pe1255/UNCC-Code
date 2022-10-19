/*
Program 1C: Determine the Nesting Depth

By: Eric Lee

*/

#include <iostream>
#include <cstdlib>
#include <string>

using namespace std;

int main() {
	int counter = 0, deepestNested = 0;
	string input;

	while (!cin.eof()) {
		cin >> input;
		//if string is begin start counting
		if (input == "begin")
			counter++;		
		// if string is end the counter is reseted
		else if (input == "end") {
			//keeps only the highest number deeply nested begin/end pair
			if(deepestNested <= counter)
				deepestNested = counter;
			cout << "Max is " << deepestNested << endl;
			counter = 0;
		}
		else
			break;
	}

	cout << "Max is " << deepestNested << endl;	
	
	return EXIT_SUCCESS;
}