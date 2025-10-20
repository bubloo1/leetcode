#include<iostream>
#include<string>
using namespace std;

class Solution {
public:
    int titleToNumber(string columnTitle) {
        int result = 0;
        for (char c : columnTitle) {
            result = result * 26 + (c - 'A' + 1);
        }
        return result;
    }
};

int main() {
    Solution sol;
    cout << sol.titleToNumber("A") << endl;     // 1
    cout << sol.titleToNumber("Z") << endl;     // 26
    cout << sol.titleToNumber("AA") << endl;    // 27
    cout << sol.titleToNumber("AB") << endl;    // 28
    cout << sol.titleToNumber("ZY") << endl;    // 701
    return 0;
}


