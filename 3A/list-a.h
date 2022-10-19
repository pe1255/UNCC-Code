#ifndef LIST_A_H
#define LIST_A_H

#include <string>
#include <iostream>
using namespace std;

class Node {
public:
    string id;
    Node* next;

    Node(string id, Node* next = nullptr) {
        this->id = id;
        this->next = next;
    }
};

class List
{
public:
    Node* head;           //stores head node
    int size;

    List() {
        head = nullptr; //initializes list
        size = 0;
    }

    Node* first() const {
        return head; // to return address of first node
    }

    friend istream& operator>> (istream& sin, List& lst);   //list is input
    friend ostream& operator<< (ostream& sout, List& lst);   //print list
    void prepend(string id);   //attatches node at head
    void append(string id);   //attatches node at end

    bool is_empty() const;       //checks for an empty list
    void reverse();       // list is reversed
    bool has_id(const string& id) const;   //seeks out the id in the list

    // adding additional methods required
    void remove(); //remove from front
    int getSize() const; // give the size of the List
};

#endif //LIST_A_H