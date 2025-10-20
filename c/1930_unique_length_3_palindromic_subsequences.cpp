#include<iostream>
#include<climits>
#include<string>
#include<vector>
#include<unordered_set>
using namespace std;

class Solution {
public:
    int countPalindromicSubsequence(string s) {
        vector<int> charMinIndex(26, INT_MAX), charMaxIndex(26,INT_MIN);

        for(int i = 0; i < s.size(); i++) {
            int charIndex = s[i] - 'a';
            charMinIndex[charIndex] = min(charMinIndex[charIndex], i);
            charMaxIndex[charIndex] = max(charMaxIndex[charIndex], i);
        }

        int uniqueCount = 0;

        for (int charIndex = 0; charIndex < 26; charIndex++) {
        
            if (charMinIndex[charIndex] == INT_MAX || charMaxIndex[charIndex] == INT_MIN) {
                continue;
            }

            unordered_set<char> uniqueCharsBetween;
            
            for (int j = charMinIndex[charIndex] + 1; j < charMaxIndex[charIndex]; j++) {
                uniqueCharsBetween.insert(s[j]);
            }

            uniqueCount += uniqueCharsBetween.size();
        }

        return uniqueCount;
    }
};