/*
Leetcode Problem 242 - Valid Anagram

 Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

NOTE: Your code has to run in O(n) time where n is the number of letters.
Zero points for any non-O(n) algorithm.
*/

#include <iostream>
#include <unordered_map>

using namespace std;
bool isAnagram(string s, string t);


int main() {
	string s = "anagram";
	string t = "nagaram";
	if (isAnagram(s, t)) cout << "True" << endl;
	else cout << "False" << endl;
	s = "rat";
	t = "car";
	if (isAnagram(s, t)) cout << "True" << endl;
	else cout << "False" << endl;
}

bool isAnagram(string s, string t) {
	// Your code here
	unordered_map<char, int> anagramMap1;
	unordered_map<char, int> anagramMap2;
	int counter = 1;
	
	// Finds how many of each letter there is for first word
	for (int i = 0; i < s.size(); i++) {
		unordered_map<char, int>::const_iterator got = anagramMap1.find(s[i]);
		anagramMap1[s[i]] = 1;
		// will look through map to see if letter was previously inputed
		// adds 1 if finds a letter that repeats
		if (got != anagramMap1.end()) {
			counter++;
			anagramMap1[s[i]] = counter;
		}

	}
	counter = 1;
	// Finds how many of each letter there is for second word
	for (int i = 0; i < t.size(); i++) {
		unordered_map<char, int>::const_iterator got = anagramMap2.find(t[i]);
		anagramMap2[t[i]] = 1;
		// will look through map to see if letter was previously inputed
		// adds 1 if finds a letter that repeats
		if (got != anagramMap2.end()) {
			counter++;
			anagramMap2[t[i]] = counter;
		}

	}
	/*
	// Prints out maps
	for (auto& x : anagramMap1) {
		std::cout << x.first << ": " << x.second << std::endl;
	}
	cout << endl;
	for (auto& y : anagramMap2) {
		std::cout << y.first << ": " << y.second << std::endl;
	}
	*/

	return (anagramMap1 == anagramMap2);
}
