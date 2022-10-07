// HW1 ECGR 3180, Eric Lee 8/30

#include <iostream>
#include <vector>
std::vector<double> vecProduct(const std::vector<double>& v1, const
	std::vector<double>& v2) {
	// Your code here
	// Return empty vector if v1 and v2 are of different sizes;
	double ans;
	std::vector<double> result;

	if (v1.size() == v2.size()) {
		for (int i = 0; i < v1.size(); i++) {
			ans = v1[i] * v2[i];
			result.push_back(ans);
			std::cout << "Product " << result[i] << std::endl;
		}
	}
	return result;
}
// Overload << operator to print std::vector
std::ostream& operator <<(std::ostream& os, const std::vector<double>& v) {
	for (int i = 0; i < v.size(); i++) {
		os << v.at(i) << " ";
	}
	os << std::endl;
	return os;
}
// Test (No need to touch Test)
int main() {
	// Test 1
	std::vector<double> v1{ 1.0, 2.0, 3.0 };
	std::vector<double> v2{ 4.0, 5.0, 6.0 };
	std::vector<double> v3 = vecProduct(v1, v2);
	std::cout << v3; // Should print 4, 10, 18
	// Test 2
	std::vector<double> v4{ 42.0 };
	std::cout << vecProduct(v1, v4); // Should print empty vector
}