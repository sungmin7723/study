#include<iostream>
#include<string>

using namespace std;

int main() {
	int A, B;
	cin >> A >> B;
	if (A > B) {
		cout << ">";
	}
	else if (A < B) {
		cout << "<";
	}
	else if (A == B) {
		cout << "==";
	}
	return 0;
}