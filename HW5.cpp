// Eric Lee, HW5 ECGR 3180, 9/27/2022 
/*
Write a function that returns if a string of paranthesis are matched.
You are required to use the STL stack datastructure in your code for O(n) time complexity.
See 5.17 in the book for problem description and a stack based algorithm.
*/
#include <iostream>
#include <stack>
#include <vector>

using namespace std;

// function to check if paranthesis are balanced 
bool areParanthesisBalanced(string expr) {
    // Your code here
    char in = 'tmp', temp;

    std::stack<char> s;
    // Fill stack up with char 
    for (int i = 0; i < expr.size(); i++) {
        temp = int(expr[i]);
        s.push(temp);

        //checks if s.top has a match with previous input
        if (temp == ')' && in == '(') {
            s.pop();
            s.pop();
        }
        if (temp == ']' && in == '[') {
            s.pop();
            s.pop();
        }
        if (temp == '}' && in == '{') {
            s.pop();
            s.pop();
        }

        // helps assign a previous/new input value after s.pop or when filling stack 
        if (s.empty() == false)
            in = s.top();
    }

    return s.empty();
}

// Test - DO NOT MODIFY
int main()
{
    vector<string> parans = { "{()}[]", "[[", "))", "{[()]}", "({[])}" };

    for (auto expr : parans) {
        if (areParanthesisBalanced(expr))
            cout << "Balanced" << endl;
        else
            cout << "Not Balanced" << endl;
    }
    return 0;
}
