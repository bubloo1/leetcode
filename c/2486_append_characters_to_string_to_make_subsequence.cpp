#include<iostream>
#include<string>
using namespace std;

class Solution {
    public:
        int appendCharacters(string s, string t) {
            int lenOfS = s.length();
            int matchedSubseqLen = 0;
            int start = 0;
            while (start < lenOfS)
            {
                if (s[start] == t[matchedSubseqLen]) {
                    matchedSubseqLen++;
                } 
                start++;
            }
            
            return t.length() - matchedSubseqLen;
        }
};

int main () {
    Solution sol;
    cout << sol.appendCharacters("z", "abcde") << endl;
    return 0;
}