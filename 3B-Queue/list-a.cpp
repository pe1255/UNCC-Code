#include "list-a.h"

//will overload >> in order to accept input as a list
istream& operator>> (istream& sin, List& lst) {
	Node* tmp;           //node is stored
	string id;
	sin >> id;           //input node
	while (sin) {
		if (id == "^D")
			break;
		tmp = new Node(id, lst.head);
		lst.sz += 1;
		lst.head = tmp;
		sin >> id;
	}
	//will return istream for object reference
	return sin;
}

//overlading << to output the list provided
ostream& operator<< (ostream& sout, List& lst) {
	string list_str = "Size: " + to_string(lst.sz) + "[";   //to print brackets shown in example
	Node* curr = lst.head;
	//will output the elements
	while ((curr != nullptr) && (curr->next != nullptr)) {
		list_str += (curr->id + ", ");
		curr = curr->next;
	}

	//adds in the final node
	if (curr)
		list_str += curr->id;

	list_str += "]";

	sout << list_str << endl;
	//will return the object from the stream
	return sout;
}

//puts node at the front
void List::prepend(string id) {
	Node* newNode = new Node(id);
	sz += 1;
	newNode->next = head;
	head = newNode;
}

//puts node at the end
void List::append(string id) {
	Node* newNode = new Node(id);
	sz += 1;
	//for if there is an empty list
	if (head == NULL) {
		head = newNode;
		return;
	}

	//puts node at the end of the list
	Node* curr = head;
	//teleport to final node
	while (curr->next)
		curr = curr->next;
	//links are adjusted
	curr->next = newNode;
}


//this will check if the list is empty

bool List::is_empty() {
	if (head == NULL)
		return true;
	else
		return false;
}

//reverses the inputted list
void List::reverse() {

	Node* temp = NULL;
	Node* prev = NULL;
	Node* current = head;
	while (current != NULL) {
		temp = current->next;
		current->next = prev;
		prev = current;
		current = temp;
	}
	head = prev;
}

//seek id in the list
bool List::has_id(string id) {
	Node* curr = head;
	//jump to last node
	while (curr->next) {
		if (curr->id == id)
			break;
		curr = curr->next;
	}

	if (curr == NULL)
		return false;
	else
		return true;

}

// this will remove a element from the list 
void List::remove() {
	// check if list is empty
	if (is_empty()) return;
	Node* temp = head;
	head = head->next;
	sz -= 1;
	delete temp;
}

int List::getSize() const {
	return sz;
}