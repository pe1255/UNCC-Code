// Midterm Q1, ECGR 3180, Eric Lee, 10/8/2022
// For an input string of words, find the most frequently occuring word. In case of ties, report any one of them. 
// Your algorithm should be O(n) time where n is the number of words in the string
#include <iostream>
#include <vector>
#include <sstream>
#include <unordered_map>

using namespace std;


string findWord(vector<string>& tokens);

int main() {
	string line = "I felt happy because I saw the others were happy and because I knew I should feel happy but I wasn’t really happy";

	// Convert string to a vector of words
	char delimiter = ' ';
	string token;
	istringstream tokenStream(line);
	vector<string> tokens;
	while (getline(tokenStream, token, delimiter)) {
		tokens.push_back(token);
	}
	cout << "The most frequently occuring word is: " << findWord(tokens) << endl;

}

string findWord(vector<string>& tokens) {
	// Your code here
	unordered_map<string, int> mostFreqWord;
	string max = "t";
	int maxValue = 0;

	for (int i = 0; i < tokens.size() - 1; i++) {
		unordered_map<string, int>::const_iterator got = mostFreqWord.find(tokens[i]);
		// will see if the word is already present, if it is then it is assigned 1
		if (got == mostFreqWord.end())
			mostFreqWord[tokens[i]] = 1;
		// will look through map to see if letter was previously inputed
		// adds 1 if finds a word that repeats
		if (got != mostFreqWord.end())
			mostFreqWord[tokens[i]] = mostFreqWord.at(tokens[i]) + 1;
	}
	// this will find the word that occurs the most and returns it
	for (auto& x : mostFreqWord) {
		if (maxValue < x.second) {
			max = x.first;
			maxValue = x.second;
		}
	}
	return max;
}


