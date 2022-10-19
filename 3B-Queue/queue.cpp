#include <bits/stdc++.h>
using namespace std;

struct Node {
	double time;
	Node* next;
	Node(double d)
	{
		time = d;
		next = NULL;
	}
};

struct Queue {
	Node* front, * rear;
	Queue()
	{
		front = rear = NULL;
	}

	void enQueue(double x)
	{
		Node* temp = new Node(x);
		// If queue is empty, then new node is front and rear both
		if (rear == NULL) {
			front = rear = temp;
			return;
		}

		// Add the new node at the end of queue and change rear
		rear->next = temp;
		rear = temp;
	}

	void deQueue()
	{
		if (front == NULL)
			return;

		// Store previous front and move front one node ahead
		Node* temp = front;
		front = front->next;

		// If front becomes NULL, then change rear also as NULL
		if (front == NULL)
			rear = NULL;
		delete (temp);
	}
};
int main()
{
	double time;
	string action;
	int personsinline = 0;
	double totaltime = 0;
	int totalprsn = 0;
	Queue line;
	while (cin >> time)
	{
		cin >> action;
		if (action == "exit")
		{
			//if someone exit when there are no customers in line
			if (personsinline == 0)
			{
				cout << "Non existant customer exited the line";
				return 1;
			}
			else
			{
				personsinline--;
				totaltime += time - ((line.front)->time);
				//remove the front person from line
				line.deQueue();
			}
		}
		else if (action == "enter")
		{
			personsinline++;
			totalprsn++;
			//add person to the back of line
			line.enQueue(time);
		}
		//if action is something else except "enter" or "exit"
		else
		{
			cout << "syntax error around" << action;
			return 1;
		}
	}
	//if no one exits
	if (totalprsn == personsinline)
	{
		cout << "No customers exited, so there is no wait times to average.";
		return 0;
	}
	cout << "Avg time spent in line is: ";
	if (personsinline == 0)
	{
		//if there are no person left in line
		cout << totaltime / totalprsn;
	}
	else
	{
		//if some person are left in line
		cout << totaltime / (totalprsn - personsinline) << endl << "However, some people are still in line";
	}

}