/***************************************************************************
* Eric Lee
* This is a program for a stack that stores data and removes data from stack
* 
***************************************************************************/
#ifndef STACK_H
#define STACK_H

#include "list-a.h"
#include <algorithm>

class Stack : public List {
public:
    friend istream& operator>> (istream& sin, Stack& stack);   //list is input
    friend ostream& operator<< (ostream& sout, Stack& stack);   //print list
private:
    void push(string id);
    void add();
    string print();
    void dump() const;
    bool isNumber(string id) const;
};

// check whether a string is a number or not
bool Stack::isNumber(string id) const {
    // checks if string is not empty and all the char in string is digit then its a number
    for (int i = 0; i < id.size(); ++i) {
        // if first char is digit or "-ve" then its fine
        if (i == 0 && (::isdigit(id[i]) || id[i] == '-')) 
            continue;
        // for rest of the char, see if its a digit
        if (!::isdigit(id[i])) 
            return false;
    }
    return true;
}

//will overload >> in order to accept input as a list
istream& operator>> (istream& sin, Stack& stack) {
    cout << "Starting input stage.\n";
    string id;
    while (getline(sin, id)) {
        if (id == "^D") 
            break;

        if (stack.isNumber(id)) // if number then push to string
            stack.push(id);
        else {
            if (id == "add") 
                stack.add();
            else if (id == "print") 
                cout << stack.print() << endl;
            else if (id == "dump") 
                stack.dump();
        }
    }
    return sin;
}

//overlading << to output the list provided
ostream& operator<< (ostream& sout, Stack& stack) {
    string stackStr = "Size: " + to_string(stack.sz) + " [";   //to print brackets shown in example
    Node* curr = stack.head;
    //will output the elements
    while ((curr != nullptr) && (curr->next != nullptr)) {
        stackStr += (curr->id + ", ");
        curr = curr->next;
    }

    //adds in the final node
    if (curr)
        stackStr += curr->id;

    stackStr += "]";

    sout << stackStr << endl;
    //will return the object from the stream
    return sout;
}

void Stack::push(string id) {
    prepend(id);
}

string Stack::print() {
    if (head == nullptr) return "Stack is empty.";
    string id = head->id; // store the head-id
    remove(); // call the List remove method to remove head
    return id;
}

void Stack::add() {
    if (sz < 2) return; // if size if less than 2, we don't need to do anything
    // extract two nodes
    string id1 = head->id;
    remove();
    string id2 = head->id;
    remove();
    // stoi -> converts string to int
    // to_string -> converts int to string
    string id = to_string(stoi(id1) + stoi(id2));
    push(id);
}

void Stack::dump() const {
    cout << "[top]----------\n";
    Node* temp = head;
    while (temp) {
        cout << temp->id << '\n';
        temp = temp->next;
    }
    cout << "[bot]TTTTTTTTTT\n";

}

#endif // STACK_H