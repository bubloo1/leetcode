#include<iostream>
#include<vector>
using namespace std;

class Solution {
public:
    double averageWaitingTime(vector<vector<int>>& customers) {
        long long currentTime = 0;
        long long totalWaitTime = 0;

        for (const vector<int>& customer : customers) {
            int arrival = customer[0];
            int timeToCook = customer[1];

            // If chef is free before the customer arrives, wait till they arrive
            currentTime = max(currentTime, (long long)arrival);
            currentTime += timeToCook;

            totalWaitTime += currentTime - arrival;
        }

        return (double)totalWaitTime / customers.size();
    }
};

int main() {
    Solution sol;
    vector<vector<int>> customersInput = {{1,2},{2,5},{4,3}};
    cout << sol.averageWaitingTime(customersInput) << endl;
    return 0;
}