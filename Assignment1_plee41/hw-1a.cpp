/*
Program 1A: Simple Control-Break

By: Eric Lee

*/

#include <iostream>
#include <cstdio>
#include <iomanip>

using namespace std;

int main() {
	int accNum, expense, prevAccNum;
	int skipAccNum = 0, skipExpense = 0;
	int total = 0;
	int grandTotal = 0;
	int counter = 0;

	cout << setw(12) << "Account Number" << setw(12) << "Expense" << endl;
	cout << setfill('-') << setw(27) << "" << endl;
	cout << setfill('\0');

	while (!cin.eof()) {
		cin >> accNum >> expense;
		// if account number the same stays in same section
		prevAccNum = accNum;
		//adds in the skipped account and expsense when previous account
		// is not the same
		if (skipAccNum != 0) {
			cout << setw(19) << left << skipAccNum
				<< left << skipExpense << endl;
			total += skipExpense;
			grandTotal += skipExpense;
			skipExpense = 0;
			skipAccNum = 0;
		}
		//keeps same account number with its expenses
		while (prevAccNum == accNum) {
			cout << setw(19) << left << accNum
				<< left << expense << endl;

			total += expense;
			grandTotal += expense;
			skipExpense = 0;

			cin >> accNum >> expense;
			skipAccNum = accNum;
			skipExpense = expense;

			if (accNum == 0)
				break;
		}
		// Once account number is not the same show sub total
		cout << left << "sub-total = " << total << endl << endl;
		total = 0;
		if (accNum == 0)
			break;
	}

	cout << left << "grand-total = " << grandTotal << endl;		

	return EXIT_SUCCESS;
	}
